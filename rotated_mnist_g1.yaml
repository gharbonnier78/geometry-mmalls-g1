import torch

from geometry_mmalls.functional_routing import (
    HybridDirectionalPrototypeRouter,
    UniformRouter,
    local_continuity_ratio,
    permute_hosts_and_routes,
    route_weighted_synthesis,
)


def test_uniform_router_returns_exact_simplex():
    context = torch.randn(7, 4)
    route = UniformRouter(4)(context)
    assert torch.allclose(route, torch.full_like(route, 0.25))


def test_hybrid_router_is_finite_and_trainable():
    router = HybridDirectionalPrototypeRouter(4, 4)
    context = torch.randn(16, 4, requires_grad=True)
    route = router(context)
    assert torch.allclose(route.sum(-1), torch.ones(16), atol=1e-6)
    loss = route.square().mean() + router.energies(context).square().mean()
    loss.backward()
    assert context.grad is not None
    assert torch.isfinite(context.grad).all()
    assert all(p.grad is None or torch.isfinite(p.grad).all() for p in router.parameters())


def test_host_permutation_preserves_synthesis():
    route = torch.softmax(torch.randn(8, 4), dim=-1)
    hosts = torch.randn(8, 4, 12)
    permutation = torch.tensor([2, 0, 3, 1])
    route_p, hosts_p = permute_hosts_and_routes(route, hosts, permutation)
    assert torch.allclose(
        route_weighted_synthesis(route, hosts),
        route_weighted_synthesis(route_p, hosts_p),
        atol=1e-6,
    )


def test_local_continuity_ratio_is_finite():
    a = torch.nn.functional.normalize(torch.randn(8, 4), dim=-1)
    b = torch.nn.functional.normalize(a + 0.05 * torch.randn(8, 4), dim=-1)
    ratio = local_continuity_ratio(a, b, torch.rand(8))
    assert torch.isfinite(ratio).all()
    assert torch.all(ratio >= 0)
