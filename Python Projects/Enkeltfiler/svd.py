import numpy as np
import matplotlib.pyplot as plt

# Steg 1: Opprette matrisen
np.random.seed(0)  # For reproduserbarhet
A = 2 * np.random.rand(100, 100) - 1  # Tilfeldige tall mellom -1 og 1
A[50, 50] = 10  # Setter et element til 10

# Steg 2: Utføre SVD
U, S, Vt = np.linalg.svd(A)

# Steg 3: Beregne A - u1*s1*v1^T og A - (u1*s1*v1^T + u2*s2*v2^T)
reconstruction_1 = U[:, 0].reshape(-1, 1) * S[0] * Vt[0, :]
reconstruction_2 = U[:, :2] @ np.diag(S[:2]) @ Vt[:2, :]

A_minus_1 = A - reconstruction_1
A_minus_2 = A - reconstruction_2

# Visualisering
fig, axes = plt.subplots(1, 3, figsize=(18, 6))
axes[0].imshow(A, cmap='gray', vmin=-1, vmax=1)
axes[0].set_title('Original A')
axes[1].imshow(A_minus_1, cmap='gray', vmin=-1, vmax=1)
axes[1].set_title('A - u1*s1*v1^T')
axes[2].imshow(A_minus_2, cmap='gray', vmin=-1, vmax=1)
axes[2].set_title('A - (u1*s1*v1^T + u2*s2*v2^T)')
for ax in axes:
    ax.axis('off')
plt.show()