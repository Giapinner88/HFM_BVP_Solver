"""
Hyper-Flexible Manipulator BVP Solver
"""

import numpy as np
from scipy.integrate import solve_bvp


def solve_hfm(L, EI, w, num_points=50):
    """
    Solve hyper-flexible manipulator boundary value problem.
    
    Parameters
    ----------
    L : float
        Beam length (m)
    EI : float
        Bending stiffness (N⋅m²)
    w : list or array
        Load at tip [f_x, f_y, m_t]
    num_points : int
        Number of discretization points
    
    Returns
    -------
    dict or None
        {'s': array, 'x': array, 'y': array, 'theta': array}
    """
    
    f_x, f_y, m_t = w
    f = np.sqrt(f_x**2 + f_y**2)
    psi = np.arctan2(f_x, f_y) if f != 0 else 0
    
    def ode(s, y):
        theta, kappa, x_pos, y_pos = y
        dtheta = kappa
        dkappa = (f / EI) * np.sin(theta - psi)
        dx = np.sin(theta)
        dy = np.cos(theta)
        return [dtheta, dkappa, dx, dy]
    
    def bc(ya, yb):
        return [ya[2], ya[3], ya[0], yb[1] - m_t / EI]
    
    s = np.linspace(0, L, num_points)
    y_guess = np.zeros((4, num_points))
    
    if f > 0:
        y_guess[0] = psi * s / L
        y_guess[1] = (m_t / EI) * np.ones_like(s)
        y_guess[2] = s * np.sin(psi)
        y_guess[3] = s * np.cos(psi)
    else:
        y_guess[3] = s
    
    sol = solve_bvp(ode, bc, s, y_guess, tol=1e-6, max_nodes=10000)
    
    if sol.success:
        return {
            's': sol.x,
            'x': sol.y[2],
            'y': sol.y[3],
            'theta': sol.y[0]
        }
    else:
        print(f"BVP solver failed for w={w}")
        return None