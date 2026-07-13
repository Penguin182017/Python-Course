# Online Python compiler (interpreter) to run Python online.
class StackFrameVisualizer:

    def indent(self, depth):
        return "    " * depth

    # 1. Linear Recursion
    def linear(self, n, depth=0):
        print(f"{self.indent(depth)}Enter linear({n})")

        if n > 0:
            self.linear(n - 1, depth + 1)

        print(f"{self.indent(depth)}Return linear({n})")

    # 2. Tail Recursion
    def tail(self, n, depth=0):
        print(f"{self.indent(depth)}Enter tail({n})")

        if n == 0:
            print(f"{self.indent(depth)}Return tail({n})")
            return

        print(f"{self.indent(depth)}Processing {n}")
        self.tail(n - 1, depth + 1)

        print(f"{self.indent(depth)}Return tail({n})")

    # 3. Head Recursion
    def head(self, n, depth=0):
        print(f"{self.indent(depth)}Enter head({n})")

        if n > 0:
            self.head(n - 1, depth + 1)

        print(f"{self.indent(depth)}Processing {n}")
        print(f"{self.indent(depth)}Return head({n})")

    # 4. Increasing-Decreasing Recursion
    def inc_dec(self, n, depth=0):
        print(f"{self.indent(depth)}Enter inc_dec({n})")

        if n > 0:
            print(f"{self.indent(depth)}Increasing {n}")
            self.inc_dec(n - 1, depth + 1)
            print(f"{self.indent(depth)}Decreasing {n}")

        print(f"{self.indent(depth)}Return inc_dec({n})")

    # 5. Tree Recursion
    def tree(self, n, depth=0):
        print(f"{self.indent(depth)}Enter tree({n})")

        if n > 1:
            self.tree(n - 1, depth + 1)
            self.tree(n - 2, depth + 1)

        print(f"{self.indent(depth)}Return tree({n})")


def main():

    visualizer = StackFrameVisualizer()

    while True:

        print("\n===== Stack Frame Visualizer =====")
        print("1. Linear Recursion")
        print("2. Tail Recursion")
        print("3. Head Recursion")
        print("4. Increasing-Decreasing Recursion")
        print("5. Tree Recursion")
        print("6. Exit")

        choice = input("Enter choice: ")

        if choice == "6":
            print("Program Ended.")
            break

        n = int(input("Enter value of n: "))
        print()

        if choice == "1":
            visualizer.linear(n)

        elif choice == "2":
            visualizer.tail(n)

        elif choice == "3":
            visualizer.head(n)

        elif choice == "4":
            visualizer.inc_dec(n)

        elif choice == "5":
            visualizer.tree(n)

        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()