import torch

from geometry_mmalls.geometry import paired_route_geometry_loss_stationary, stationary_route_target


def _routes(batch: int, angles: int, hosts: int = 4) -> torch.Tensor:
    logits = torch.randn(batch, angles, hosts, requires_grad=True)
    return torch.softmax(logits, dim=-1), logits


def test_stationary_route_loss_backward_is_finite():
    routes, logits = _routes(8, 5)
    factors = torch.tensor([-60.0, -30.0, 0.0, 30.0, 60.0])
    loss = paired_route_geometry_loss_stationary(routes, factors)
    loss.backward()
    assert torch.isfinite(loss)
    assert logits.grad is not None and torch.isfinite(logits.grad).all()


def test_same_factor_gap_has_same_target_across_curriculum_spans():
    gap = torch.tensor([30.0])
    early_stage_target = stationary_route_target(gap, max_factor_span=120.0)
    full_stage_target = stationary_route_target(gap, max_factor_span=120.0)
    expected = torch.sin(torch.tensor(torch.pi / 8.0))
    assert torch.allclose(early_stage_target, full_stage_target)
    assert torch.allclose(early_stage_target, expected[None], atol=1e-7)


def test_collapsed_routes_are_penalized_for_nonzero_factor_gaps():
    routes = torch.full((6, 5, 4), 0.25)
    factors = torch.tensor([-60.0, -30.0, 0.0, 30.0, 60.0])
    loss = paired_route_geometry_loss_stationary(routes, factors)
    assert loss > 0.05


def test_stationary_loss_is_permutation_equivariant_over_angles():
    routes, _ = _routes(5, 5)
    factors = torch.tensor([-60.0, -30.0, 0.0, 30.0, 60.0])
    permutation = torch.tensor([2, 4, 0, 3, 1])
    original = paired_route_geometry_loss_stationary(routes, factors)
    permuted = paired_route_geometry_loss_stationary(
        routes[:, permutation], factors[permutation]
    )
    assert torch.allclose(original, permuted, atol=1e-6, rtol=1e-6)
