
import torch

from geometry_mmalls.functional_routing import (
    SmoothSimplexResidualRouter,
    simplex_continuity_hinge_loss,
)


def test_smooth_residual_route_is_simplex_and_bounded():
    torch.manual_seed(12)
    router = SmoothSimplexResidualRouter(4, 4, residual_cap=0.35)
    context = torch.nn.functional.normalize(torch.randn(32, 4), dim=-1)
    router.initialize_from_contexts(context, seed=0)
    route = router(context)
    base, residual, gate = router.components(context)
    assert torch.allclose(route.sum(-1), torch.ones(32), atol=1e-6)
    assert residual.abs().max() <= router.residual_cap + 1e-6
    assert torch.all((gate >= 0) & (gate <= 1))


def test_continuity_hinge_zero_for_identical_routes():
    routes = torch.full((8, 3, 4), 0.25)
    contexts = torch.nn.functional.normalize(torch.randn(8, 3, 4), dim=-1)
    value = simplex_continuity_hinge_loss(routes, contexts, kappa=1.0)
    assert torch.allclose(value, torch.tensor(0.0))


def test_smooth_residual_gradients_are_finite():
    router = SmoothSimplexResidualRouter(4, 4)
    context = torch.randn(16, 4, requires_grad=True)
    loss = router(context).square().mean()
    loss.backward()
    assert torch.isfinite(context.grad).all()
