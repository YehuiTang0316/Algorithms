def merge(array, left_index, right_index, middle):
    left_copy = array[left_index:middle + 1]
    right_copy = array[middle+1:right_index+1]

    left_copy_index = 0
    right_copy_index = 0
    sorted_index = left_index

    while left_copy_index < len(left_copy) and right_copy_index < len(right_copy):

        if left_copy[left_copy_index] <= right_copy[right_copy_index]:
            array[sorted_index] = left_copy[left_copy_index]
            left_copy_index = left_copy_index + 1
        else:
            array[sorted_index] = right_copy[right_copy_index]
            right_copy_index = right_copy_index + 1
        sorted_index = sorted_index + 1

    while left_copy_index < len(left_copy):
        array[sorted_index] = left_copy[left_copy_index]
        left_copy_index = left_copy_index + 1
        sorted_index = sorted_index + 1

    while right_copy_index < len(right_copy):
        array[sorted_index] = right_copy[right_copy_index]
        right_copy_index = right_copy_index + 1
        sorted_index = sorted_index + 1


def merge_sort(array, left_index, right_index):
    """
    time complexity n * log(n)
    :param array:
    :param left_index:
    :param right_index:
    :return:
    """
    if left_index >= right_index:
        return

    middle = (left_index + right_index)//2
    merge_sort(array, left_index, middle)
    merge_sort(array, middle + 1, right_index)
    merge(array, left_index, right_index, middle)


def partition(arr, p, left_index, right_index):
    tmp = arr[p]
    arr[p] = arr[right_index]
    arr[right_index] = tmp

    l = left_index

    for i in range(left_index,right_index+1):
        if arr[i] < arr[right_index]:
            tmp = arr[l]
            arr[l]= arr[i]
            arr[i] = tmp
            l += 1
    tmp = arr[right_index]
    arr[right_index] = arr[l]
    arr[l] = tmp
    return l


def quick_sort(arr, left_index, right_index):
    """

    :param arr:
    :param left_index:
    :param right_index:
    :return:
    """

    if left_index >= right_index - 1:
        return
    pivot_ind = (left_index + right_index) // 2
    r = partition(arr, pivot_ind, left_index, right_index)
    quick_sort(arr, left_index, r)
    quick_sort(arr, r+1, right_index)


if __name__ == '__main__':
    array = [33, 42, 9, 37, 8, 47, 5, 29, 49, 31, 4, 48, 16, 22, 26]
    # merge_sort(array, 0, len(array) - 1)
    quick_sort(array, 0, len(array)-1)
    print(array)
