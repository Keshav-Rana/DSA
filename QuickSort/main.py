class QuickSort:
    def __init__(self, array):
        self.array = array

    def partition(self, array, start, end):
        # we always pick the first element as the pivot
        pivotIdx = start
        pivotElem = array[pivotIdx]

        while start <= end:
            # find the first element from left that is greater than pivot
            while start <= end and array[start] <= pivotElem:
                start += 1

            # find the last element from right that is smaller than pivot
            while start <= end and array[end] > pivotElem:
                end -= 1

            # swap the variables
            if start < end:
                array[start], array[end] = array[end], array[start]

        # place the pivot in the right place which would be at the idx pointed by end var
        array[pivotIdx], array[end] = array[end], array[pivotIdx]
        return end

    def sort_list(self, start, end):
        if (start < end):
            # pivot consists of the idx
            pivot = self.partition(self.array, start, end)
            # call the sort list on left subarray
            self.sort_list(start, pivot-1)
            # call the sort list on right subarray
            self.sort_list(pivot+1, end)

if __name__ == "__main__":
    # test out quicksort here
    ls = [1,1,1,1]

    qs = QuickSort(ls)
    qs.sort_list(0, len(ls) - 1)

    print(ls)

