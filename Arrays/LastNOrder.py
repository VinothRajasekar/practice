class Log(object):
    def __init__(self, n):
        self._log = []
        self.n = n

    def record(self, order_id):
        if len(self._log) >= self.n:
            self._log.pop(0)
        self._log.append(order_id)

    def get_last(self, i):
        return self._log[-i]



a = Log(3)
a.record(1)
a.record(2)
a.record(3)
print(a.get_last(1))
a.record(4)
print(a.get_last(1))
