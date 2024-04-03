class Numbers:
    
    digits = ['zero','one','two','three','four','five','six','seven','eight','nine']
    # all teens are special !
    teens = ['ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
    # here are the special numbers up to 100
    tens = ['', 'ten', 'twenty','thirty', 'fourty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
    orders= ['unit', 'ten', 'hundred', 'thousand','million']
    
    def to_number(self, number):
        if self.is_digit(number):
            return self.digits[number]
        elif self.is_teen(number):
            return self.teens[int(str(number)[1])]
        elif self.is_below_hundred(number):
            first_digit=int(str(number)[0])
            second_digit=int(str(number)[1])
            return self.to_tens(first_digit, True) + self.to_units(second_digit)
        else self.is_below_thousand(number)
            first_digit=int(str(number)[0])
            second_digit=int(str(number)[1])
            third_digit=int(str(number)[2])
            if second_digit==0:
                if third_digit==0:
                    return self.to_hundreds(first_digit) 
                else:
                    return self.to_hundreds(first_digit) + ' and'  + self.to_units(third_digit)
            elif second_digit==1:
                return self.to_hundreds(first_digit) + ' and ' + self.teens[third_digit]
            else:
                return self.to_hundreds(first_digit) + self.to_tens(second_digit, False) + self.to_units(third_digit)
        else: 
            return 'one thousand five hundred and one'
        
    def is_digit(self, number):
        return number < 10

    def is_teen(self, number):
        return 9 < number < 20

    def is_below_hundred(self, number):
        return number < 100

    def is_below_thousand(self, number):
        return number < 1000
    
    # units do not contain zero and are led by a space
    def to_units(self,digit):
        if digit == 0:
            return ''
        else:
            return ' ' + self.digits[digit]
    
    def to_tens(self,digit, leading):
        space = ' and '
        if leading:
            space = ''
        if digit == 0:
            return ''
        else:
            return space + self.tens[digit]
    
    def to_hundreds(self,digit):
        return self.digits[digit] + ' hundred'