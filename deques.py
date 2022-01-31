class deque:
    def __init__(self):
        self.items = []
    '''
    only methods add_front and remove_front uses O(n), rest O(1)
    '''
    def add_rear(self,item):
        self.items.append(item)
    def add_front(self,item):
        self.items.insert(0,item)

    def remove_rear(self):
        if self.items:
            return self.items.pop()
        else:
            return None
    def remove_front(self):
        if self.items:
            return self.items.pop(0)
        else:
            return None

    def peek_rear(self):
        if self.items:
            return self.items[-1]
        else:
            return None

    def peek_front(self):
        if self.items:
            return self.items[0]
        else:
            return None

    def size(self):
        return len(self.items)

    def isempty(self):
        return self.items == []
  
