from typing import Any, List

class QueueOverflowError(Exception):
    pass

class QueueUnderflowError(Exception):
    pass

class Queue:
    def __init__(self, length: int):
        self.length = length
        self.elements: List[Any] = []

    def __str__(self) -> str:
        return f"Queue({self.elements})"  # returns the queue represented as a string when you call the object

    def isFull(self) -> bool:
        return len(self.elements) >= self.length

    def isEmpty(self) -> bool:
        return len(self.elements) == 0

    def enqueue(self, value: Any) -> str:
        if self.isFull():
            raise QueueOverflowError("Queue is full. Cannot enqueue more elements.")
        self.elements.append(value)
        return f"Enqueued {value}"

    def dequeue(self) -> Any:
        if self.isEmpty():
            raise QueueUnderflowError("Queue is empty. Cannot dequeue more elements.")
        return self.elements.pop(0)


class CircularQueue(Queue):
    def __init__(self, length: int):
        super().__init__(length)
        self.elements: List[Any] = [None] * length  # fill elements with NoneType objects
        self.rear_pointer: int = -1
        self.front_pointer: int = -1

    def __str__(self) -> str:
        formatted_elements = self.elements
        for index, element in enumerate(formatted_elements):
            if element:
                if index == self.rear_pointer:
                    element = formatted_elements[index] = f"({element})"  # value in rear of queue
                if index == self.front_pointer:
                    element = formatted_elements[index] = f"[{element}]"  # value in front of queue
            else:
                formatted_elements[index] = "_"
        return " | ".join(formatted_elements)

    def isFull(self) -> bool:
        return (self.rear_pointer+1) % self.length == self.front_pointer  # queue is always full if rear_pointer sends you to the front_pointer

    def isEmpty(self) -> bool:
        return self.front_pointer == -1

    def enqueue(self, value: Any) -> str:
        if self.isFull():
            raise QueueOverflowError("Circular queue is full. Cannot enqueue more elements.")
        if self.isEmpty():
            self.front_pointer += 1  # undo pointer being -1 when it is empty (basically turning the queue babck on)
        self.rear_pointer = (self.rear_pointer+1) % self.length  # modulus of length means the newly incremented pointers are always between 0 -> 4 (length 5)
        self.elements[self.rear_pointer] = value

    def dequeue(self) -> Any:
        if self.isEmpty():
            raise QueueUnderflowError("Circular queue is empty. Cannot dequeue more elements.")
        old_value = self.elements[self.front_pointer]
        self.elements[self.front_pointer] = None

        if self.front_pointer == self.rear_pointer:  # set to -1 (which means queue is empty)
            self.front_pointer = -1
            self.rear_pointer = -1
        else:
            self.front_pointer = (self.front_pointer+1) % self.length  # modulus of length means the newly incremented pointers are always between 0 -> 4 (length 5)
        return old_value
    
    def peek(self) -> Any:
        if self.isEmpty():
            raise QueueUnderflowError("Circular queue is empty. Cannot peek further.")
        return self.elements[self.front_pointer]


queue = CircularQueue(5)