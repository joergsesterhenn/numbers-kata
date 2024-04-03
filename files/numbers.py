class Numbers:
    
    digits = ['zero','one','two','three','four','five','six','seven','eight','nine']
    # all teens are special !
    teens = ['ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
    # here are the special numbers up to 100
    tens = ['zero', 'ten', 'twenty','thirty', 'fourty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
    
    
    def to_number(self, number):
        if self.is_digit(number):
            return self.digits[number]
        elif self.is_teen(number):
            return self.teens[int(str(number)[1])]
        else:
            return self.tens[int(str(number)[0])] + ' ' + self.digits[int(str(number)[1])]
        
    def is_digit(self, number):
        return number < 10

    def is_teen(self, number):
        return 9 < number < 20
