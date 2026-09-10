import numpy as np

I = np.eye(2, dtype=complex)
X = np.array([[0, 1], [1, 0]], dtype=complex)
P0 = np.array([[1, 0], [0, 0]], dtype=complex)
P1 = np.array([[0, 0], [0, 1]], dtype=complex)

# Fixed refined second-step operator on memory M x system S.
V = np.kron(P0, I) + np.kron(P1, X)

# Coarse history-conditioned second maps.
U = {0: I, 1: X}

ket0 = np.array([[1], [0]], dtype=complex)
ket1 = np.array([[0], [1]], dtype=complex)
W = {0: np.kron(ket0, I), 1: np.kron(ket1, I)}

intertwine = {e: np.linalg.norm(V @ W[e] - W[e] @ U[e]) for e in (0, 1)}

rng = np.random.default_rng(20260909)

def rand_rho():
    A = rng.normal(size=(2, 2)) + 1j * rng.normal(size=(2, 2))
    rho = A @ A.conj().T
    return rho / np.trace(rho)

def ptrace_memory(rho_ms):
    r = rho_ms.reshape(2, 2, 2, 2)
    return np.einsum('msmt->st', r)

max_branch_def = 0.0
for _ in range(100):
    rho = rand_rho()
    for e in (0, 1):
        coarse = U[e] @ rho @ U[e].conj().T
        refined_in = W[e] @ rho @ W[e].conj().T
        refined_out = V @ refined_in @ V.conj().T
        visible = ptrace_memory(refined_out)
        max_branch_def = max(max_branch_def, np.linalg.norm(coarse - visible))

alpha = 0.6 + 0.2j
beta = np.sqrt(1 - abs(alpha) ** 2)
psi = np.array([[1], [1j]], dtype=complex)
psi /= np.linalg.norm(psi)
mem = alpha * ket0 + beta * ket1
in_state = np.kron(mem, psi)
out_ref = V @ in_state
out_expected = alpha * np.kron(ket0, I @ psi) + beta * np.kron(ket1, X @ psi)
coherent_def = np.linalg.norm(out_ref - out_expected)

def random_unitary(n):
    A = rng.normal(size=(n, n)) + 1j * rng.normal(size=(n, n))
    Q, R = np.linalg.qr(A)
    d = np.diag(R)
    ph = np.where(np.abs(d) > 0, d / np.abs(d), 1)
    return Q @ np.diag(ph.conj())

Us = [random_unitary(2) for _ in range(3)]
V3 = np.zeros((6, 6), dtype=complex)
W3 = []
for e, Ue in enumerate(Us):
    Pe = np.zeros((3, 3), dtype=complex)
    Pe[e, e] = 1
    V3 += np.kron(Pe, Ue)
    ke = np.zeros((3, 1), dtype=complex)
    ke[e, 0] = 1
    We = np.kron(ke, I)
    W3.append(We)

max_general = max(np.linalg.norm(V3 @ W3[e] - W3[e] @ Us[e]) for e in range(3))
unitarity_def = np.linalg.norm(V3.conj().T @ V3 - np.eye(6))

print('PAIR_VS_MEMORY_DILATION_VERIFY')
print('intertwine_e0', intertwine[0])
print('intertwine_e1', intertwine[1])
print('max_branch_visible_defect', max_branch_def)
print('coherent_superposition_defect', coherent_def)
print('three_history_general_intertwine_defect', max_general)
print('three_history_fixed_V_unitarity_defect', unitarity_def)
checks = [
    intertwine[0] < 1e-12,
    intertwine[1] < 1e-12,
    max_branch_def < 1e-12,
    coherent_def < 1e-12,
    max_general < 1e-12,
    unitarity_def < 1e-12,
]
print('RESULT', f'{sum(checks)}/{len(checks)} PASS')
