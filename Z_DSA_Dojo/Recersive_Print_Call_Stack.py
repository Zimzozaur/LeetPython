def countdown(n, depth=0):
    indent = "  " * depth
    print(f"{indent}countdown({n})")

    if n == 0:
        print(f"{indent}-> countdown({n}) reached the base case.")
        return

    countdown(n - 1, depth + 1)

    print(f"{indent}-> countdown({n}) completed.")


if __name__ == '__main__':
    countdown(5)
