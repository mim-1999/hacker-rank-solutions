# Problem: List Operations
# Link: https://www.hackerrank.com/challenges/python-lists/problem
# Language: Python 3
# Approach: Use built-in methods of list to generate output


if __name__ == '__main__':
    N = int(input())
    my_list = []

    for _ in range(N):
        commands, *args = input().split()
        args = list(map(int, args))

        if commands == 'insert':
            my_list.insert(args[0], args[1])
        elif commands == 'print':
            print(my_list)
        elif commands == 'remove':
            my_list.remove(args[0])
        elif commands == 'append':
            my_list.append(args[0])
        elif commands == 'sort':
            my_list.sort()
        elif commands == 'pop':
            my_list.pop()
        elif commands == 'reverse':
            my_list.reverse()
