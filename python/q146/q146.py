from collections import deque

class LRUCache:
    def __init__(self, capacity: int):
        self.__queue = deque()
        self.__capacity = capacity
        self.__dict = {}

    def __markUse(self, key):
        self.__queue.remove(key)
        self.__queue.append(key)

    def get(self, key: int) -> int:
        if key in self.__queue:
            self.__markUse(key)
            return self.__dict[key]
        return -1


    def put(self, key: int, value: int) -> None:
        if key in self.__queue:
            self.__dict[key] = value
            self.__markUse(key)
            return
        if len(self.__queue) == self.__capacity:
            key = self.__queue.popleft()
            self.__dict.pop(key)
        self.__queue.append(key)
        self.__dict[key] = value


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)