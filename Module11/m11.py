"""
Name:John Valencia-Londono
Date:11/12/2023
Assignment:Module11:
Due Date:11/12/2023
About this project:
Demonstrate threads and threadevents using ThreadPoolExecutor to calculate several processes of the FV equation
in concurrency. FV = PV * (1+(i/n)) ** (n*t)
All work below was performed by John Valencia-Londono
"""
import random
import time
from concurrent.futures import ThreadPoolExecutor

MAX_WORKERS = 3
global_years = []


def fv(pv,i,n,t):
    global_years.append(t)
    return pv * (1+(i/n)) ** (n*t)

def main():
    random.seed(time.time())
    r1 = random.uniform(0.05,0.1)
    r2 = random.uniform(0.05,0.1)
    r3 = random.uniform(0.05,0.1)

    arg0=[10,10,10]
    arg1=[r1,r2,r3]
    arg2=[2,2,2]
    arg3=[4,5,6]

    with ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
        # There are 4 threads theoretically. Three threads are working on solving the fv() function. 
        # The last thread which is the main is waiting on the completion of all threads to return the result
        results = executor.map(fv,arg0,arg1,arg2,arg3)

        max = 0
        i = 0
        for result in results:
            print("total number of payments:" + str(arg2[i] + arg3[i]) + " Future Value: " + str(result))
            i=i+1
            if result > max:
                max = result
        print("Highest future value: " + str(max))


if __name__ == '__main__':
    main()
