from files.numbersplitter import NumberSplitter


class NumbersPrinter:
    DIGITS = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven',
              'eight', 'nine']
    # all teens are special - who would have thought!
    TEENS = ['ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen',
             'sixteen', 'seventeen', 'eighteen', 'nineteen']
    # all multiples of ten are also special to us
    TENS = ['', 'ten', 'twenty', 'thirty', 'forty', 'fifty', 'sixty',
            'seventy', 'eighty', 'ninety']
    # so are all multiples of thousand apparently
    # - we are counting  with the short scale
    ORDERS = ['', 'thousand', 'million', 'billion', 'trillion', 'quadrillion',
              'quintillion', 'sextillion', 'septillion', 'octillion',
              'nonillion']

    SEPERATOR_OF_ORDERS = ', '

    number_splitter: NumberSplitter
    number: int

    def __init__(self, number: int):
        self.number = number
        self.number_splitter = NumberSplitter(number)

    # we need to look at the length of the number before we start calculations
    #
    # length:
    # 1 == units
    # 2 == tens (of units -- we do not mention those. they are the default)
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
    # zero needs to be handled separately
    # multiples of ten and teens need to be handled for length 2, 5, 8, (2+x*3)
    #
    # we need to count segments of three digits
    # once those are done we can calculate the next order of magnitude
    # blocks of three digits are divided by a comma - unless nothing follows
    # if we have hundreds we append partial hundreds with an ' and '

    def print(self):

        # edge case handled first
        if self.number == 0:
            return 'zero'

        # split number into segments of three digits
        # and return them in an array from the highest order to lowest
        number_string = ''

        # build number_string by traversing orders
        # from highest to lowest and appending the parts
        for inverse_order, number_part in self.number_splitter.enumerate():

            # first get the string for the current segment and append it
            part_of_number_string = self.get_number_part(number_part)

            # if this part is not empty 
            if part_of_number_string:
                # if we are not the highest order lead with a comma
                if inverse_order > 0:
                    number_string += self.SEPERATOR_OF_ORDERS

                number_string += part_of_number_string

                # attach the order for everything but the lowest order
                order = (self.number_splitter.get_order_of_number()
                         - inverse_order)
                if order > 0:
                    number_string += ' ' + self.ORDERS[order]

        return number_string

    def get_number_part(self, number_string: str):

        hundreds = int(number_string[0])
        tens = int(number_string[1])
        units = int(number_string[2])

        number_as_text = ''

        if hundreds > 0:
            number_as_text = self.DIGITS[hundreds] + ' hundred'
            if tens > 0 or units > 0:
                number_as_text += ' and '
        if tens == 1:
            return number_as_text + self.TEENS[units]
        elif tens > 1:
            number_as_text += self.TENS[tens]
            if units > 0:
                number_as_text += ' '
        if units > 0:
            number_as_text += self.DIGITS[units]

        return number_as_text
