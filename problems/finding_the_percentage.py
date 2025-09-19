# Problem: Finding the Percentage
# Link: https://www.hackerrank.com/challenges/finding-the-percentage/problem
# Language: Python 3
# Approach: Store student marks in a dictionary, retrieve the queried student, compute average, format to 2 decimal places


if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    list_of_scores = student_marks.get(query_name)
    average = sum(list_of_scores) / len(list_of_scores)
    print(f"{average:.2f}")
