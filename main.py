import number_tools
import array_tools
import marks_tools

SUBJECTS = 3


def read_int(message, low, high):
    while True:
        text = input(message)
        if text.isdigit():
            value = int(text)
            if value >= low and value <= high:
                return value
        print("Invalid input. Enter a number from", low, "to", high)


def read_list():
    text = input("Enter numbers separated by spaces: ")
    parts = text.split()
    numbers = []
    for p in parts:
        if p.isdigit():
            numbers.append(int(p))
    return numbers


def number_menu():
    while True:
        print("\n--- Number Tools ---")
        print("1. Factorial")
        print("2. Fibonacci series")
        print("3. Reverse a number")
        print("4. Base conversion")
        print("5. GCD of two numbers")
        print("6. Primes up to a limit")
        print("7. Prime factors")
        print("8. Square root")
        print("9. Back")
        choice = read_int("Choice: ", 1, 9)

        if choice == 1:
            n = read_int("n (0-500): ", 0, 500)
            print("Factorial =", number_tools.factorial(n))
        elif choice == 2:
            n = read_int("How many terms (1-50): ", 1, 50)
            print(number_tools.fibonacci(n))
        elif choice == 3:
            n = read_int("Number: ", 0, 10 ** 12)
            print("Reversed =", number_tools.reverse_number(n))
        elif choice == 4:
            n = read_int("Decimal number: ", 0, 10 ** 12)
            base = read_int("Convert to base (2-16): ", 2, 16)
            print("Result =", number_tools.to_base(n, base))
        elif choice == 5:
            a = read_int("First number: ", 1, 10 ** 12)
            b = read_int("Second number: ", 1, 10 ** 12)
            print("GCD =", number_tools.gcd(a, b))
        elif choice == 6:
            limit = read_int("Limit (2-10000): ", 2, 10000)
            print(number_tools.generate_primes(limit))
        elif choice == 7:
            n = read_int("Number (2 or more): ", 2, 10 ** 12)
            print("Smallest divisor =", number_tools.smallest_divisor(n))
            print("Prime factors =", number_tools.prime_factors(n))
        elif choice == 8:
            n = read_int("Number: ", 0, 10 ** 9)
            print("Square root =", round(number_tools.square_root(n), 4))
        else:
            break


def array_menu():
    while True:
        print("\n--- Array Tools ---")
        print("1. Maximum and minimum")
        print("2. Reverse the list")
        print("3. Remove duplicates")
        print("4. Count an item")
        print("5. Kth smallest element")
        print("6. Partition around a pivot")
        print("7. Sort the list")
        print("8. Back")
        choice = read_int("Choice: ", 1, 8)
        if choice == 8:
            break

        data = read_list()
        if len(data) == 0:
            print("No valid numbers entered.")
            continue

        if choice == 1:
            print("Max =", array_tools.find_max(data))
            print("Min =", array_tools.find_min(data))
        elif choice == 2:
            print(array_tools.reverse_list(data))
        elif choice == 3:
            print(array_tools.remove_duplicates(data))
        elif choice == 4:
            item = read_int("Item to count: ", 0, 10 ** 12)
            print("Count =", array_tools.count_item(data, item))
        elif choice == 5:
            k = read_int("k: ", 1, len(data))
            print("Answer =", array_tools.kth_smallest(data, k))
        elif choice == 6:
            pivot = read_int("Pivot: ", 0, 10 ** 12)
            small, same, big = array_tools.partition(data, pivot)
            print("Smaller:", small)
            print("Equal  :", same)
            print("Bigger :", big)
        elif choice == 7:
            print(array_tools.sort_list(data))


def marks_menu(students):
    while True:
        print("\n--- Student Marks ---")
        print("1. Add student")
        print("2. Remove student")
        print("3. Show all students")
        print("4. Show topper")
        print("5. Rank list")
        print("6. Grade summary")
        print("7. Back")
        choice = read_int("Choice: ", 1, 7)

        if choice == 1:
            name = input("Student name: ").strip()
            if name == "":
                print("Name cannot be empty.")
                continue
            marks = []
            for i in range(SUBJECTS):
                marks.append(read_int("Marks for subject " + str(i + 1) + " (0-100): ", 0, 100))
            marks_tools.add_student(students, name, marks)
            print("Saved.")
        elif choice == 2:
            name = input("Name to remove: ").strip()
            if marks_tools.remove_student(students, name):
                print("Removed.")
            else:
                print("No such student.")
        elif len(students) == 0:
            if choice != 7:
                print("No students added yet.")
        elif choice == 3:
            for name in students:
                avg = marks_tools.average(students[name])
                print(name, students[name], "avg =", round(avg, 2),
                      "grade =", marks_tools.get_grade(avg))
        elif choice == 4:
            name, avg = marks_tools.topper(students)
            print("Topper:", name, "with average", round(avg, 2))
        elif choice == 5:
            position = 1
            for name, avg in marks_tools.rank_list(students):
                print(position, name, round(avg, 2))
                position += 1
        elif choice == 6:
            print("Grades:", marks_tools.grade_count(students))
            print("Highest average:", round(array_tools.find_max(marks_tools.all_averages(students)), 2))
            print("Lowest average :", round(array_tools.find_min(marks_tools.all_averages(students)), 2))
            print("Distinct marks used:", len(marks_tools.distinct_marks(students)))
        else:
            break


def main():
    students = {}
    print("=== Number and Marks Toolkit ===")
    while True:
        print("\nMAIN MENU")
        print("1. Number tools")
        print("2. Array tools")
        print("3. Student marks")
        print("4. Exit")
        choice = read_int("Choice: ", 1, 4)
        if choice == 1:
            number_menu()
        elif choice == 2:
            array_menu()
        elif choice == 3:
            marks_menu(students)
        else:
            print("Bye!")
            break


main()
