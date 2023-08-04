def walk(steps):
    for i in range(0, steps):
        print(f"Step: {i}")


def r_walk(steps):

    if steps < 1:  # Base case
        return
    print(f"Step: {steps}")
    r_walk(steps - 1)  # Recursive case


if __name__ == '__main__':
    r_walk(5)
