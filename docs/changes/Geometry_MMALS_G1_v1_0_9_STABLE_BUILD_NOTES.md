# Geometry-MMALS G1 v1.0.9 — canonical stable build

**Scientific version:** 1.0.9  
**Build revision:** `stationary-route-qualification-pilot-r3`

This build incorporates the two execution-stability corrections directly
into the canonical GitHub source and notebook. No runtime source patching is
required.

## Integrated functions

### Non-negative deterministic RNG seeds

All notebook-local RNG helpers normalize integer seeds into NumPy's uint32
domain:

```python
UINT32_MODULUS = 2 ** 32

def nonnegative_rng_seed(seed):
    return int(seed) % UINT32_MODULUS
```

This covers dense negative evaluation angles such as `-75°`.

### Gradient-stable stationary route distance

The stationary route geometry uses the normalized root-space chord:

```python
root_delta = torch.sqrt(p) - torch.sqrt(q)
distance = torch.linalg.vector_norm(root_delta, dim=-1) / math.sqrt(2.0)
```

It is algebraically equivalent to `sqrt(1-affinity)` for normalized
square-root-simplex coordinates, but avoids cancellation and the singular
derivative at coincident routes.

## Regression gates

The package tests and notebook gates cover:

- random routes;
- exactly uniform/coincident routes;
- nearly coincident routes;
- dense negative-angle RNG offsets;
- finite forward loss and finite backward gradients.

## Execution

Use the stable notebook from the repository after publishing this package.
A fresh Colab runtime should clone the repository, verify package version
`1.0.9` and build revision `stationary-route-qualification-pilot-r3`, and run without any manual
source replacement.

## Claim status

These are numerical and release-integrity corrections only. The five-seed
pilot remains pending; C1-C6 remain unqualified.
