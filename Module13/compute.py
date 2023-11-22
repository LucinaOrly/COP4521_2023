"""
Name:John Valencia-Londono
Date:11/22/2023
Assignment:Module13: Python Dask Multi Task Script
Due Date:11/26/2023
About this project:
Demonstrate knowledge of distributed computing by using the Dask library to compute
alternating harmonic series that approximates = ln 2. Visualize the DAG
All work below was performed by John Valencia-Londono
"""
import dask.delayed as delayed
from dask.diagnostics import ProgressBar

DEBUG = False # modify this to True to see log()
MAX_NUMBER = 10000000 # modify this to test higher numbers

def log(s):
    if DEBUG:
        print(s)


#calculate the number in series
def num_in_series(num):
    return 1 / (num if num % 2 != 0 else -num)

def sum(iterable):
   sum = 0
   for i in iterable:
       sum = sum + i
   return sum


# old series done with ranges
# # series used should approximate = ln 2
# def series(start, end):
#     sum = 0
#     for i in range(start, end):
#         sum = num_in_series()
#     return sum


# per the requirement of the assignment, must be placed in three different functions
@delayed
def first(col):
    result = sum(map(num_in_series,col))
    log("first() finished computing!")
    return result


@delayed
def second(col):
    result = sum(map(num_in_series,col))
    log("second() finished computing!")
    return result


@delayed
def third(col):
    result = sum(map(num_in_series,col))
    log("third() finished computing!")
    return result


def main():
    firstThird = int(MAX_NUMBER / 3)
    secondThird = int(MAX_NUMBER * 2 / 3)
    log((firstThird, secondThird))

    firstSet = range(1,firstThird)
    secondSet = range(firstThird,secondThird)
    thirdSet = range(secondThird,MAX_NUMBER)
    log(f'{firstSet}\n{secondSet}\n{thirdSet}')

    step1 = delayed(first)(firstSet)
    step2 = delayed(second)(secondSet)
    step3 = delayed(third)(thirdSet)
    total = delayed(sum)((step1,step2,step3))
    log(f'{step1}\n{step2}\n{step3}')

    with ProgressBar():
        print(total.compute())


if __name__ == '__main__':
    main()
