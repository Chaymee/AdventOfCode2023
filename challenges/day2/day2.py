from re import split
import sys

POSSIBLE = {"red": 12, "green": 13, "blue": 14}


def main():
    input = select_file(sys.argv[1])

    gamesdicts = [split_game(line) for line in input.readlines()]
    print(gamesdicts)
    part1=0
    for gameset in gamesdicts:
        results = [part_1(game) for game in gameset[1]]
        if all(item == True for item in results):
            part1 += int(gameset[0])
    print(part1)
    part2 = 0
    for gameset in gamesdicts:
        part2 += part_2(gameset)
    print("part2: " + str(part2))


def select_file(mode):
    if mode == "test":
        file = "./test.txt"
    elif mode == "part1":
        file = "./part1.txt"
    elif mode == "part2":
        file = "./part2.txt"
    return open(file, "r")


def split_game(line):
    games = line.split(":")
    gameNumber = games[0].split(" ")
    games = games[1].split(";")
    gameNumber = gameNumber[1]
    games = [game.split(" ") for game in games]
    gamesdicts = []
    for game in games:
        game.remove("")
        game = [item.strip("\n") for item in game]
        game = [item.strip(",") for item in game]
        gamedict = {game[i + 1]: int(game[i]) for i in range(0, len(game), 2)}
        gamesdicts.append(gamedict)
    return gameNumber, gamesdicts

"""


def score_game(game):
    win = False
    game.remove("")
    game = [word.strip(",") for word in game]
    game = [word.strip("\n") for word in game]
    dct = {game[i+1]: game[i] for i in range(0, len(game), 2)}
    #print(dct)
    #print(POSSIBLE)
    #print(all(int(dct.get(key)) <= int(POSSIBLE.get(key)) for key in dct.keys()))
    # Part 1

    # Part 2

"""


def part_1(gamedict):
    return all(gamedict.get(key) <= POSSIBLE.get(key) for key in gamedict.keys())

def part_2(gamedict) -> int:
    minimum = {"red": 0, "green": 0, "blue": 0}
    games = gamedict[1]
    for game in games:
        for key in game.keys():
            if game.get(key) > minimum.get(key):
                minimum.update({key: game.get(key)})
    print(minimum.values())
    power = 1
    for value in minimum.values():
        if int(value) > 0:
            power = power * value
    print(power)
    return power


if __name__ == "__main__":
    main()
