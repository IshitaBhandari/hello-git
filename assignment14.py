#Question 1: Write a python program to read last n lines of a file.

file='test.txt'
with open(file,'r')as f:
    lines=f.readlines()

n=2
for i in range(len(lines)-n,len(lines)):
    print(lines[i])
#2
from collections import Counter
def word_count(fname):
        with open(fname) as f:
                return Counter(f.read().split())

print("Number of words in the file :",word_count("test.txt"))
#3
from shutil import copyfile
copyfile('test.txt', 'copied.txt')

#Question 4: Write a Python program to combine each line from first file with the corresponding line in second file.
with open('test.txt') as fh1, open('copied.txt') as fh2:
    for line1, line2 in zip(fh1, fh2):
        # line1 from sample.txt, line2 from copied.txt
        print(line1+line2)

#Write a Python program to write 10 random numbers into a file. Read the file and then sort the numbers and then store it to another file.
import random
from operator import itemgetter

randfile = open("Random.txt", "w" )

for i in range(int(input('How many to generate?: '))):
    line = str(random.randint(1, 10))+ ","
    randfile.write(line)
    print(line)

with open('Random.txt','r') as f:
    list = []
    for line in f:
        line = line.split() # to deal with blank
        if line:            # lines (ie skip them)
            line = [int(i) for i in line]
            list.append(line)

data=[]
with open('Random.txt','r')as f:
        data=sorted(map(int,f.readline().split(',')))
print(data)
