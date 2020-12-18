import pytest
import unittest
import time


@pytest.mark.usefixtures("one_time_set_up", "set_up")
class SleepProblem(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self):
        pass

    @pytest.mark.run(order=1)
    def test_1(self):
        time.sleep(1)

    @pytest.mark.run(order=2)
    def test_2(self):
        time.sleep(1)

    @pytest.mark.run(order=3)
    def test_3(self):
        time.sleep(1)

    @pytest.mark.run(order=4)
    def test_4(self):
        time.sleep(1)