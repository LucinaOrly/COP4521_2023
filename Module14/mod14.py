"""
https://catalog.data.gov/dataset/motor-vehicle-collisions-crashes
Name:John Valencia-Londono
Date:12/4/2023
Assignment:Module14: Dask Large Dataset
Due Date:12/3/2023
About this project:
Demonstrate knowledge of distributed computing by using the Dask library to compute
Data Sets and fetch Series to compute aggregates. Also visualize a DAG used by DASK
All work below was performed by John Valencia-Londono
"""
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

with ProgressBar():
       print(df.dtypes)



print()
print("Aggregate for NUMBER OF PERSONS INJURED:")
series = df["NUMBER OF PERSONS INJURED"]
with ProgressBar():
       print(series.describe().apply(lambda x: format(x,'f'), meta=('NUMBER OF PERSONS INJURED', 'float64')).compute())

print()
print("Aggregate for NUMBER OF PERSONS KILLED:")
series = df["NUMBER OF PERSONS KILLED"]
with ProgressBar():
       print(series.describe().apply(lambda x: format(x,'f'), meta=('NUMBER OF PERSONS INJURED', 'float64')).compute())

print()
print("Aggregate for VEHICLE TYPE CODE 1:")
series = df["VEHICLE TYPE CODE 1"]
with ProgressBar():
       print(series.describe().compute())

print()
print("Aggregate for VEHICLE TYPE CODE 3:")
series = df["VEHICLE TYPE CODE 3"]
with ProgressBar():
       print(series.describe().compute())

print()
print("Aggregate for CONTRIBUTING FACTOR VEHICLE 3:")
series = df["CONTRIBUTING FACTOR VEHICLE 3"]
with ProgressBar():
       print(series.describe().compute())
       
print()
print("Aggregate for ZIP CODE:")
series = df["ZIP CODE"]
with ProgressBar():
       print(series.describe().compute())
