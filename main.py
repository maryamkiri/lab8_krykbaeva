import grades

db = {
    "Алия": [90, 85, 100],
    "Тимур": [70, 65, 80],
    "Дана": [95, 100, 90],
    "Ерлан": [50, 60, 45],
}

for name, scores in db.items():
    avg = grades.average(scores)
    print(f"{name}: {avg} ({grades.grade(avg)})")

name, avg = grades.best_student(db)
print(f"Лучший результат: {name} ({avg})")
print()