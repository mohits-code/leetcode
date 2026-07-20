class LRUCache:
    class deque:
        class Node:
            def __init__(self, key, val):
                self.key = key
                self.val = val
                self.next = None
                self.prev = None
        
        def __init__(self):
            self.head = self.Node(0,0)
            self.tail = self.Node(0,0)
            self.head.prev = self.tail
            self.tail.next = self.head
        
        def insert(self, node):
            prev_node = self.head.prev
            prev_node.next = node
            self.head.prev = node
            node.prev = prev_node
            node.next = self.head
        
        def remove(self, node):
            prev_node = node.prev
            next_node = node.next
            prev_node.next = next_node
            next_node.prev = prev_node

    def __init__(self, capacity: int):
        self.cap = capacity
        self.dict = {}
        self.dll = self.deque()

    def get(self, key: int) -> int:
        if key in self.dict:
            node = self.dict[key]
            self.dll.remove(node)
            self.dll.insert(node)
            return node.val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.dict:
            self.dict[key].val = value
            node = self.dict[key]
            self.dll.remove(node)
            self.dll.insert(node)
            return
        
        if self.cap == 0:
            lru_node = self.dll.tail.next
            self.dll.remove(lru_node)
            del self.dict[lru_node.key]
            self.cap += 1

        new_node = self.deque.Node(key, value)
        self.dict[key] = new_node
        self.dll.insert(new_node)
        self.cap -= 1


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)