import numpy as np

from geometry_mmalls.memory import ReconstructiveAuditMemory, SyntheticFunctionalMemory, TraceRecord


def test_reconstructive_memory_fidelity():
    mem = ReconstructiveAuditMemory()
    z = np.array([1.0, 2.0, 3.0])
    rec = TraceRecord(sample_id="a", stage=1, context=np.zeros(2), route=np.array([0.7, 0.3]), z_mm=z)
    mem.add(rec)
    assert len(mem) == 1
    assert mem.by_stage(1)[0].sample_id == "a"
    assert mem.reconstruction_fidelity("a", z) > 0.999999


def test_synthetic_memory_updates_prototype():
    mem = SyntheticFunctionalMemory()
    mem.update("role-0", np.array([1.0, 0.0]), momentum=0.5)
    mem.update("role-0", np.array([0.0, 1.0]), momentum=0.5)
    proto = mem.get("role-0")
    assert np.allclose(proto, np.array([0.5, 0.5]))
    assert mem.count("role-0") == 2
