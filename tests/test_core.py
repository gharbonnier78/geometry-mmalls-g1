import torch

from geometry_mmalls.model import GeometryMMALS, SmallConvEncoder


def test_model_trace_shapes():
    encoder = SmallConvEncoder(latent_dim=16)
    model = GeometryMMALS(encoder, latent_dim=16, context_dim=2, num_hosts=3, host_hidden_dim=8)
    x = torch.randn(5, 1, 28, 28)
    trace = model(x)
    assert trace.z0.shape == (5, 16)
    assert trace.context.shape == (5, 2)
    assert trace.route.shape == (5, 3)
    assert trace.host_outputs.shape == (5, 3, 16)
    assert trace.z_mm.shape == (5, 16)
    assert trace.logits.shape == (5, 10)
    assert torch.allclose(trace.route.sum(dim=1), torch.ones(5), atol=1e-6)
