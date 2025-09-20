# Problem: Tuples
# Link: https://www.hackerrank.com/challenges/python-tuples/problem
# Language: Python 2
# Approach: print the hash(t) of the tuple elements

if __name__ == '__main__':
    n = int(raw_input())
    integer_list = tuple(map(int, raw_input().split()))
    print(hash(integer_list))
