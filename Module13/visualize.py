import dask.delayed as delayed
from compute import MAX_NUMBER, log, first, second, third

FILE_NAME = "mydask.png"

def main():
    firstThird = int(MAX_NUMBER / 3)
    secondThird = int(MAX_NUMBER * 2 / 3)
    log((firstThird, secondThird))

    firstSet = range(1, firstThird)
    secondSet = range(firstThird, secondThird)
    thirdSet = range(secondThird, MAX_NUMBER)
    log(f'{firstSet}\n{secondSet}\n{thirdSet}')

    step1 = delayed(first)(firstSet)
    step2 = delayed(second)(secondSet)
    step3 = delayed(third)(thirdSet)
    total = delayed(sum)((step1, step2, step3))
    log(f'{step1}\n{step2}\n{step3}')

    total.visualize(FILE_NAME)
    print(f"made file {FILE_NAME}")

if __name__ == '__main__':
    main()