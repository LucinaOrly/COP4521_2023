import random
import time
from concurrent.futures import ThreadPoolExecutor

MAX_WORKERS = 3
global_years = []

args = []

def fv(pv,i,n,t):
    global_years.append(t)
    return pv * (1+(i/n)) ** (n*t)

def main():
    random.seed(time.time())
    r1 = random.uniform(0.05,0.1)
    r2 = random.uniform(0.05,0.1)
    r3 = random.uniform(0.05,0.1)


    with ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
        results = executor.map(fv)

if __name__ == '__main__':
    main()