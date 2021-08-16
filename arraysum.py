def counElements(arr) -> int:
    """
    :type arr: List[int] - List of integers
    :rtype: int - Number of elements in arr satisfying the condition
    """

    result = 0

    for value in arr:
        n_value = value + 1

        if (n_value in arr):
            result += 1

    return result


if __name__ =='__main__':
    line = input()
    components = line.strip().split()
    arr = [int(component) for component in components]

    print(counElements(arr))
