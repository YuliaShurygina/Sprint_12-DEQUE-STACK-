# ID 79875079
# От вас требуется реализовать функцию, осуществляющую поиск в сломанном массиве.
from typing import List, Any


def broken_search(nums: List[Any], target: Any) -> int:
    """Поиск элемента в сломанном массиве."""
    left = 0
    right = len(nums) - 1
    while right >= left:
        left_element = nums[left]
        if left_element == target:
            return left
        mid = (left + right) // 2
        item = nums[mid]
        if item == target:
            return mid
        if left_element <= item:
            if left_element < target < item:
                right = mid - 1
            else:
                left = mid + 1
        else:
            if item < target < left_element:
                left = mid + 1
            else:
                right = mid - 1
    return -1
