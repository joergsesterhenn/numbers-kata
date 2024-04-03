from numbers import global_answer, Numbers
import unittest
from approvaltests.approvals import verify
from approvaltests.reporters.report_on_cyber_dojo import ReportOnCyberDojo
from approvaltests import set_default_reporter


class NumbersTest(unittest.TestCase):
    def setUp(self):
        set_default_reporter(ReportOnCyberDojo())

    # if you want to change the expected result, 
    # move HikerTest.test_global.recieved.txt
    # to   HikerTest.test_global.approved.txt
    # to view the differences, 
    # open HikerTest.test_global.diff

    def test_global(self):
        result = str(global_answer())
        verify(result)

    def test_instance(self):
        result = str(Numbers().instance_answer())
        verify(result)


if __name__ == "__main__":
    unittest.main()
