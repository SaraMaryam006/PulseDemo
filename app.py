def calculate_total(marks):
    return sum(marks)


def calculate_average(marks):
    return calculate_total(marks) / len(marks)


def get_result(average):
    if average >= 40:
        return "PASS"
    return "FAIL"