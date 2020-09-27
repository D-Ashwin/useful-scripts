from tqdm import tqdm 
from time import sleep


def niceprint(methodnum):
	print("-"*70)
	print(f"Method {methodnum}")


# Method 1
niceprint(1)
for i in tqdm(range(5)):
	sleep(0.2)
print("\n")

# Method 2
niceprint(2)
for i in tqdm(range(0, 100), total = 100, 
              desc ="Progress"): 
    sleep(.1) 
print("\n")

# Method 3 : ncols : width
niceprint(3)
for i in tqdm(range(0, 100), ncols = 70, 
               desc ="Text You Want"): 
    sleep(.1) 

# Method 4 : mininterval
niceprint(4)
for i in tqdm(range(0, 100), mininterval = 3,  
              desc ="Text You Want"): 
    sleep(.1) 


# Method 5 : ascii chars
niceprint(5)
for i in tqdm(range(0, 100),  
              ascii ="|#"): 
    sleep(.1)


# Method 5.1 : ascii chars
niceprint(5.1)
for i in tqdm(range(0, 100),  
              ascii ="*✦"): 
    sleep(.1)