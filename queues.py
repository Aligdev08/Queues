from typing import Any, List

class Queue:
    def __init__(self, length: int):
        self.length = length
        self.elements: List[Any] = []

    def __str__(self) -> str:
        return f"Queue({self.elements})"  # prints the list when you print the object

    def _check_is_full(self) -> bool:
        return len(self.elements) >= self.length

    def _check_is_empty(self) -> bool:
        return len(self.elements) == 0

    def enqueue(self, value: Any) -> str:
        if self._check_is_full():
            return "Queue is full."
        self.elements.append(value)
        return f"Enqueued {value}"

    def dequeue(self) -> Any:
        if self._check_is_empty():
            return "Queue is empty."
        return self.elements.pop(0)


class CircularQueue(Queue):
    def __init__(self, length: int):
        super().__init__(length)
        self.elements: List[Any] = [None] * length  # fill elements with NoneType objects
        self.rear_pointer: int = -1
        self.front_pointer: int = -1

    def _check_is_full(self) -> bool:
        return (self.rear_pointer + 1) % self.length == self.front_pointer  # queue is always full if rear_pointer sends you to the front_pointer

    def _check_is_empty(self) -> bool:
        return self.front_pointer == -1

    def enqueue(self, value: Any) -> str:
        if self._check_is_full():
            return "Circular queue is full."
        # Advance rear pointer and insert value at that position
        if self._check_is_empty():
            self.front_pointer = 0  # fix pointer being -1 when it is empty (basically turning the queue babck on)
        self.rear_pointer = (self.rear_pointer + 1) % self.length  # modulus of length means the newly incremented pointers are always between 0 -> 4 (length 5)
        self.elements[self.rear_pointer] = value
        return f"Enqueued {value}"

    def dequeue(self) -> Any:
        if self._check_is_empty():
            return "Circular queue is empty."
        old_value = self.elements[self.front_pointer]
        self.elements[self.front_pointer] = None

        if self.front_pointer == self.rear_pointer:  # set to -1 (which means queue is empty)
            self.front_pointer = -1
            self.rear_pointer = -1
        else:

            self.front_pointer = (self.front_pointer + 1) % self.length  # modulus of length means the newly incremented pointers are always between 0 -> 4 (length 5)
        return old_value
