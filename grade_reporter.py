scores = [72, 45, 90, 61, 38]

passed = 0
failed = 0
total = 0

for score in scores:
    if score >= 80:
        grade = "A"
    elif score >= 70:
        grade = "B"
    elif score >= 50:
        grade = "C"
    else:
        grade = "F"

    print(f"{score} - {grade}")
    total += score

    if score >= 50:
        passed += 1
    else:
        failed += 1

print(f"Passed: {passed}")
print(f"Failed: {failed}")

average = total / len(scores)
print(f"Average: {round(average, 1)}")