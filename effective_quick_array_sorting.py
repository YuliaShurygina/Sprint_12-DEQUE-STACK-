# ID 79906115
# Тимофей решил сортировать таблицу результатов следующим образом:
# при сравнении двух участников выше будет идти тот,
#  у которого решено больше задач.
# При равенстве числа решённых задач первым идёт участник с меньшим штрафом.
#  Если же и штрафы совпадают, то первым будет тот,
#  у которого логин идёт раньше в алфавитном (лексикографическом) порядке.
from typing import Any, List, Tuple


def fast_sorting(array: List[Any]) -> List[Any]:
    """Эффективная быстрая сортировка
       без использования дополнительной памяти."""

    def quick_sorting(left: int, right: int) -> None:
        if right <= left:
            return
        mid = (left + right) // 2
        mid_element = array[mid]
        left_index = left
        right_index = right
        while left_index <= right_index:
            if array[left_index] < mid_element:
                left_index += 1
                continue
            if mid_element < array[right_index]:
                right_index -= 1
                continue
            if left_index > right_index:
                break
            (
                array[left_index], array[right_index]
            ) = (
                array[right_index], array[left_index]
            )
            left_index += 1
            right_index -= 1
        quick_sorting(left, right_index)
        quick_sorting(left_index, right)
    quick_sorting(0, len(array) - 1)
    return array


if __name__ == '__main__':

    #def changing_data(*participant: Tuple[Any]) -> Tuple[Any]:
    #    """Изменение данных для удобства сравнения."""
     #   return -int(participant[1]), int(participant[2]), participant[0]

    # participants = int(input())
    # print(*[name for _, _, name in fast_sorting(
    #        [changing_data(*input().split(
    #         )) for participant in range(participants)])], sep='\n')
    print(
        *[name for _, _, name in fast_sorting([
            (lambda name, tasks, penalty:
                (-int(tasks), int(penalty), name)
             )(
                *input().split()
            ) for _ in range(int(input()))
        ])],
        sep='\n',
    )
