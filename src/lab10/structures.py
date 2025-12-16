from collections import deque
from typing_extensions import Any

class Stack:
    data: list
    
    def __init__(self):
        self.data = []
    
    def __len__(self) -> int:
        return len(self.data)
    
    def is_empty(self) -> bool:
        return self.__len__() == 0
    
    def push(self, item):
        self.data.append(item)
    
    def pop(self) -> Any:
        if self.is_empty():
            raise IndexError("В стеке нет элементов для удаления")
        return self.data.pop()
    
    def peek(self) -> Any | None:
        if self.is_empty():
            return None
        return self.data[-1]

class Queue:
    data: deque
    
    def __init__(self):
        self.data = deque()
    
    def __len__(self) -> int:
        return len(self.data)
    
    def is_empty(self) -> bool:
        return self.__len__() == 0
    
    def enqueue(self, item):
        self.data.append(item)
    
    def dequeue(self) -> Any:
        if self.is_empty():
            raise IndexError("В стеке нет элементов для удаления")
        return self.data.popleft()
    
    def peek(self) -> Any | None:
        if self.is_empty():
            return None
        return self.data[0]

if __name__ == "__main__":
    st = Stack()
    st.push(3)
    st.push(5)
    print(st.pop())
    print(st.peek())
    st.push(-3)
    print(st.pop())
    
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    print(q.peek())
    q.enqueue(3)
    print(q.dequeue())
