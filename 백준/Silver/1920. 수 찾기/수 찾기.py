import sys
def binarySearch(k):
    L = 0
    R = n-1
    if n_List[L] > k or n_List[R] < k:
        return False

    while L <= R:
        mid = (L+R)//2
        if n_List[mid] == k:
            return True
        elif n_List[mid] > k:
            R = mid - 1
        else:
            L = mid + 1
    return False

if __name__ == "__main__":
    n = int(input())
    n_List = list(map(int, sys.stdin.readline().split()))

    m = int(input())
    m_List = list(map(int, sys.stdin.readline().split()))

    n_List.sort()

    for num in m_List:
        if binarySearch(num):
            print("1")
        else:
            print("0")


