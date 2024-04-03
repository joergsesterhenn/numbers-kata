class Numbers:
    
    digits = ['zero','one','two','three','four','five','six','seven','eight','nine']
    # everytime we hit zero there is a new special number until we get to hundreds so we need the other numbers as separate array
    units = digits[1:]
    # all teens are special !
    teens = ['ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
    # here are the special numbers up to 100
    tens = ['twenty','thirty', 'fourty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
    
    
    def to_number(self, number):
        if is_digit(number):
            return self.digits[number]
        elif number < 20:
            return "ten"
        else:
            return "ninety nine"
        
    def is_digit(self, number):
        return number < 10
