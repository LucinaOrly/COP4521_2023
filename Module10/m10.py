"""
Name:John Valencia-Londono
Date:11/5/2023
Assignment:Module 10: Using Threads
Due Date:11/5/2023
About this project:
Play craps 100,000 times. Use a ThreatPoolExecutor(max_workers=3).
All work below was performed by John Valencia-Londono """
import concurrent.futures
import random

NUM_OF_TRIALS = 100000
MAX_WORKERS = 3

# play craps. Win if two dice sum to 7 or 11
def playcraps(none):
    d1 = random.randint(1,6)
    d2 = random.randint(1,6)
    total = d1+d2

    if total == 7 or total == 11:
        return 1
    return 0



def main():
    # create a ThreadPoolExecutor w/ max_workers=3
    with concurrent.futures.ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
        # play craps with the exectutor NUM_OF_TRIALS times (default: 100,000)
        results = executor.map(playcraps,range(1,NUM_OF_TRIALS))

        # calculate the sum / NUM_OF_TRIALS
        sum = 0
        for result in results:
            sum += result
        print("Sum of results / Num of Trials = " + str(sum / NUM_OF_TRIALS))

if __name__ == '__main__':
    main()

""" 
Sample Output:
Sum of results / Num of Trials = 0.22309
"""