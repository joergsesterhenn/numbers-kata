# takes a number and splits it into an array of strings with length three
# in order to always have three digits in a segment we first fill up the number
class NumberSplitter:

    number: int
    ordered_segments: [str]

    def __init__(self, number: int):
        super().__init__()
        self.number = number
        self.ordered_segments = []
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
        self.ordered_segments = \
            [self.number_to_string()[start:start+3]
             for start in (range(0, self.get_length_of_number(), 3))]

    def get_length_of_number(self):
        return len(str(self.number))

    def get_order_of_number(self):
        return (self.get_length_of_number() - 1) // 3

    def number_to_string(self):
        return str(self.number).zfill((self.get_order_of_number()+1) * 3)

    def segments(self):
        """
        :return: ordered tuples of order and segment
        """
        reversed_orders, segments = zip(* enumerate(self.ordered_segments))
        # we need to reverse the order so that it starts with the highest
        return zip(reversed(reversed_orders), self.ordered_segments)
