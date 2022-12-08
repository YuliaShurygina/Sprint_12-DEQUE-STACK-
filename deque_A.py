# ID 78986607
from typing import List, Any
import logging


class DequeIsEmpty(Exception):
    pass


class DequeIsFull(Exception):
    pass


class Deque:
    """Создаем класс Deque."""

    def __init__(self, n):
        self.deque: List[int] = [None] * n
        self.max_n: int = n
        self.__size: int = 0
        self.__head: int = 0
        self.__tail: int = 0

    def is_empty(self):
        """Метод проверки пустая ли очередь."""
        return self.__size == 0

    def find_index(n: int, some_index: int, one: int) -> int:
        """Метод вычисления индекса."""
        return (some_index + one) % n

    def push_front(self, value) -> None:
        """Метод добавления элемента в очередь слева."""
        if self.__size != self.max_n:
            self.__head = Deque.find_index(self.max_n, self.__head, -1)
            self.deque[self.__head] = value
            self.__size += 1
        else:
            raise DequeIsFull('error')

    def push_back(self, value) -> None:
        """Метод добавления элемента в очередь справа."""
        if self.__size != self.max_n:
            self.deque[self.__tail] = value
            self.__tail = Deque.find_index(self.max_n, self.__tail, 1)
            self.__size += 1
        else:
            raise DequeIsFull('error')

    def pop_front(self) -> int:
        """Метод удаления элемента слева."""
        if self.is_empty():
            raise DequeIsEmpty('error')
        x: int = self.deque[self.__head]
        self.deque[self.__head] = None
        self.__head = Deque.find_index(self.max_n, self.__head, 1)
        self.__size -= 1
        return x

    def pop_back(self) -> int:
        """Метод удаления элемента справа."""
        if self.is_empty():
            raise DequeIsEmpty('error')
        x: int = self.deque[self.__tail - 1]
        self.deque[self.__tail - 1] = None
        self.__size -= 1
        self.__tail = Deque.find_index(self.max_n, self.__tail, -1)
        return x


def main():
    commands: int = int(input())
    max_size: int = int(input())
    deque: Deque = Deque(max_size)
    for i in range(commands):
        command, *params = input().strip().split()
        try:
            result: Any = getattr(deque, command)(*params)
            if result:
                print(result)
        except Exception as error:
            logging.error(f'{error} Проверьте вводимые',
                          f'символы в команде {command}!')
            print('error')


if __name__ == '__main__':
    main()
