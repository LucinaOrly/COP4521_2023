"""
Name:John Valencia-Londono
Date:11/19/2023
Assignment:Module12: Using Threads with Locks
Due Date:11/19/2023
About this project:
Demonstrate locks using craps players and an accountant
All work below was performed by John Valencia-Londono
"""
import random as ran
from os.path import exists
from threading import Thread, Barrier, Lock

FILE_NAME = "win.txt"
NUM_OF_PLAYERS = 10
DEBUG = False # change to true to see player's results

''' play craps with the following win chart:
2              3 to 1
3 or 4       1 to 1 (evens)
10 or 11    2 to 1
12            5 to 1
'''


def craps(bet) -> int:
    if bet < 0:
        raise Exception("Bet has to be greater than 0")

    die = ran.randint(1, 6) + ran.randint(1, 6)
    if die == 3 or die == 4:
        return bet
    elif die == 10 or die == 11:
        return bet * 2
    elif die == 2:
        return bet * 3
    elif die == 12:
        return bet * 5
    else:
        return 0


def log(s):
    if DEBUG:
        print(s)


def clearFile():
    lock.acquire()
    open(FILE_NAME, "w").close()
    lock.release()


# noinspection PyGlobalUndefined
def appendFile(strng):
    global lock
    f = open(FILE_NAME, "a", encoding="utf-8")
    lock.acquire()
    f.write(strng + '\n')
    f.close()
    lock.release()
    log(f"appended {strng} to file")


# called after all players finished as defined by the barrier
def accountant(barrier):
    # wait for all players to finish before accounting
    barrier.wait()
    print("All players finished!")

    global lock, sum
    lock.acquire()
    f = open(FILE_NAME, "r", encoding="utf-8")
    nums = f.readlines()
    f.close()
    lock.release()

    clearFile()

    for num in nums:
        sum = sum + int(num)

    print(f"Accountant counted money earned by players = {sum}")


def player(barrier, name="", money=500):
    while money > 0:
        bet = ran.randint(1, money)
        win = craps(bet)
        if win:
            appendFile(str(win))
            log(f"{name}: won {win}! Money left={money}")
        else:
            money = money - bet
            log(f"{name}:lost {bet}. Money left={money}")
    # thread ends when out of money
    print(f"Player {name} out of money!")
    barrier.wait()


def main():
    global sum, lock
    sum = 0
    lock = Lock()

    barrier = Barrier(NUM_OF_PLAYERS + 1)
    for i in range(NUM_OF_PLAYERS):
        worker = Thread(target=player, args=(barrier, i, 500))
        worker.start()
    acc = Thread(target=accountant, args=(barrier,))
    acc.start()
    acc.join()
    print("Accountant finished!")


if __name__ == "__main__":
    if not exists(FILE_NAME):
        open(FILE_NAME, "w").close()
    main()
