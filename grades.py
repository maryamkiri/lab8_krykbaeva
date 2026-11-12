"""Модуль для работы с оценками студентов."""

PASS_SCORE = 50


def average(scores):
    """Возвращает среднее арифметическое списка оценок (0 для пустого списка)."""
    if not scores:
        return 0
    return round(sum(scores) / len(scores), 2)


def grade(score):
    """Возвращает буквенную оценку по баллу от 0 до 100."""
    if score >= 90:
        return "A"
    if score >= 75:
        return "B"
    if score >= 60:
        return "C"
    if score >= 50:
        return "D"
    return "F"


def best_student(db):
    """Возвращает имя и средний балл лучшего студента."""
    name = max(db, key=lambda n: average(db[n]))
    return name, average(db[name])


if __name__ == "__main__":
    print("Проверка модуля grades")
    print(average([90, 80, 70]), grade(80), grade(45))

def passed(score):
    return score>= PASS_SCORE

def count_by_grade(db, letter):
    """Считает, сколько студентов получили по среднему баллу оценку letter."""
    count = 0
    for scores in db.values():
        if grade(average(scores)) == letter:
            count += 1
    return count
