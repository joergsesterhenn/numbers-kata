from numbersprinter import NumbersPrinter
from numbersplitter import NumberSplitter
import unittest
from approvaltests.approvals import verify
from approvaltests.reporters.report_on_cyber_dojo import ReportOnCyberDojo
from approvaltests import set_default_reporter


class NumbersTest(unittest.TestCase):
    def setUp(self):
        set_default_reporter(ReportOnCyberDojo())

    # testplan:
    #
    # x 1 --> one
    # x test single digit
    # x 10 --> ten
    # x 99 --> ninety nine
    # x test two digits
    # x 100 --> one hundred
    # x 300 --> three hundred
    # x 310 --> three hundred and ten
    # x test three digits
    # x 1501 --> one thousand, five hundred and one
    # x 12609 --> twelve thousand, six hundred and nine
    # x 512607 --> five hundred and twelve thousand, six hundred and seven
    # x 43112603 --> forty three million, one hundred and twelve thousand, six hundred and three

    def test_number_zero(self):
        result = str(NumbersPrinter(0).print())
        verify(result)

    def test_number_one(self):
        result = str(NumbersPrinter(1).print())
        verify(result)
    
    def test_single_digits(self):
        result = [NumbersPrinter(number).print() for number in range(1, 10)]
        verify(result)
 
    def test_ten(self):
        result = str(NumbersPrinter(10).print())
        verify(result)
        
    def test_ninety_nine(self):
        result = str(NumbersPrinter(99).print())
        verify(result)

    def test_every_two_digit_number(self):
        result = "\n".join([NumbersPrinter(number).print() for number in range(10, 100)])
        verify(result)
 
    def test_one_hundred(self):
        result = NumbersPrinter(100).print()
        verify(result)
        
    def test_three_hundred(self):
        result = NumbersPrinter(300).print()
        verify(result)
        
    def test_three_hundred_ten(self):
        result = NumbersPrinter(310).print()
        verify(result)
        
    def test_every_three_digit_number(self):
        result = "\n".join([NumbersPrinter(number).print() for number in range(100, 1000)])
        verify(result)
        
    def test_one_thousand_five_hundred_and_one(self):
        result = NumbersPrinter(1501).print()
        verify(result)
        
    def test_dissecting_to_order(self):
        splitter = NumberSplitter(1501)
        result = splitter.array_of_ordered_numbers
        verify(result)
        
    def test_twelve_thousand_six_hundred_and_nine(self):
        result = NumbersPrinter(12609).print()
        verify(result)
    
    def test_five_hundred_and_twelve_thousand_six_hundred_and_seven(self):
        result = NumbersPrinter(512607).print()
        verify(result)
    
    def test_forty_three_million(self):
        result = NumbersPrinter(43112603).print()
        verify(result)
        
    def test_one_million(self):
        result = NumbersPrinter(1000000).print()
        verify(result)
        
    def test_sample_in_millions(self):
        result = "\n".join([NumbersPrinter(number).print() for number in range(1000000, 100000000, 215431)])
        verify(result)
       
    def test_a_really_long_one(self):
        result = NumbersPrinter(1050907000407750600030640022401).print()
        verify(result)


if __name__ == "__main__":
    unittest.main()
