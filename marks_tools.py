import array_tools


def average(marks):
    total = 0
    for m in marks:
        total += m
    return total / len(marks)


def get_grade(avg):
    if avg >= 90:
        return "S"
    elif avg >= 80:
        return "A"
    elif avg >= 70:
        return "B"
    elif avg >= 60:
        return "C"
    elif avg >= 50:
        return "D"
    else:
        return "F"


def add_student(students, name, marks):
    students[name] = marks


def remove_student(students, name):
    if name in students:
        del students[name]
        return True
    return False


def topper(students):
    best_name = ""
    best_avg = -1
    for name in students:
        avg = average(students[name])
        if avg > best_avg:
            best_avg = avg
            best_name = name
    return (best_name, best_avg)


def grade_count(students):
    counts = {}
    for name in students:
        g = get_grade(average(students[name]))
        if g in counts:
            counts[g] += 1
        else:
            counts[g] = 1
    return counts


def all_averages(students):
    avgs = []
    for name in students:
        avgs.append(average(students[name]))
    return avgs


def distinct_marks(students):
    marks_set = set()
    for name in students:
        for m in students[name]:
            marks_set.add(m)
    return marks_set


def rank_list(students):
    pairs = []
    for name in students:
        pairs.append((name, average(students[name])))
    for i in range(len(pairs)):
        best = i
        for j in range(i + 1, len(pairs)):
            if pairs[j][1] > pairs[best][1]:
                best = j
        pairs[i], pairs[best] = pairs[best], pairs[i]
    return pairs
