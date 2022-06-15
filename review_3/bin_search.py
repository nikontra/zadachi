# ID: 68764552
def broken_search(nums: list, target: int) -> int:
    """Поиск индекс елемента target."""
    left: int = 0
    right: int = len(nums) - 1
    if nums[left] == target:
        return left
    elif nums[right] == target:
        return right

    while left <= right:
        mid: int = (left + right)//2
        item = nums[mid]
        if item == target:
            return mid
        if nums[left] < item:
            if nums[left] <= target < item:
                right = mid - 1
            else:
                left = mid + 1
        else:
            if item < target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1
    return -1


def test():
    arr = [19, 21, 100, 101, 1, 4, 5, 7, 12]
    assert broken_search(arr, 5) == 6
