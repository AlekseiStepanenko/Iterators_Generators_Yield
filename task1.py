class FlatIterator:

    def __init__(self, list_of_list):
        self.list_of_list = list_of_list

    def __iter__(self):
        self.element = tuple(list_ for list_ in self.list_of_list)
        self.el = -1
        self.elements = []
        self.elements_i = -1
        return self

    def __next__(self):
        self.elements_i += 1
        if self.elements_i >= len(self.elements):
            self.el += 1
            if self.el >= len(self.element):
                raise StopIteration
            el = self.element[self.el]
            self.elements = self.list_of_list[self.el]
            self.elements_i = 0
        return self.elements[self.elements_i]


def test_1():

    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):

        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]


if __name__ == '__main__':
    test_1()