from numbers import Numbers
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
    
    # testplan:
    #
    # test number one
    # test single digit
    # test ten
    # test two digits
    # 99 --> ninety nine
    # test one hundred
    # 300 --> three hundred
    # 310 --> three hundred and ten
    # 1501 --> one thousand, five hundred and one
    # 12609 --> twelve thousand, six hundred and nine
    # 512607 --> five hundred and twelve thousand, six hundred and seven
    # 43112603 --> forty three million, one hundred and twelve thousand, six hundred and three
      
    def test_number_one(self):
        result = str(Numbers().to_number(1))
        verify(result)


if __name__ == "__main__":
    unittest.main()
