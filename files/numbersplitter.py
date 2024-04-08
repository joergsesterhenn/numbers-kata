# takes a number and splits it into an array of strings with length three
# in order to always have three digits in a segment we first fill up the number
class NumberSplitter:

    number: int
    number_string: str
    length_of_number: int
    order_of_number: int
    array_of_ordered_numbers: [str]

    def __init__(self, number: int):
        super().__init__()
        self.number = number
        self.length_of_number = self.get_length_of_number()
        self.order_of_number = self.get_order_of_number()
        self.number_string = self.number_to_string()
        self.array_of_ordered_numbers = []
        self.dissect_number()

    # example 1234567:
    # length_of_number = 7
    # order_of_number  = 2  means 1000^order
    #                         ==>  million is the largest segment
    #    001 234 567
    #                     --first--
    #    ^----------------start =0
    #        ^------------end   =3
    #                     --second--
    #        ^------------start =3
    #            ^--------end   =6
    #                     --third--
    #            ^--------start =6
    #                ^----end   =9
    def dissect_number(self):
        self.array_of_ordered_numbers = \
            [self.number_string[start:start+3]
             for start in (range(0, self.length_of_number, 3))]

    def get_length_of_number(self):
        return len(str(self.number))

    def get_order_of_number(self):
        return (self.length_of_number - 1) // 3

    def number_to_string(self):
        return str(self.number).zfill((self.order_of_number+1) * 3)

    def enumerate(self):
        return enumerate(self.array_of_ordered_numbers)
