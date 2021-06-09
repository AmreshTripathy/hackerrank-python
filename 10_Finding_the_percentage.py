if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        line = input().split()
        name, scores = line[0], line[1:]
        scores = map(float, scores)
        student_marks[name] = scores
    query_name = input()
    print ("{0:.2f}".format(*[(sum(scores)/len(scores))for name, scores in student_marks.items() if name==query_name]))
