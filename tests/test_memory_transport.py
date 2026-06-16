import torch

from geometry_mmalls.memory_transport import (
    compile_root_gaussian,
    distributional_functional_transport,
    distillation_kl,
    functional_path_statistics,
    functional_transport_anchor_loss,
    isotropic_root_gaussian,
    root_gaussian_nll,
    root_route_anchor_loss,
)


def _routes(seed: int, n: int = 5, hosts: int = 4) -> torch.Tensor:
    generator = torch.Generator().manual_seed(seed)
    return torch.softmax(torch.randn(n, hosts, generator=generator), dim=-1)


def _cost(hosts: int = 4) -> torch.Tensor:
    base = torch.arange(hosts, dtype=torch.float32)
    cost = torch.abs(base[:, None] - base[None, :])
    cost.fill_diagonal_(0.0)
    return cost


def test_anchor_losses_are_finite_and_zero_on_identity():
    routes = _routes(0)
    cost = _cost()
    assert torch.allclose(root_route_anchor_loss(routes, routes), torch.tensor(0.0), atol=1e-7)
    assert torch.isfinite(functional_transport_anchor_loss(routes, routes, cost))


def test_distributional_transport_is_symmetric_up_to_tolerance():
    a, b, cost = _routes(1), _routes(2), _cost()
    ab = distributional_functional_transport(a, b, cost, cloud_iterations=8, route_iterations=8)
    ba = distributional_functional_transport(b, a, cost, cloud_iterations=8, route_iterations=8)
    assert torch.isfinite(ab) and torch.isfinite(ba)
    assert float(ab) >= 0.0 and float(ba) >= 0.0


def test_path_statistics_detect_detour():
    a = _routes(3)
    b = _routes(4)
    c = a.clone()
    stats = functional_path_statistics([a, b, c], _cost(), iterations=8)
    assert stats.cumulative_length > 0
    assert stats.endpoint_distance >= 0
    assert torch.isfinite(torch.tensor(stats.path_to_endpoint_cost_ratio))
    assert stats.path_to_endpoint_cost_ratio >= 0.0
    assert stats.path_excess == stats.path_to_endpoint_cost_ratio


def test_root_gaussian_memory_has_finite_nll():
    fit = _routes(5, n=10)
    test = _routes(6, n=5)
    memory = compile_root_gaussian(fit)
    isotropic = isotropic_root_gaussian(memory)
    value = root_gaussian_nll(test, memory)
    isotropic_value = root_gaussian_nll(test, isotropic)
    expected_variance = torch.trace(memory.covariance) / memory.covariance.shape[0]
    assert memory.count == 10
    assert torch.isfinite(value) and torch.isfinite(isotropic_value)
    assert torch.allclose(
        isotropic.covariance,
        expected_variance * torch.eye(memory.covariance.shape[0]),
    )


def test_distillation_kl_is_zero_for_identical_logits():
    logits = torch.randn(8, 10)
    assert torch.allclose(distillation_kl(logits, logits), torch.tensor(0.0), atol=1e-6)
