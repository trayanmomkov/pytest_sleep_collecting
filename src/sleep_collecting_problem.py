import pytest
import unittest
from src.helper import execute_test


@pytest.mark.usefixtures("one_time_set_up", "set_up")
class SleepProblem(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self):
        pass

    @pytest.mark.run(order=1)
    def test_1(self):
        execute_test('Test 1')

    @pytest.mark.run(order=2)
    def test_2(self):
        execute_test('Test 2')

    @pytest.mark.run(order=3)
    def test_3(self):
        execute_test('Test 3')

    @pytest.mark.run(order=4)
    def test_4(self):
        execute_test('Test 4')