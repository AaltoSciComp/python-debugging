
class IndexedList():
    def __init__(self, l):
        self.l = l

    def __getitem__(self, i):
        ''' Map letters to integers and use them to index the list '''
        if not isinstance(i, str):
            i = str(i)
        index = ord(i)
        return self.l[index]