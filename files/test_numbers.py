from numbers import Numbers
import unittest
from approvaltests.approvals import verify
from approvaltests.reporters.report_on_cyber_dojo import ReportOnCyberDojo
from approvaltests import set_default_reporter




class NumbersTest(unittest.TestCase):
    def setUp(self):
        set_default_reporter(ReportOnCyberDojo())

    # testplan:
    #
    # x test number one
    # x test single digit
    # x test ten
    # x 99 --> ninety nine
    # x test two digits
    # x test one hundred
    # x 300 --> three hundred
    # 310 --> three hundred and ten
    # 1501 --> one thousand, five hundred and one
    # 12609 --> twelve thousand, six hundred and nine
    # 512607 --> five hundred and twelve thousand, six hundred and seven
    # 43112603 --> forty three million, one hundred and twelve thousand, six hundred and three
      
    def test_number_one(self):
        result = str(Numbers().to_number(1))
        verify(result)
    
    def test_single_digits(self):
        result =  [Numbers().to_number(number) for number in range(1,10)]
        verify(result)

    def test_ten(self):
        result = str(Numbers().to_number(10))
        verify(result)
        
    def test_ninety_nine(self):
        result = str(Numbers().to_number(99))
        verify(result)

    def test_every_two_digit_number(self):
        result = [Numbers().to_number(number) for number in range(10,100)]
        verify(result)

    def test_one_hundred(self):
        result = Numbers().to_number(100)
        verify(result)
        
    def test_three_hundred(self):
        result = Numbers().to_number(300)
        verify(result)
        
    def test_three_hundred_ten(self):
        result = Numbers().to_number(310)
        verify(result)
        
if __name__ == "__main__":
    unittest.main()
