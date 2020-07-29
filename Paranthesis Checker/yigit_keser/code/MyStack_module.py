class MyStack:
    """ Stack implementation using lists """

    def __init__(self):
        """ create an empty stack """
        self._data = []

    def get_size(self):
        if len(self._data) > 0:
            return len(self._data)
        else:
            return False

    def is_empty(self):
        if self.get_size() == 0:
            return True
        else:
            return False

    def push(self, e):
        self._data.append(e)

    def top(self):
        if self.is_empty():
            return False
        else:
            return self._data[-1]

    def pop(self):
        self._data.pop(-1)

    def print_stack(self):
        if self.is_empty() is True:
            return print('Current stack is empty')
        else:
            return print('Stack Contents: {}'.format(self._data))
        