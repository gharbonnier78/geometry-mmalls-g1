
import builtins
import importlib
import sys


def test_core_import_does_not_require_pypdf(monkeypatch):
    real_import = builtins.__import__

    def guarded_import(name, *args, **kwargs):
        if name == "pypdf" or name.startswith("pypdf."):
            raise ModuleNotFoundError("simulated missing pypdf")
        return real_import(name, *args, **kwargs)

    monkeypatch.setattr(builtins, "__import__", guarded_import)

    for name in list(sys.modules):
        if name == "geometry_mmalls" or name.startswith("geometry_mmalls."):
            del sys.modules[name]

    module = importlib.import_module("geometry_mmalls")
    assert module.__version__ == "1.1.3"


def test_verification_module_import_is_lazy(monkeypatch):
    real_import = builtins.__import__

    def guarded_import(name, *args, **kwargs):
        if name == "pypdf" or name.startswith("pypdf."):
            raise ModuleNotFoundError("simulated missing pypdf")
        return real_import(name, *args, **kwargs)

    monkeypatch.setattr(builtins, "__import__", guarded_import)

    for name in list(sys.modules):
        if name == "geometry_mmalls.verification":
            del sys.modules[name]

    module = importlib.import_module("geometry_mmalls.verification")
    assert callable(module.verify_evidence_bundle)
