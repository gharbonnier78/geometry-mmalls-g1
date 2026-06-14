# Instructions de migration : v1.0.6 → v1.0.7
## Geometry-MMALS G1 — Context-Bottleneck Experiment

**Objectif scientifique de v1.0.7**  
Trancher la question ouverte laissée par v1.0.6 : l'échec de la médiation contextuelle vient-il d'un
raccourci architectural (le routeur préfère z0 parce qu'il est disponible), ou d'un problème de
représentation plus profond (le contexte inféré ne contient pas d'information géométrique exploitable) ?

**Intervention centrale :** supprimer ou bloquer l'accès de z0 dans le routeur, en plusieurs variantes
contrôlées, et mesurer si le contexte *forcé* produit un effet géométrique et causal.

---

## 1. Fichiers à modifier

| Fichier | Nature du changement |
|---|---|
| `src/geometry_mmalls/model.py` | Ajout `ContextBottleneckRouter` + nouveau mode `context_bottleneck` dans `forward_with_router_mode` |
| `configs/rotated_mnist_g1_v107.yaml` | Nouveau fichier de config avec les hyperparamètres v1.0.7 |
| `src/geometry_mmalls/__init__.py` | Bump version `1.0.6` → `1.0.7` |
| `notebooks/Geometry_MMALS_G1_ContextBottleneck_v1_0_7.ipynb` | Nouveau carnet (fork de v1.0.6) |
| `CHANGELOG.md` | Section v1.0.7 |

---

## 2. Modification de `model.py`

### 2a. Ajouter la classe `ContextBottleneckRouter`

Insérer après la classe `ResidualHost`, avant `MMALSTrace` :

```python
class ContextBottleneckRouter(nn.Module):
    """Router that receives only the inferred context, not z0 directly.

    The context encoder is made more expressive (two hidden layers) to avoid
    giving the bottleneck an architectural disadvantage relative to the
    standard router.  z0 is never passed here; any geometric order learned
    by this router must come through the context path.
    """

    def __init__(self, context_dim: int, num_hosts: int, hidden_dim: int = 128) -> None:
        super().__init__()
        self.net = nn.Sequential(
            nn.Linear(context_dim, hidden_dim),
            nn.GELU(),
            nn.Linear(hidden_dim, hidden_dim),
            nn.GELU(),
            nn.Linear(hidden_dim, num_hosts),
        )

    def forward(self, context: torch.Tensor) -> torch.Tensor:
        return self.net(context)
```

### 2b. Ajouter le `context_bottleneck_router` dans `GeometryMMALS.__init__`

Dans `GeometryMMALS.__init__`, après la ligne `self.router = nn.Sequential(...)` :

```python
        self.context_bottleneck_router = ContextBottleneckRouter(
            context_dim=context_dim,
            num_hosts=num_hosts,
            hidden_dim=64,
        )
```

### 2c. Ajout du mode dans `forward_with_router_mode` (dans le notebook)

Dans la fonction `forward_with_router_mode` du carnet, dans le bloc `if/elif` sur `router_mode`,
ajouter après `elif router_mode == "context_only":` :

```python
    elif router_mode == "context_bottleneck":
        # Uses the dedicated ContextBottleneckRouter — never sees z0.
        route_logits = model.context_bottleneck_router(context_for_router)
        route = torch.softmax(route_logits, dim=-1)
    elif router_mode == "context_bottleneck_geo":
        # Same as context_bottleneck but also receives geometry loss.
        route_logits = model.context_bottleneck_router(context_for_router)
        route = torch.softmax(route_logits, dim=-1)
    elif router_mode == "context_bottleneck_stopgrad":
        # Stop-gradient sur z0 avant context_net :
        # le contexte est calculé à partir d'un z0 détaché, forçant le
        # context_net à s'optimiser sans recevoir de gradient de la CE.
        z0_detached = z0.detach()
        context_sg = model.context_net(z0_detached)
        route_logits = model.router(torch.cat([z0_detached, context_sg], dim=-1))
        route = torch.softmax(route_logits, dim=-1)
```

**Note** : `context_bottleneck_stopgrad` est la variante la moins invasive — elle garde l'architecture
standard mais coupe le gradient qui permet au routeur d'apprendre à exploiter z0 directement.

---

## 3. Fichier `configs/rotated_mnist_g1_v107.yaml`

Copier `rotated_mnist_g1_v106.yaml` et modifier uniquement :

```yaml
version: "1.0.7"
experiment:
  name: context_bottleneck
  hypothesis: >
    If context-mediation failure in v1.0.6 was architectural (sensory shortcut),
    then a bottleneck router that cannot see z0 should produce measurable
    context geometry order under geometry regularization.
  falsification_condition: >
    If context_bottleneck_geo fails to improve context-space Spearman rho
    above the v1.0.6 baseline with a CI excluding zero, the failure is
    representational, not architectural.
```

Laisser tous les autres hyperparamètres identiques à v1.0.6.

---

## 4. Nouveau `METHOD_SPECS` dans le carnet v1.0.7

Remplacer le bloc `METHOD_SPECS` par celui-ci :

```python
METHOD_SPECS = {
    # --- Contrôles hérités de v1.0.6 (inchangés, pour comparaison directe) ---
    "paired_anchor_adaptive_no_geometry": {
        "paired": True, "geometry_weight": 0.0, "anchor_weight": 0.10,
        "router_mode": "standard",
    },
    "paired_anchor_uniform_static": {
        "paired": True, "geometry_weight": 0.0, "anchor_weight": 0.10,
        "router_mode": "uniform_static",
    },
    # --- Nouvelles variantes v1.0.7 : context-bottleneck ---
    "bottleneck_anchor_no_geo": {
        "paired": True, "geometry_weight": 0.0, "anchor_weight": 0.10,
        "router_mode": "context_bottleneck",
    },
    "bottleneck_anchor_geo": {
        "paired": True, "geometry_weight": 0.10, "anchor_weight": 0.10,
        "router_mode": "context_bottleneck_geo",
    },
    "stopgrad_anchor_no_geo": {
        "paired": True, "geometry_weight": 0.0, "anchor_weight": 0.10,
        "router_mode": "context_bottleneck_stopgrad",
    },
    "stopgrad_anchor_geo": {
        "paired": True, "geometry_weight": 0.10, "anchor_weight": 0.10,
        "router_mode": "context_bottleneck_stopgrad",
    },
}
```

**Rationnel du choix des 6 variantes :**

| Variante | Ce qu'elle teste |
|---|---|
| `paired_anchor_adaptive_no_geometry` | Ligne de base v1.0.6, shortcut actif, sans géo |
| `paired_anchor_uniform_static` | Plancher statique, référence opérationnelle |
| `bottleneck_anchor_no_geo` | Le bottleneck seul améliore-t-il la tâche ? |
| `bottleneck_anchor_geo` | **Contraste principal** : bottleneck + géo → context order |
| `stopgrad_anchor_no_geo` | Variante douce : stop-grad sans nouvelle architecture |
| `stopgrad_anchor_geo` | Variante douce + géo |

---

## 5. Nouvelles métriques à ajouter dans le carnet

### 5a. Médiation diagnostic obligatoire (déjà dans v1.0.6, à conserver)

Conserver intégralement la section 11 (router mediation interventions).  
Pour les modes bottleneck, adapter l'intervention `router_z0_zeroed` : dans `context_bottleneck`,
z0 n'est jamais passé au routeur, donc l'intervention équivalente est de **zeroing le contexte**
(`router_context_zeroed`) — qui doit maintenant causer une chute mesurable si le bottleneck
fonctionne. C'est le test de falsification central.

Exporter dans `mediation_dependency_summary.csv` la colonne `context_to_z0_shift_ratio` pour
chaque méthode. La question est : ce ratio passe-t-il au-dessus de 1.0 pour les variantes bottleneck ?

### 5b. Nouveau contraste dans `PAIRED_CONTRASTS`

Ajouter :

```python
("bottleneck_geo_effect", "bottleneck_anchor_geo", "bottleneck_anchor_no_geo"),
("bottleneck_vs_standard",  "bottleneck_anchor_geo", "paired_anchor_adaptive_no_geometry"),
("stopgrad_geo_effect",     "stopgrad_anchor_geo",   "stopgrad_anchor_no_geo"),
```

Ces trois contrastes permettent de décomposer proprement :
1. l'effet de la géo dans le bottleneck (bottleneck_geo_effect)
2. le gain total bottleneck+géo vs baseline v1.0.6 (bottleneck_vs_standard)  
3. l'effet stop-grad seul (stopgrad_geo_effect)

### 5c. Table de diagnostic de médiation étendue

Dans la section médiation, exporter par méthode :

```python
mediation_summary_rows.append({
    "method": method,
    "context_route_shift_mean": ...,   # déjà présent
    "z0_route_shift": ...,              # déjà présent
    "context_to_z0_shift_ratio": ...,  # déjà présent
    "context_accuracy_drop": ...,      # NOUVEAU : chute d'accuracy quand contexte zéroé
    "z0_accuracy_drop": ...,           # NOUVEAU : chute d'accuracy quand z0 zéroé
    "context_is_primary": context_to_z0_shift_ratio > 1.0,  # NOUVEAU : flag binaire
})
```

Le flag `context_is_primary` est la condition de succès la plus lisible pour un reviewer.

---

## 6. Changements tracked (bloc `tracked_changes` dans le manifest)

```python
TRACKED_CHANGES_107 = [
    "CHG-107-01 - ContextBottleneckRouter: dedicated router receiving only inferred context",
    "CHG-107-02 - context_bottleneck router mode: no z0 access at any point",
    "CHG-107-03 - context_bottleneck_geo router mode: same + geometry regularization",
    "CHG-107-04 - context_bottleneck_stopgrad mode: stop-gradient on z0 before context_net",
    "CHG-107-05 - Extended mediation table: context_accuracy_drop and context_is_primary flag",
    "CHG-107-06 - Three new paired contrasts: bottleneck_geo_effect, bottleneck_vs_standard, stopgrad_geo_effect",
    "CHG-107-07 - METHOD_SPECS reduced to 6 targeted variants (removed redundant v1.0.6 methods)",
    "CHG-107-08 - Config v107 with explicit hypothesis and falsification condition",
    "CHG-107-09 - Package version bumped to 1.0.7",
    "CHG-107-10 - Primary curriculum kept as cb_a for comparability with v1.0.6",
]
```

---

## 7. Ce qu'on NE change PAS

- Curriculum : garder `cb_a` comme curriculum primaire (comparabilité directe v1.0.6).
- Splits : mêmes hash de sources. `split_manifest` identique.
- Sensory encoder : toujours gelé, même architecture, mêmes poids.
- Evidence ladder : C0–C6 inchangée. v1.0.7 vise spécifiquement C1-contexte.
- `STAGE_EPOCHS`, `BOOTSTRAP_SAMPLES`, `RUN_MODE` : identiques à v1.0.6.
- Les 4 curricula contrebalancés : les conserver si `RUN_COUNTERBALANCED_CURRICULA=True`,
  mais les appliquer uniquement à `bottleneck_anchor_geo` pour économiser du compute.

---

## 8. Interprétation attendue des résultats

### Scénario A — Succès architectural (hypothèse principale)
`context_to_z0_shift_ratio > 1.0` pour `bottleneck_anchor_geo`,  
ET `delta_rho_context > 0` avec CI excluant zéro pour `bottleneck_geo_effect`.

→ Conclusion : l'échec v1.0.6 était un shortcut architectural. Le contexte contient  
de l'information géométrique. Prochaine étape : forcer ce bottleneck dans l'architecture  
standard sans sacrifier l'accuracy.

### Scénario B — Échec représentationnel
`context_to_z0_shift_ratio` reste < 0.1 même pour `context_bottleneck`,  
ET `delta_rho_context` reste plat ou négatif.

→ Conclusion : le context_net n'apprend pas de représentation géométriquement ordonnée  
même quand il est la seule entrée du routeur. Problème de capacité ou de supervision.  
Piste : augmenter context_dim (2 → 8), ajouter une supervision directe angle→contexte  
(régression auxiliaire), ou reconsidérer la définition du contexte.

### Scénario C — Résultat mixte (le plus probable)
`stopgrad_anchor_geo` améliore légèrement context order,  
mais `bottleneck_anchor_geo` dégrade l'accuracy.

→ Le contexte contient une information partielle, mais le système est sous-contraint  
sans accès à z0. Piste : gate appris (α*z0 + (1-α)*context_output pour le routeur,  
avec régularisation sur α → 0).

---

## 9. Note sur le compute

6 variantes × 5 stages × 2 epochs (dev) = charge comparable à v1.0.6 (9 variantes).  
En supprimant les variantes redondantes v1.0.6 (`paired_geometry`, `paired_geometry_anchor_010`,
`paired_anchor_context_only`, `paired_anchor_direct_z0`, `paired_anchor_learned_static`),
v1.0.7 est **plus léger** en temps de run total malgré l'ajout du `ContextBottleneckRouter`.

---

*Document généré à partir de l'analyse des CSV v1.0.6 et du carnet source v1.0.6.  
Auteur : Guillaume Harbonnier. Collaborateur analytique : Claude Sonnet 4.6.*
