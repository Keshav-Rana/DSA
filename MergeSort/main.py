class MergeSort:
    def __init__(self, arr):
        self.arr = arr
        self.low = 0
        self.high = len(arr) - 1 # last idx

    def merge(self, arr, low, mid, high):
        # create temp array to store sorted/merged elements
        temp = []
        i = low
        j = mid+1

        # two pointer approach
        while i <= mid and j <= high:
            if arr[i] <= arr[j]:
                temp.append(arr[i])

                i += 1

            else:
                temp.append(arr[j])
                j += 1

        # push remaining elements
        while i <= mid:
            temp.append(arr[i])
            i += 1

        while j <= high:
            temp.append(arr[j])
            j += 1

        # update the original array
        for i in range(low, high+1):
            arr[i] = temp[i - low]


    def sortHelper(self, arr, low, high):
        # base case - we have a single element or no elements in our divided array
        if low >= high:
            return
        
        # calculate mid of the array
        mid = (low + high) // 2
        
        # call merge sort on the left subarray
        self.sortHelper(arr, low, mid)
        # call merge sort on the right subarray
        self.sortHelper(arr, mid+1, high)
        # merge the two sub arrays
        self.merge(arr, low, mid, high)

    def sort(self):
        self.sortHelper(self.arr, self.low, self.high)

if __name__ == '__main__':
    # test out merge sort here
    arr = [-1, -100, -200]

    m = MergeSort(arr)

    m.sort()

    print(arr)
