# Problem: Find the Runner-Up Score
# Link: https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem?isFullScreen=true
# Language: Python 3
# Approach: Convert list to set to remove duplicates, sort in descending order, pick second element


if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))

    arr = list(set(arr))
    arr.sort(reverse=True)
    print(arr[1])
