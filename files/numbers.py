class Numbers:
    
    digits = ['zero','one','two','three','four','five','six','seven','eight','nine']
    
    def to_number(self, number):
        if number < 10:
            return self.digits[number]
        else:
            return "ten"
