def check(array, target):
    for i in range(len(array)):
        total = 0
        for j in range(i, len(array)):
            total += array[j]

            if total == target:
                print("Indexes:", list(range(i, j + 1)))
                return

    print("No combination found")


array = [2, 7, 11, 15]
target = 9

check(array, target)