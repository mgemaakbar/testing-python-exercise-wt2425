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
    solver.initialize_domain(w = 10., h = 11., dx = 0.1, dy = 0.2)

    assert solver.nx == 100.
    assert solver.ny == 55.


def test_initialize_physical_parameters():
    """
    Checks function SolveDiffusion2D.initialize_domain
    """
    solver = SolveDiffusion2D()
    solver.w = 10.
    solver.h = 11.
    solver.dx = 0.1
    solver.dy = 0.2
    solver.nx = 100.
    solver.ny = 55.
    solver.initialize_physical_parameters()

    assert solver.dt == 0.0010000000000000002, f"Expecting 0.0010000000000000002, found {solver.dt}"


def test_set_initial_condition():
    """
    Checks function SolveDiffusion2D.get_initial_function
    """
    solver = SolveDiffusion2D()
    solver.w = 10.
    solver.h = 11.
    solver.dx = 0.1
    solver.dy = 0.2
    solver.nx = 100
    solver.ny = 55
    solver.D = 4
    solver.T_cold = 301
    solver.T_hot = 701

    solver.initialize_physical_parameters()
    res = solver.set_initial_condition()
    
    for i in range(100):
        for j in range(55):
            p2 = (i * 0.1 - 5) ** 2 + (j * 0.2 - 5) ** 2
            if p2 < 2**2:
                assert res[i, j] == 701. # value inside the circle
            else:
                assert res[i, j] == 301.