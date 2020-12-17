import unittest
import pytest
from sleep_collecting_problem import SleepProblem


@pytest.yield_fixture()
def set_up():
    yield


@pytest.yield_fixture(scope="class")
def one_time_set_up():
    pass


unittest.TextTestRunner(verbosity=2).run(unittest.TestLoader().loadTestsFromTestCase(SleepProblem))
