class EvenNumbers:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.i = 0

    def __iter__(self):
        self.i = self.start
        return self

    def __next__(self):
        if self.i > self.end:
            raise StopIteration
        else:
            self.i += 2
            return self.i - 2

en = EvenNumbers(10, 25)
for i in en:
    print(i)