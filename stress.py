import time

pressure = input("Enter Pressure :  ")

count = "1000"

for e in range(int(pressure)):
    count = count + "0"

tic = time.perf_counter()
for e in range(int(count)):
    print(e)
    
toc = time.perf_counter()
print(f"Done in :: {toc - tic:0.4f} seconds")
