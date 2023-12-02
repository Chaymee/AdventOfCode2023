import sys

INTS = {"one":"1", "two":"2", "three":"3", "four":"4", "five":"5", "six":"6", "seven":"7", "eight":"8","nine":"9"}

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
     total += fix_numbers(line)
    print(total)

def fix_numbers(s: str) -> int:
    numbers = []
    for num, digit in INTS.items():
        s = s.replace(num, f"{num[0]}{digit}{num[-1]}")
    for value in s:
        if value.isnumeric():
            numbers.append(value)
    result = numbers[0] + numbers.pop()
    return int(result)

if __name__ == "__main__":
    main()