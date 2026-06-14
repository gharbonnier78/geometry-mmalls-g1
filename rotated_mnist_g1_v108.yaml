import math
import numpy as np
import torch
from torch import nn

from geometry_mmalls.functional_routing import (
    FunctionalRoutingMMALS,
    LinearContextRouter,
    MLPContextRouter,
    PrototypeEnergyRouter,
    entropic_transport_cost,
    half_chord_distance,
    host_output_cost_matrix,
    host_specialization,
    host_territory,
    pairwise_functional_route_distances,
    parameter_count,
    reconstruct_route_from_root_probe,
    root_simplex_chord,
    spherical_kmeans,
    territory_overlap,
    usage_balance_loss,
)


def test_routers_return_probability_simplex():
    context = torch.randn(12, 4)
    for router in [
        MLPContextRouter(4, 4),
        LinearContextRouter(4, 4),
        PrototypeEnergyRouter(4, 4),
    ]:
        route = router(context)
        assert route.shape == (12, 4)
        assert torch.all(route >= 0)
        assert torch.allclose(route.sum(-1), torch.ones(12), atol=1e-6)
        assert parameter_count(router) > 0


def test_prototype_energy_gradient_and_projection_are_finite():
    router = PrototypeEnergyRouter(4, 4)
    context = torch.randn(16, 4, requires_grad=True)
    route = router(context)
    loss = route.square().mean() + router.energies(context).square().mean()
    loss.backward()
    assert context.grad is not None
    assert torch.isfinite(context.grad).all()
    router.project_prototypes_()
    assert torch.allclose(router.prototypes.norm(dim=-1), torch.ones(4), atol=1e-6)


def test_spherical_kmeans_and_prototype_initialization():
    contexts = torch.nn.functional.normalize(torch.randn(64, 4), dim=-1)
    centers, assignment = spherical_kmeans(contexts, 4, seed=3)
    assert centers.shape == (4, 4)
    assert assignment.shape == (64,)
    assert torch.allclose(centers.norm(dim=-1), torch.ones(4), atol=1e-6)
    router = PrototypeEnergyRouter(4, 4)
    diagnostics = router.initialize_from_contexts(contexts, seed=3)
    assert diagnostics["min_cluster_count"] > 0
    assert torch.all(router.bandwidths > 0)


def test_root_and_context_chords_are_bounded():
    p = torch.tensor([[1.0, 0.0], [0.5, 0.5]])
    q = torch.tensor([[0.0, 1.0], [0.5, 0.5]])
    d = root_simplex_chord(p, q)
    assert torch.all(d >= 0)
    assert torch.all(d <= 1.0 + 1e-6)
    a = torch.tensor([[1.0, 0.0]])
    b = torch.tensor([[-1.0, 0.0]])
    assert torch.allclose(half_chord_distance(a, b), torch.ones(1))


def test_transport_identity_and_symmetry():
    routes = torch.tensor([
        [0.70, 0.20, 0.05, 0.05],
        [0.10, 0.70, 0.10, 0.10],
        [0.25, 0.25, 0.25, 0.25],
    ])
    cost = torch.tensor([
        [0.0, 0.2, 1.0, 1.2],
        [0.2, 0.0, 0.9, 1.1],
        [1.0, 0.9, 0.0, 0.3],
        [1.2, 1.1, 0.3, 0.0],
    ])
    pairwise = pairwise_functional_route_distances(routes, cost, epsilon=0.05)
    assert pairwise.shape == (3, 3)
    assert torch.allclose(pairwise, pairwise.T, atol=1e-5)
    assert torch.allclose(torch.diag(pairwise), torch.zeros(3), atol=1e-6)
    values = entropic_transport_cost(routes, routes, cost, epsilon=0.05)
    assert torch.isfinite(values).all()


def test_host_cost_and_ecology_metrics():
    outputs = torch.randn(20, 4, 16)
    cost = host_output_cost_matrix(outputs)
    assert cost.shape == (4, 4)
    assert torch.allclose(cost, cost.T, atol=1e-6)
    assert torch.allclose(torch.diag(cost), torch.zeros(4), atol=1e-6)
    routes = torch.softmax(torch.randn(30, 4), dim=-1)
    factors = torch.tensor([-30.0] * 10 + [0.0] * 10 + [30.0] * 10)
    unique, territory = host_territory(routes, factors)
    assert unique.shape == (3,)
    assert territory.shape == (3, 4)
    specialization = host_specialization(territory)
    overlap = territory_overlap(territory)
    assert torch.isfinite(specialization).all()
    assert overlap.shape == (4, 4)
    assert usage_balance_loss(torch.full((20, 4), 0.25)) < 1e-10


def test_root_probe_reconstruction_returns_simplex():
    q = np.array([[0.2, -0.3, 0.5, 0.1], [1.0, 1.0, 1.0, 1.0]])
    route = reconstruct_route_from_root_probe(q)
    assert np.all(route >= 0)
    assert np.allclose(route.sum(axis=1), 1.0)
