file = "students.txt"

# 🔹 Create file automatically if it doesn't exist
open(file, "a").close()

while True:
    print("\n1.Add  2.View  3.Update  4.Exit")
    choice = input("Choose: ")

    # ADD
    if choice == "1":
        name = input("Name: ").strip()
        subject = input("Subject: ").strip()

        if name and subject:
            with open(file, "a") as f:
                f.write(f"{name},{subject}\n")
            print("Added!")
        else:
            print("Invalid input")

    # VIEW
    elif choice == "2":
        with open(file, "r") as f:
            lines = f.readlines()

        if not lines:
            print("No students yet")
        else:
            print("\nStudents:")
            for i, line in enumerate(lines, 1):
                n, s = line.strip().split(",")
                print(f"{i}. {n} - {s}")

    # UPDATE (by number = easier, no name mistakes)
    elif choice == "3":
        with open(file, "r") as f:
            lines = f.readlines()

        if not lines:
            print("No students to update")
            continue

        print("\nStudents:")
        for i, line in enumerate(lines, 1):
            n, s = line.strip().split(",")
            print(f"{i}. {n} - {s}")

        try:
            num = int(input("Enter number to update: "))
            if 1 <= num <= len(lines):
                new_sub = input("New subject: ").strip()
                n, _ = lines[num - 1].strip().split(",")
                lines[num - 1] = f"{n},{new_sub}\n"

                with open(file, "w") as f:
                    f.writelines(lines)

                print("Updated!")
            else:
                print("Invalid number")
        except:
            print("Enter a valid number")

    elif choice == "4":
        print("Done 👍")
        break

    else:
        print("Invalid choice")