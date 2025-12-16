class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

class SinglyLinkedList:
    head: Node | None
    tail: Node | None
    _size: int
    
    def __init__(self):
        self.head = None
        self.tail = None
        self._size = 0
    
    def __len__(self) -> int:
        return self._size
    
    def _create_first(self, value):
        item = Node(value)
        self.head = item
        self.tail = item
        self._size = 1
    
    def append(self, value):
        if self.tail is None:
            self._create_first(value)
            return
        
        item = Node(value)
        self.tail.next = item
        self.tail = item
        self._size += 1
    
    def prepend(self, value):
        if self.tail is None:
            self._create_first(value)
            return
        
        item = Node(value, self.head)
        self.head = item
        self._size += 1
    
    def insert(self, idx, value):
        if not isinstance(idx, int) or idx < 0 or idx > self._size:
            raise IndexError("Невозможно вставить элемент по индексу: индекс невероятен")
        if idx == 0:
            self.prepend(value)
            return
        if idx == self.__len__():
            self.append(value)
            return
        
        item = self.head
        for _ in range(idx - 1):
            if isinstance(item, Node):
                item = item.next
        if isinstance(item, Node):
            new_item = Node(value, item.next)
            item.next = new_item
        self._size += 1
    
    def remove_at(self, idx):
        if self.head is None or not isinstance(idx, int) or idx < 0 or idx >= self.__len__():
            raise IndexError(f"{self.__len__()}Невозможно удалить элемент по индексу: индекс невероятен")
        if idx == 0:
            self.head = self.head.next
            return
        
        item = self.head
        for _ in range(idx - 1):
            if isinstance(item, Node):
                item = item.next
        if isinstance(item, Node) and isinstance(item.next, Node):
            item.next = item.next.next
        if idx == self.__len__() - 1:
            self.tail = item
        self._size -= 1
    
    def __iter__(self):
        ret = []
        item = self.head
        while isinstance(item, Node):
            ret.append(item)
            item = item.next
        return ret
    
    def __repr__(self) -> str:
        ret = []
        item = self.head
        while isinstance(item, Node):
            ret.append(item.value)
            item = item.next
        return str(ret)

if __name__ == "__main__":
    ll = SinglyLinkedList()
    ll.append(3)
    ll.append(5)
    ll.append(4)
    ll.prepend(1)
    ll.remove_at(2)
    ll.insert(1, 2)
    print(ll.__repr__())
