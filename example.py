from hfm_solver import solve_hfm
import matplotlib.pyplot as plt
import numpy as np

# Thông số
L = 1.0
EI = 1.0

# So sánh các trường hợp tải
loads = [
    [0.5, 0, 0],    # lực ngang
    [0, 0.5, 0],    # lực dọc
    [0, 0, 0.2],    # moment
]

plt.figure(figsize=(10, 6))
for i, w in enumerate(loads):
    sol = solve_hfm(L, EI, w)
    if sol:
        plt.plot(sol['x'], sol['y'], label=f'Load {i+1}')

plt.xlabel('x (m)')
plt.ylabel('y (m)')
plt.legend()
plt.axis('equal')
plt.grid(True)
plt.title('Beam Deformation under Different Loads')
plt.show()