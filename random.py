import random
import pandas as pd
import string

#rows of data
numRows = 10000

#GENERATING COLUMNS
#column 1: random positive integer
column_1 = random.sample(range(0,100000000000000), numRows)
#column 2: random negative integer
column_2 = random.sample(range(-100000000000000,0), numRows)
#column 3: random integer, either positive or negative
column_3 = random.sample(range(-100000000000000,100000000000000), numRows)
#column 4: random ASCII letter
column_4 = [str(random.choice(string.ascii_letters)) for i in range (numRows)]

#assign to dataframe
my_big_data = pd.DataFrame({"col1":column_1, "col2":column_2, "col3":column_3, "col4":column_4})

#write to excel CSV file
my_big_data.to_csv("my_big_data.csv", index=False)
