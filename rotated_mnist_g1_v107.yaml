import torch

from geometry_mmalls.model import GeometryMMALS, SmallConvEncoder


def test_model_trace_shapes():
    encoder = SmallConvEncoder(latent_dim=16)
    model = GeometryMMALS(encoder, latent_dim=16, context_dim=2, num_hosts=3, host_hidden_dim=8)
    x = torch.randn(5, 1, 28, 28)
    trace = model(x)
    assert trace.z0.shape == (5, 16)
    assert trace.context.shape == (5, 2)
    assert trace.context_raw is not None
    assert trace.context_raw.shape == (5, 2)
    assert torch.allclose(
        torch.linalg.vector_norm(trace.context, dim=-1),
        torch.ones(5),
        atol=1e-6,
    )
    assert trace.route.shape == (5, 3)
    assert trace.host_outputs.shape == (5, 3, 16)
    assert trace.z_mm.shape == (5, 16)
    assert trace.logits.shape == (5, 10)
    assert torch.allclose(trace.route.sum(dim=1), torch.ones(5), atol=1e-6)


def test_context_bottleneck_router_shapes_and_gradients():
    encoder = SmallConvEncoder(latent_dim=16)
    model = GeometryMMALS(
        encoder,
        latent_dim=16,
        context_dim=3,
        num_hosts=4,
        host_hidden_dim=8,
        bottleneck_hidden_dim=12,
    )
    context = torch.randn(6, 3, requires_grad=True)
    logits = model.context_bottleneck_router(context)
    assert logits.shape == (6, 4)
    loss = logits.square().mean()
    loss.backward()
    assert context.grad is not None
    assert torch.isfinite(context.grad).all()


def test_sensory_bottleneck_router_shapes_and_gradients():
    encoder = SmallConvEncoder(latent_dim=16)
    model = GeometryMMALS(
        encoder,
        latent_dim=16,
        context_dim=3,
        num_hosts=4,
        host_hidden_dim=8,
        bottleneck_hidden_dim=12,
    )
    z0 = torch.randn(6, 16, requires_grad=True)
    logits = model.sensory_bottleneck_router(z0)
    assert logits.shape == (6, 4)
    loss = logits.square().mean()
    loss.backward()
    assert z0.grad is not None
    assert torch.isfinite(z0.grad).all()


def test_bottleneck_router_parameter_sets_are_disjoint():
    encoder = SmallConvEncoder(latent_dim=16)
    model = GeometryMMALS(encoder, latent_dim=16, context_dim=2, num_hosts=3, host_hidden_dim=8)
    context_ids = {id(p) for p in model.context_bottleneck_router.parameters()}
    sensory_ids = {id(p) for p in model.sensory_bottleneck_router.parameters()}
    standard_ids = {id(p) for p in model.router.parameters()}
    assert context_ids.isdisjoint(sensory_ids)
    assert context_ids.isdisjoint(standard_ids)
    assert sensory_ids.isdisjoint(standard_ids)
