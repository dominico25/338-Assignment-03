import threading
import random
import time

class CircularQueue:
    def __init__(self, size):
        self.size = size
        self.queue = [None for i in range(size)]
        self.head = self.tail = -1
        self._lock = threading.Lock()

    def lock(self):
        self._lock.acquire()

    def unlock(self):
        self._lock.release()

    def enqueue(self, data):
        # Implement enqueue function
        while True:
            self.lock()
            if (self.tail + 1) % self.size == self.head:
                print("Queue is full trying again with:", data)
                self.unlock()
                time.sleep(1)
                q.enqueue(data) # Confusing if "try again" meant rerun the queue with the same data or not
            else:
                if self.head == -1:
                    self.head = 0
                self.tail = (self.tail + 1) % self.size
                self.queue[self.tail] = data
                self.unlock()
                return

    def dequeue(self):
        # Implement dequeue function
        while True:
            self.lock() 
            if self.head == -1:
                self.unlock()
                time.sleep(1)
            else:
                data = self.queue[self.head]
                self.queue[self.head] = None
                if self.head == self.tail:
                    self.head = -1
                    self.tail = -1
                else:
                    self.head = (self.head + 1) % self.size
                self.unlock() 
                return data

def producer():
    while True:
        random_integer = random.randint(1, 2)
        time.sleep(random_integer)
        q.enqueue(random_integer)

def consumer():
    while True:
        random_integer = random.randint(1, 4)
        time.sleep(random_integer)
        data = q.dequeue()
        if (data):
            print("Dequeued: ", data)

if __name__ == '__main__':
    q = CircularQueue(5)
    t1 = threading.Thread(target=producer)
    t2 = threading.Thread(target=consumer)
    t1.start()
    t2.start()
    t1.join()
    t2.join()
