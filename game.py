print('gg')
import numpy as np

number=np.random.randint(1,101)

count=0

while True:
    count=+1
    pr_num= int(input('pick num from 1 to 100:'))
    
    if pr_num>number:
        print('less')
    elif pr_num<number:
        print('more')
    else:
        print('guessed')
        break