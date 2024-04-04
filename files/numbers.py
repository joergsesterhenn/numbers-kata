class Numbers:
    
    digits = ['zero','one','two','three','four','five','six','seven','eight','nine']
    # all teens are special - who would have thought!
    teens = ['ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
    # all multiples of ten are also special to us
    tens = ['', 'ten', 'twenty','thirty', 'fourty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
    orders= ['', 'thousand', 'million', 'billion', 'trillion']
    
    
    # we need to look at the length of the number before we start calculations
    #
    # length:
    # 1 == units
    # 2 == tens (of units -- we never mention those as they are the default when counting)    
    # 3 == hundreds (of units)
    # ----------
    # 4 == thousands 
    # 5 == tens of thousands 
    # 6 == hundreds of thousands
    # ----------
    # 7 == millions
    # 8 == tens of millions
    # 9 == hundreds of millions ...
    #
    # every new oder can have every lower order as part 
    # zeros need to be handled for every length above 1
    # multiples of ten and teens need to be handled for length 2, 5, 8, 11, ... (2+x*3)
    #
    # we need to count tupples of three digits
    # once those are done we can calculate the next order of magnitude
    # blocks of three digits are divided by a comma - unless nothing follows
    # if we have hundreds of something we append partial hundreds with an ' and '
    
   
    
    def to_number(self, number):
     #   array_of_numbers_by_order = self.disect_number_to_order(number)
        if self.is_digit(number):
            return self.digits[number]
        elif self.is_teen(number):
            return self.teens[int(str(number)[1])]
        elif self.is_below_hundred(number):
            first_digit=int(str(number)[0])
            second_digit=int(str(number)[1])
            return self.to_tens(first_digit, True) + self.to_units(second_digit)
        elif self.is_below_thousand(number):
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
        
    def disect_number(self, number):
        order_of_number = len(str(number))//3
        length_of_number=len(str(number))
        print('number: ',number)
        print('order: ',order_of_number)
        print('length: ',length_of_number)
        #array_of_ordered_numbers=[str(number)[max(3*start,-1*length_of_number):start] for start in (range(-1*(order_of_number+1),-2,-1))]
        array_of_ordered_numbers = []
        for start in reversed((range(-1*(order_of_number+1),0))):
            print(start, -1+(start+1)*3, -1*length_of_number, str(number)[max(3*start,-1*length_of_number):(start+1)*3])
            array_of_ordered_numbers.append(str(number)[max(3*start,-1*length_of_number):(start+1)*3])

            #number:  1501
            #order:  1
            #length:  4
            #-1 -1 -4 50
            #-2 -4 -4 
            #['50', '']
            
        print(array_of_ordered_numbers)
        return array_of_ordered_numbers  
        
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