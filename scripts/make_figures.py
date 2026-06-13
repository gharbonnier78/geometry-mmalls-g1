from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt

OUT = Path(__file__).resolve().parents[1] / 'paper' / 'figures'
OUT.mkdir(parents=True, exist_ok=True)

# Figure 1: conceptual latent manifold
angles = np.linspace(-60, 60, 13)
t = np.deg2rad(angles)
x = 1.2*np.sin(t)
y = 0.7*np.sin(2*t) + 0.15*np.cos(3*t)
plt.figure(figsize=(6.2, 4.2))
plt.plot(x, y, marker='o')
for a, xx, yy in zip(angles[::2], x[::2], y[::2]):
    plt.annotate(f'{int(a)}°', (xx, yy), xytext=(4,4), textcoords='offset points', fontsize=8)
plt.xlabel('Latent coordinate 1')
plt.ylabel('Latent coordinate 2')
plt.title('Synthetic illustration: an ordered context manifold')
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig(OUT / 'conceptual_manifold.pdf', bbox_inches='tight')
plt.savefig(OUT / 'conceptual_manifold.png', dpi=220, bbox_inches='tight')
plt.close()

# Figure 2: conceptual route trajectory
angles2 = np.linspace(-60, 60, 121)
w1 = np.exp(-0.5*((angles2+35)/22)**2)
w2 = np.exp(-0.5*((angles2)/22)**2)
w3 = np.exp(-0.5*((angles2-35)/22)**2)
W = np.vstack([w1,w2,w3])
W /= W.sum(axis=0, keepdims=True)
plt.figure(figsize=(6.4, 4.2))
plt.plot(angles2, W[0], label='Host H1')
plt.plot(angles2, W[1], label='Host H2')
plt.plot(angles2, W[2], label='Host H3')
plt.xlabel('Grounded context factor: rotation angle (degrees)')
plt.ylabel('Routing mass')
plt.ylim(0,1.02)
plt.title('Synthetic illustration: continuous route transport')
plt.legend(frameon=False)
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig(OUT / 'route_trajectory.pdf', bbox_inches='tight')
plt.savefig(OUT / 'route_trajectory.png', dpi=220, bbox_inches='tight')
plt.close()

# Figure 3: conceptual drift curves
steps = np.arange(1, 7)
baseline = np.array([0.00,0.13,0.22,0.31,0.39,0.47])
geom = np.array([0.00,0.07,0.11,0.15,0.18,0.21])
plt.figure(figsize=(6.2, 4.2))
plt.plot(steps, baseline, marker='o', label='Unconstrained router')
plt.plot(steps, geom, marker='o', label='Geometry-regularized router')
plt.xlabel('Continual-learning stage')
plt.ylabel('Normalized route-function drift')
plt.title('Synthetic illustration: controlled functional transport')
plt.legend(frameon=False)
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig(OUT / 'transport_drift.pdf', bbox_inches='tight')
plt.savefig(OUT / 'transport_drift.png', dpi=220, bbox_inches='tight')
plt.close()
