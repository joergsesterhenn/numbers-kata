class Numbers:
    
    digits = ['zero','one','two','three','four','five','six','seven','eight','nine']
    # units do not contain zero and are led by a space
    units = [''] + [' '+ value for value in digits [1:]]
    # all teens are special !
    teens = ['ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
    # here are the special numbers up to 100
    tens = ['zero', 'ten', 'twenty','thirty', 'fourty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
    orders= ['unit', 'ten', 'hundred', 'thousand','million']
    
    def to_number(self, number):
        if self.is_digit(number):
            return self.digits[number]
        elif self.is_teen(number):
            return self.teens[int(str(number)[1])]
        elif self.is_below_hundred(number):
            first_digit=int(str(number)[0])
            second_digit=int(str(number)[1])
            return self.tens(first_digit) + self.units(second_digit)
        else:
            return 'one hundred'
        
    def is_digit(self, number):
        return number < 10

    def is_teen(self, number):
        return 9 < number < 20

    def is_below_hundred(self, number):
        return number < 100
    
    def units(self,digit):
        return self.units[digit]
    
    def tens(self,digit):
        return self.tens[digit]