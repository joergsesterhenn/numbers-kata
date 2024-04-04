class Numbers:
    
    digits = ['zero','one','two','three','four','five','six','seven','eight','nine']
    # all teens are special - who would have thought!
    teens = ['ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
    # all multiples of ten are also special to us
    tens = ['', 'ten', 'twenty','thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
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
        
    def to_number(self, number: int):
        array_of_numbers_by_order = self.disect_number(number)
        order_of_number = (len(str(number))-1)//3
        number_string=''
        for order, number_part in enumerate(array_of_numbers_by_order):
            number_string = number_string + (self.get_number_by_order(number_part, order))
            if order_of_number-order>0:
                number_string = number_string + ' ' + self.orders[order_of_number-order] + ', ' 
        return number_string
    
# 43112603 [43, 112, 603]
# 43112603 0 2 43  fourty three
# 43112603 1 2 112 thousand fourty three thousand, one hundred and twelve
# 43112603 2 2 603 million fourty three thousand, one hundred and twelve million, six hundred and three
    
    
    def get_number_by_order(self, number: int, order: int):    
        number_as_string=str(number).zfill(3)
        first_digit=int(number_as_string[0])
        second_digit=int(number_as_string[1])
        third_digit=int(number_as_string[2])
        
        if self.is_digit(number) and order==0:
            return self.digits[number]
        elif self.is_teen(number):
            return self.teens[int(str(number)[1])]
        elif self.is_below_hundred(number):
            return self.to_tens(first_digit, True) + self.to_units(second_digit)
        elif self.is_below_thousand(number):
            if second_digit==0:
                if third_digit==0:
                    return self.to_hundreds(first_digit) 
                else:
                    return self.to_hundreds(first_digit) + ' and'  + self.to_units(third_digit)
            elif second_digit==1:
                return self.to_hundreds(first_digit) + ' and ' + self.teens[third_digit]
            else:
                return self.to_hundreds(first_digit) + self.to_tens(second_digit, False) + self.to_units(third_digit)
        
    def disect_number(self, number: int):
        order_of_number = (len(str(number))-1)//3
        length_of_number=len(str(number))
        #print('number: ',number)
        #print('order: ',order_of_number)
        #print('length: ',length_of_number)
        array_of_ordered_numbers=[str(number)[max(3*start,-1*length_of_number):start] for start in (range(-1*(order_of_number+1),-2,-1))]
        array_of_ordered_numbers = []
        for order in reversed((range(-1*(order_of_number+1),0))):
            start=max(3*order,-1*length_of_number)
            end=(order+1)*3
            #print(start,end,str(number)[start:end])
            if end==0:
                array_of_ordered_numbers.append(int(str(number)[start:]))
            else:
                array_of_ordered_numbers.append(int(str(number)[start:end]))
        return list(reversed(array_of_ordered_numbers))  
        
    def is_digit(self, number: int):
        return number < 10

    def is_teen(self, number: int):
        return 9 < number < 20

    def is_below_hundred(self, number: int):
        return number < 100

    def is_below_thousand(self, number: int):
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