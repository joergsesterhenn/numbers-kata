from files.numbersplitter import NumberSplitter
from files.segmentwriter import SegmentWriter


class NumbersPrinter:

    # names for multiples of thousand
    # - we are counting  with the short scale
    ORDERS_APPENDIX = ['', ' thousand', ' million', ' billion', ' trillion',
                       ' quadrillion', ' quintillion', ' sextillion',
                       ' septillion', ' octillion', ' nonillion']

    SEPERATOR_OF_ORDERS = ', '

    number_splitter: NumberSplitter
    number: int

    def __init__(self, number: int):
        self.number = number
        self.number_splitter = NumberSplitter(number)

    def print(self):

        # edge case handled first
        if self.number == 0:
            return 'zero'

        number_string = ''

        # build number_string by traversing orders
        # from highest to lowest and appending the parts
        for inverse_order, segment in self.number_splitter.enumerate():

            # split number into segments of three digits
            # and return them in an array from the highest order to lowest
            segment_string = SegmentWriter(segment).to_text()

            # if this part is not empty 
            if segment_string:
                # if we are not the highest order lead with a comma
                if inverse_order > 0:
                    number_string += self.SEPERATOR_OF_ORDERS

                number_string += segment_string

                # attach the order
                order = (self.number_splitter.get_order_of_number()
                         - inverse_order)
                number_string += self.ORDERS_APPENDIX[order]

        return number_string
