import sys

INTS = ["one", "two", "three", "four", "five", "six", "seven", "eight","nine"]

def main():
    mode = sys.argv[1]
    if mode == "test":
        file = "./test.txt"
    elif mode == "part1":
        file = "./part1.txt"
    elif mode == "part2":
        file = "./part2.txt"

    input = open(file, 'r')
    lines = input.readlines()
    total = 0
    for line in lines:
        numbers = []
        line.casefold()
        print(line.index("two"))
        for value in line:
            if value.isnumeric():
                numbers.append(value)
        result = numbers[0] + numbers.pop()
        total += int(result)
    print(total)

if __name__ == "__main__":
    main()