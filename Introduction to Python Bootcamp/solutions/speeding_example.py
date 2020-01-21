# Speeding Example 
# Solution Code for Speeding Example from Intro to Python
# August 28, 2019 - Matthew Garton

# import pandas package
import pandas as pd

# read in data as DataFrame
df = pd.read_csv(
     "https://vincentarelbundock.github.io/Rdatasets/csv/boot/amis.csv", 
     usecols=range(1,5))

# create lists to store before and after data
before = []
after = []

# populate before and after by looping through df
for row in df.values:
    if row[3] == 7:
        if row[2] == 1:
            if row[1] == 1:
                before.append(row[0])
            if row[1] == 3:
                after.append(row[0])

# print results
print("Average before signs: ", sum(before)/len(before))
print("Average after signs: ", sum(after)/len(after))
