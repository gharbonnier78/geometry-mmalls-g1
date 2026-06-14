# Résumé scientifique en français

## Le problème

Les expériences MMALS récentes ont utilisé une géométrie de traces d'audit et de contrôle : précision, rétention, coût, stabilité, spécialisation, route et mémoire étaient projetés dans un même espace afin de comparer des décisions. Cette couche reste utile, mais elle ne prouve pas que MMALS apprend une géométrie interne réelle.

Geometry-MMALS G1 change l'objet étudié. La géométrie doit être cherchée dans la chaîne fonctionnelle elle-même :

```text
entrée -> représentation perceptive -> contexte inféré -> route
       -> transformations des hôtes -> synthèse -> prédiction/mémoire
```

Une géométrie est dite **ancrée** lorsque la proximité d'un facteur réel connu, par exemple l'angle d'une image, correspond à une proximité mesurable des états internes. Elle devient scientifiquement intéressante seulement si elle permet aussi d'interpoler, de prévoir, d'intervenir causalement et d'améliorer le fonctionnement du système.

## Pourquoi RotatedMNIST d'abord

RotatedMNIST fournit un facteur continu observable : l'angle de rotation. Le modèle apprend sur certains angles et est évalué sur des angles intermédiaires jamais vus. Il ne suffit pas d'obtenir de beaux groupes sur une projection UMAP. Il faut vérifier que :

1. les angles voisins restent voisins dans l'espace interne ;
2. les routes changent progressivement avec l'angle ;
3. une direction latente correspondant à la rotation produit, lorsqu'on l'applique artificiellement, le changement attendu de route ou de sortie ;
4. les contraintes géométriques améliorent réellement l'interpolation, la rétention ou la stabilité.

## Ce que signifie la spécialisation d'un hôte

Un hôte n'est pas spécialisé simplement parce qu'il est souvent sélectionné. Sa spécialisation doit être locale, causale et reproductible :

- il apporte un gain dans une région définie du contexte ;
- son ablation détériore surtout cette région ;
- sa transformation se distingue de celles des autres hôtes ;
- son rôle demeure suffisamment stable au cours du continual learning ;
- le même rôle réapparaît sur plusieurs seeds, même si l'indice de l'hôte change.

La spécialisation est donc une propriété de l'écosystème MMALS complet, et non une qualité isolée de l'hôte.

## Les quatre niveaux de preuve

- **Descriptif :** ordre, distances et voisinages correspondent au facteur réel.
- **Prédictif :** les contextes non vus sont interpolés avec une erreur maîtrisée.
- **Causal :** une intervention dans une direction géométrique produit un effet spécifique, contrairement aux directions de contrôle.
- **Opérationnel :** la géométrie améliore un objectif concret face à des baselines durcies.

## Les cinq objectifs concrets

G1 doit servir au moins l'un des objectifs suivants sans dégrader arbitrairement les autres : précision, rétention, coût, stabilité sous dérive et spécialisation des hôtes.

## Ordre du programme

```text
G1 : démontrer une géométrie fonctionnelle réelle
G2 : utiliser une énergie pour router sur cette géométrie
G3 : tester des amplitudes/phases inspirées du quantique
```

Les amplitudes complexes n'ont de sens scientifique qu'après l'existence de trajectoires et de recombinaisons fonctionnelles mesurables. G1 est donc un préalable, pas une simple étape de présentation.
