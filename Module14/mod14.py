import time
import dask.dataframe as ddf

CSV = "steam-200k.csv"

time_start = time.time()
df = ddf.read_csv(CSV)

time_elapsed = time.time()-start

