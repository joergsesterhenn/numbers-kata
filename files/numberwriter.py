from files.numbersplitter import NumberSplitter
from files.segmentwriter import SegmentWriter


class NumberWriter:

    # names for multiples of thousand - we are counting with the short scale
    ORDERS_APPENDIX = ['', ' thousand', ' million', ' billion', ' trillion',
                       ' quadrillion', ' quintillion', ' sextillion',
                       ' septillion', ' octillion', ' nonillion']

    SEPERATOR_OF_ORDERS = ', '

    number: int
    number_splitter: NumberSplitter

    def __init__(self, number: int):
        self.number = number
        self.number_splitter = NumberSplitter(number)

    def to_text(self):
        """
        :return: the number as text
        """

        # edge case handled first
        if self.number == 0:
            return 'zero'

        number_as_text = ''

        # build number_as_text by traversing and appending segments
        # from highest to lowest orders
        for inverse_order, segment in self.number_splitter.enumerate():

            # split number into segments of three digits
            # and return them in an array from the highest order to lowest
            segment_as_text = SegmentWriter(segment).to_text()

            # if this part is not empty 
            if segment_as_text:
                # if we are not the highest order lead with a comma
                if inverse_order > 0:
                    number_as_text += self.SEPERATOR_OF_ORDERS

                number_as_text += segment_as_text

                # attach the order
                order = (self.number_splitter.get_order_of_number()
                         - inverse_order)
                number_as_text += self.ORDERS_APPENDIX[order]

        return number_as_text
