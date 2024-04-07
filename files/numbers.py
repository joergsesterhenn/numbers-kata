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
        #split number into segments of three digits and return them in an array from highest order to lowest
        array_of_numbers_by_order = self.disect_number(number)
        order_of_number = (len(str(number))-1)//3
        number_string=''
        # build number_string by traversing orders from highest to lowest and appending the parts
        for order, number_part in enumerate(array_of_numbers_by_order):
            # first get the string for the current segment and append it
            part_of_number_string = self.get_number_by_order(number_part, order)
            number_string += part_of_number_string
            # then determine how to connect it to the next segment
            #if part_of_number_string == '' and not order_of_number == order:
            #    number_string=number_string[:number_string.rfind(',')]
            if order_of_number-order>0 and not part_of_number_string == '':
                number_string = number_string + ' ' + self.orders[order_of_number-order] + ', ' 
        return number_string
    
# 43112603 [43, 112, 603]
# 43112603 0 2 43  fourty three
# 43112603 1 2 112 thousand fourty three thousand, one hundred and twelve
# 43112603 2 2 603 million fourty three thousand, one hundred and twelve million, six hundred and three
    
    
    def get_number_by_order(self, number: int, order: int):    
        number_string=str(number).zfill(3)
        
        hundreds=int(number_string[0])
        tens=int(number_string[1])
        units=int(number_string[2])
        
        number_as_text=''
        #print (str(number),str(number).zfill(3))
        
        # edgecase handled first
        if self.is_digit(number) and order==0:
            return self.digits[number]
        
        if hundreds>0:
            number_as_text = self.digits[hundreds] + ' hundred'
            if tens > 0 or units > 0:
                number_as_text += ' and '
        
        if tens==1:
            return number_as_text + self.teens[units]
        elif tens>1:
            number_as_text += self.tens[tens]
            if units>0:
                number_as_text += ' '
        if units > 0:
            number_as_text +=self.digits[units]

        return number_as_text
        
    def disect_number(self, number: int):
        order_of_number = (len(str(number))-1)//3
        length_of_number=len(str(number))
        #print('number: ',number)
        #print('order: ',order_of_number)
        #print('length: ',length_of_number)
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
