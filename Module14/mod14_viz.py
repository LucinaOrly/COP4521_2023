import time
from dask.diagnostics import ProgressBar
import dask.dataframe as ddf

CSV = "Motor_Vehicle_Collisions_-_Crashes.csv"
dtype={'CONTRIBUTING FACTOR VEHICLE 3': 'object',
       'CONTRIBUTING FACTOR VEHICLE 4': 'object',
       'CONTRIBUTING FACTOR VEHICLE 5': 'object',
       'NUMBER OF PERSONS INJURED': 'float64',
       'VEHICLE TYPE CODE 3': 'object',
       'VEHICLE TYPE CODE 4': 'object',
       'VEHICLE TYPE CODE 5': 'object',
       'ZIP CODE': 'object'}

time_start = time.time()
df = ddf.read_csv(CSV, dtype=dtype,assume_missing=True)

time_elapsed = time.time()-time_start
print(f"Time elapsed: {time_elapsed}ms")

with ProgressBar(): print(df.dtypes)



print()
print("Aggregate for NUMBER OF PERSONS INJURED:")
series = df["NUMBER OF PERSONS INJURED"]
with ProgressBar():
       print(series.describe().visualize("NUMBER OF PERSONS INJURED"))

print()
print("Aggregate for NUMBER OF PERSONS KILLED:")
series = df["NUMBER OF PERSONS KILLED"]
with ProgressBar():
       print(series.describe().visualize("NUMBER OF PERSONS KILLED"))

print()
print("Aggregate for VEHICLE TYPE CODE 1:")
series = df["VEHICLE TYPE CODE 1"]
with ProgressBar():
       print(series.describe().visualize("VEHICLE TYPE CODE 1"))
       
print()
print("Aggregate for VEHICLE TYPE CODE 3:")
series = df["VEHICLE TYPE CODE 3"]
with ProgressBar():
       print(series.describe().visualize("VEHICLE TYPE CODE 3"))

print()
print("Aggregate for CONTRIBUTING FACTOR VEHICLE 3:")
series = df["CONTRIBUTING FACTOR VEHICLE 3"]
with ProgressBar():
       print(series.describe().visualize("CONTRIBUTING FACTOR VEHICLE 3"))
       
print()
print("Aggregate for ZIP CODE:")
series = df["ZIP CODE"]
with ProgressBar():
       print(series.describe().visualize("ZIP CODE"))
