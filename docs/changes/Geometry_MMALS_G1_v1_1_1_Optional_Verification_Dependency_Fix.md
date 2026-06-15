
# Geometry-MMALS G1 v1.1.1 optional verification dependency fix

## Symptom

The training notebook failed during:

```python
import geometry_mmalls
```

with:

```text
ModuleNotFoundError: No module named 'pypdf'
```

## Root cause

The package root eagerly imported:

```python
from .verification import verify_evidence_bundle, write_verification_outputs
```

The verification module imported `pypdf` at module import time. The training
notebook deliberately installs the scientific package with `--no-deps`, so an
optional PDF-verification dependency incorrectly became mandatory for all core
training runs.

## Canonical correction

Scientific version remains `1.1.1`.

Build revision becomes:

```text
bridge-isolation-common-hosts-c0-r2
```

Changes:

1. `geometry_mmalls.__init__` no longer imports the Verification Stack.
2. `geometry_mmalls.verification` imports `pypdf` lazily only inside
   `pdf_report()`.
3. The Verification Stack notebook explicitly installs `pypdf>=4.0`.
4. The main v1.1.1 notebook requires no PDF library.
5. Regression tests simulate an environment in which `pypdf` is unavailable.

## Architectural rule

The mandatory MMALS core must not depend on optional audit/reporting packages.

Use:

```python
import geometry_mmalls
```

for training and routing.

Use:

```python
from geometry_mmalls.verification import (
    verify_evidence_bundle,
    write_verification_outputs,
)
```

only in the independent verification workflow.
