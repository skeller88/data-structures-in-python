__author__ = 'Shane'


class QueueWithTwoStacks:
    def __init__(self):
        self.inbox = []
        self.outbox = []

    def enqueue(self, value):
        self.inbox.push(value)

    def dequeue(self):
        if not self.outbox:
            while self.inbox:
                self.outbox.push(self.inbox.pop())

        return self.outbox.pop()
