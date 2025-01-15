"""
Tests for functions in class SolveDiffusion2D
"""

from diffusion2d import SolveDiffusion2D
import numpy as np


def test_initialize_domain():
    """
    Check function SolveDiffusion2D.initialize_domain
    """
    solver = SolveDiffusion2D()
    solver.initialize_domain()

    assert solver.nx == 100.
    assert solver.ny == 100.


def test_initialize_physical_parameters():
    """
    Checks function SolveDiffusion2D.initialize_domain
    """
    solver = SolveDiffusion2D()
    solver.initialize_domain()
    solver.initialize_physical_parameters()

    assert solver.dt == 0.0006250000000000001, f"Expecting 0.0006250000000000001, found {solver.dt}"


def test_set_initial_condition():
    """
    Checks function SolveDiffusion2D.get_initial_function
    """
    solver = SolveDiffusion2D()
    solver.initialize_domain()
    solver.initialize_physical_parameters()
    res = solver.set_initial_condition()
    
    for i in range(100):
        for j in range(100):
            p2 = (i * 0.1 - 5) ** 2 + (j * 0.1 - 5) ** 2
            if p2 < 2**2:
                assert res[i, j] == 700. # value inside the circle
            else:
                assert res[i, j] == 300.