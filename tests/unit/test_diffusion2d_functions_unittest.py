import unittest
from diffusion2d import SolveDiffusion2D

class TestDiffusion2D(unittest.TestCase):
    def setUp(self):
        self.solver = SolveDiffusion2D()

    def test_initialize_domain(self):
        """
        Check function SolveDiffusion2D.initialize_domain
        """
        self.solver.initialize_domain(w = 10., h = 11., dx = 0.1, dy = 0.2)


        self.assertEqual(self.solver.nx, 100)
        self.assertEqual(self.solver.ny, 55)

    def test_initialize_physical_parameters(self):
        """
        Checks function SolveDiffusion2D.initialize_domain
        """
        self.solver.w = 10.
        self.solver.h = 11.
        self.solver.dx = 0.1
        self.solver.dy = 0.2
        self.solver.nx = 100.
        self.solver.ny = 55.
        self.solver.initialize_physical_parameters()

        self.assertEqual(self.solver.dt, 0.0010000000000000002)


    def test_set_initial_condition(self):
        """
        Checks function SolveDiffusion2D.get_initial_function
        """
        self.solver.w = 10.
        self.solver.h = 11.
        self.solver.dx = 0.1
        self.solver.dy = 0.2
        self.solver.nx = 100
        self.solver.ny = 55
        self.solver.D = 4
        self.solver.T_cold = 301
        self.solver.T_hot = 701
        res = self.solver.set_initial_condition()
        
        for i in range(100):
            for j in range(55):
                p2 = (i * 0.1 - 5) ** 2 + (j * 0.2 - 5) ** 2
                if p2 < 2**2:
                    self.assertEqual(res[i, j], 701) # value inside the circle
                else:
                    self.assertEqual(res[i, j], 301)