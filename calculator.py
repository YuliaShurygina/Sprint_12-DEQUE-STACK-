# ID 78805735
# >>> type(lambda a, b: a * b)
# function
# ```
# Тут нужно воспользоваться дженериками.

# ```python
# from typing import Callable

# operations: Dict[str, Callable(int, int), int] = {} 
from typing import List, Dict, Callable


class Stack:
    """Создаем класс Stack."""

    def __init__(self) -> None:
        self.items: List[int] = []

    def push(self, item) -> None:
        """Метод добавления элемента в Stack."""
        self.items.append(item)

    def pop(self) -> int:
        """Метод удаления элемента из Stack."""
        try:
            return self.items.pop()
        except IndexError:
            raise IndexError("Стек пустой!")
  

    def peek(self) -> int:
        """Метод чтения элемента из Stack."""
        return self.items[-1]


def calculator(expression_array: List[str]) -> Stack:
    """Вычисление выражения."""
    new_stack: Stack = Stack()
    operations: Dict[str, Callable(int, int), int] = {'*': lambda a, b: a * b,
                                  '+': lambda a, b: a + b,
                                  '/': lambda a, b: b // a,
                                  '-': lambda a, b: b - a, }
    for i in expression_array:
        if i.lstrip("-").isdigit():
            new_stack.push(i)
        else:
            try:
                a = int(new_stack.pop())
                b = int(new_stack.pop())
                new_stack.push(operations[i](a, b))
            except Exception as error:
                print(f'{error} Проверьте вводимые символы!')
    return new_stack


def main():
    expression_array: List[str] = [str(i) for i in input().strip().split()]
    print(calculator(expression_array).peek())


if __name__ == '__main__':
    main()
