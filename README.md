# Continuum Beam BVP Solver

> Numerical solver for the boundary value problem (BVP) of a **hyper-flexible manipulator (HFM)** or **continuum beam** — based on the governing equations from nonlinear beam theory.

---

## Overview

This project provides a Python implementation of a **boundary value problem (BVP)** solver for the static configuration of a flexible beam under end loads.

It numerically integrates the governing equation:

\[
\theta''(s) = \frac{F}{EI}\sin(\theta(s) + \psi)
\]

and simultaneously reconstructs the spatial configuration:

\[
x'(s) = \sin\theta(s), \quad y'(s) = \cos\theta(s)
\]

The solution gives the **true deformation shape** of the beam, often used in modeling of **continuum manipulators**, **soft robots**, and **flexural elements**.

---

## Mathematical Model

### Governing Equations

\[
\begin{cases}
x'(s) = \sin \theta(s), \quad x(0) = 0 \\
y'(s) = \cos \theta(s), \quad y(0) = 0 \\
\theta''(s) = \dfrac{F}{EI}\sin(\theta(s) + \psi) \\
\theta'(L) = \dfrac{M(L)}{EI} + \dfrac{1}{r(L)} \\
\theta(0) = 0
\end{cases}
\]

Where:

| Symbol | Meaning |
|:--|:--|
| \( s \) | Arc length coordinate (0 → L) |
| \( \theta(s) \) | Orientation of beam centerline |
| \( F = \sqrt{F_x^2 + F_y^2} \) | Resultant end force |
| \( \psi = \arctan2(F_x, F_y) \) | Force direction |
| \( EI \) | Flexural rigidity |
| \( M(L) \) | Tip moment |
| \( r(L) \) | Tip radius of curvature |

---

## Numerical Method

To use standard solvers, the 2nd-order ODE is converted to a **first-order system**:

\[
\begin{cases}
\theta' = \kappa \\
\kappa' = \dfrac{F}{EI}\sin(\theta - \psi) \\
x' = \sin(\theta) \\
y' = \cos(\theta)
\end{cases}
\]

Boundary conditions:
\[
\begin{cases}
x(0)=0,\ y(0)=0,\ \theta(0)=0 \\
\kappa(L)=M(L)/EI
\end{cases}
\]

We solve this numerically using `scipy.integrate.solve_bvp`, a collocation-based method with adaptive mesh refinement.

---

## File Structure

continuum-bvp/
├── README.md
├── solver/
│ └── hfm_solver.py
├── examples/
│ └── plot_example.py
└── requirements.txt

## Setting up

```bash
pip install numpy scipy matplotlib
```
## Sử dụng
```python
from hfm_solver import solve_hfm
import matplotlib.pyplot as plt

# Tham số
L = 1.0          # chiều dài beam (m)
EI = 1.0         # độ cứng uốn (N⋅m²)
w = [0.5, 0, 0]  # [f_x, f_y, m_t]

# Giải
sol = solve_hfm(L, EI, w, num_points=100)

# Vẽ
plt.plot(sol['x'], sol['y'])
plt.axis('equal')
plt.grid(True)
plt.show()
```

## Author

Giap Nguyen
Department of School of Mechanical Engineering
Hanoi University of Science and Technology
