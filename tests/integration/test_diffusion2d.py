"""
Tests for functionality checks in class SolveDiffusion2D
"""

from diffusion2d import SolveDiffusion2D


def test_initialize_physical_parameters():
    """
    Checks function SolveDiffusion2D.initialize_domain
    """
    solver = SolveDiffusion2D()
    solver.initialize_domain(w = 10., h = 11., dx = 0.1, dy = 0.2)
    solver.initialize_physical_parameters()
    assert solver.dt == 0.0010000000000000002

def test_set_initial_condition():
    """
    Checks function SolveDiffusion2D.get_initial_function
    """
    solver = SolveDiffusion2D( )
    solver.initialize_domain(w = 10., h = 11., dx = 0.1, dy = 0.2)
    solver.initialize_physical_parameters(T_cold = 301., T_hot = 701.)
    res = solver.set_initial_condition()

    for i in range(100):
        for j in range(55):
            p2 = (i * 0.1 - 5) ** 2 + (j * 0.2 - 5) ** 2
            if p2 < 2**2:
                assert res[i, j] == 701. # value inside the circle
            else:
                assert res[i, j] == 301.
