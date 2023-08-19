def two_int_equals_target(vetor: list[int], target: int, low=0, high=None):

    if high is None:
        high = len(vetor)-1

    if vetor[low] + vetor[high] == target:
        return True

    elif low > high:
        return False

    else:
        if vetor[low] + vetor[high] < target:
            return two_int_equals_target(vetor, target, low + 1, high)
        else:
            return two_int_equals_target(vetor, target, low, high - 1)


print(two_int_equals_target([1, 2, 3, 4, 6, 7, 8, 9], 5))
