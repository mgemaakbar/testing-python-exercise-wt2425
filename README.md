# Python code to solve the diffusion equation in 2D

Please follow the instructions in [python_testing_exercise.md](https://github.com/Simulation-Software-Engineering/Lecture-Material/blob/main/05_testing_and_ci/python_testing_exercise.md).

## Test logs (for submission)

### pytest log

============================= test session starts ==============================
platform linux -- Python 3.12.3, pytest-7.4.4, pluggy-1.4.0
rootdir: /home/akbar/Documents/SSE/testing-python-exercise-wt2425
collected 1 item

tests/unit/test_diffusion2d_functions.py F                               [100%]

=================================== FAILURES ===================================
____________________________ test_initialize_domain ____________________________

    def test_initialize_domain():
        """
        Check function SolveDiffusion2D.initialize_domain
        """
        solver = SolveDiffusion2D()
        solver.initialize_domain(w = 10., h = 11., dx = 0.1, dy = 0.2)
    
>       assert solver.nx == 100.
E       assert 110 == 100.0
E        +  where 110 = <diffusion2d.SolveDiffusion2D object at 0x748a79ff1160>.nx

tests/unit/test_diffusion2d_functions.py:16: AssertionError
=========================== short test summary info ============================
FAILED tests/unit/test_diffusion2d_functions.py::test_initialize_domain - ass...
============================== 1 failed in 0.45s ===============================
Finished running tests!

============================= test session starts ==============================
platform linux -- Python 3.12.3, pytest-7.4.4, pluggy-1.4.0
rootdir: /home/akbar/Documents/SSE/testing-python-exercise-wt2425
collected 1 item

tests/unit/test_diffusion2d_functions.py F                               [100%]

=================================== FAILURES ===================================
_____________________ test_initialize_physical_parameters ______________________

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
    
>       assert solver.dt == 0.0010000000000000002, f"Expecting 0.0010000000000000002, found {solver.dt}"
E       AssertionError: Expecting 0.0010000000000000002, found 0.0006666666666666669
E       assert 0.0006666666666666669 == 0.0010000000000000002
E        +  where 0.0006666666666666669 = <diffusion2d.SolveDiffusion2D object at 0x73ede2063ef0>.dt

tests/unit/test_diffusion2d_functions.py:33: AssertionError
----------------------------- Captured stdout call -----------------------------
dt = 0.0006666666666666669
=========================== short test summary info ============================
FAILED tests/unit/test_diffusion2d_functions.py::test_initialize_physical_parameters
============================== 1 failed in 0.44s ===============================
Finished running tests!

### unittest log

============================= test session starts ==============================
platform linux -- Python 3.12.3, pytest-7.4.4, pluggy-1.4.0
rootdir: /home/akbar/Documents/SSE/testing-python-exercise-wt2425
collected 1 item

tests/unit/test_diffusion2d_functions_unittest.py F                      [100%]

=================================== FAILURES ===================================
____________________ TestDiffusion2D.test_initialize_domain ____________________

self = <test_diffusion2d_functions_unittest.TestDiffusion2D testMethod=test_initialize_domain>

    def test_initialize_domain(self):
        """
        Check function SolveDiffusion2D.initialize_domain
        """
        solver = SolveDiffusion2D()
        solver.initialize_domain(w = 10., h = 11., dx = 0.1, dy = 0.2)
    
    
>       self.assertEqual(solver.nx, 100)
E       AssertionError: 110 != 100

tests/unit/test_diffusion2d_functions_unittest.py:13: AssertionError
=========================== short test summary info ============================
FAILED tests/unit/test_diffusion2d_functions_unittest.py::TestDiffusion2D::test_initialize_domain
============================== 1 failed in 0.41s ===============================
Finished running tests!


============================= test session starts ==============================
platform linux -- Python 3.12.3, pytest-7.4.4, pluggy-1.4.0
rootdir: /home/akbar/Documents/SSE/testing-python-exercise-wt2425
collected 1 item

tests/unit/test_diffusion2d_functions_unittest.py F                      [100%]

=================================== FAILURES ===================================
_____________ TestDiffusion2D.test_initialize_physical_parameters ______________

self = <test_diffusion2d_functions_unittest.TestDiffusion2D testMethod=test_initialize_physical_parameters>

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
    
>       self.assertEqual(self.solver.dt, 0.0010000000000000002)
E       AssertionError: 0.0006666666666666669 != 0.0010000000000000002

tests/unit/test_diffusion2d_functions_unittest.py:30: AssertionError
----------------------------- Captured stdout call -----------------------------
dt = 0.0006666666666666669
=========================== short test summary info ============================
FAILED tests/unit/test_diffusion2d_functions_unittest.py::TestDiffusion2D::test_initialize_physical_parameters
============================== 1 failed in 0.43s ===============================
Finished running tests!

============================= test session starts ==============================
platform linux -- Python 3.12.3, pytest-7.4.4, pluggy-1.4.0
rootdir: /home/akbar/Documents/SSE/testing-python-exercise-wt2425
collected 1 item

tests/unit/test_diffusion2d_functions_unittest.py F                      [100%]

=================================== FAILURES ===================================
__________________ TestDiffusion2D.test_set_initial_condition __________________

self = <test_diffusion2d_functions_unittest.TestDiffusion2D testMethod=test_set_initial_condition>

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
>                   self.assertEqual(res[i, j], 301)
E                   AssertionError: 701.0 != 301

tests/unit/test_diffusion2d_functions_unittest.py:54: AssertionError
=========================== short test summary info ============================
FAILED tests/unit/test_diffusion2d_functions_unittest.py::TestDiffusion2D::test_set_initial_condition
============================== 1 failed in 0.42s ===============================
Finished running tests!

## Citing

The code used in this exercise is based on [Chapter 7 of the book "Learning Scientific Programming with Python"](https://scipython.com/book/chapter-7-matplotlib/examples/the-two-dimensional-diffusion-equation/).
