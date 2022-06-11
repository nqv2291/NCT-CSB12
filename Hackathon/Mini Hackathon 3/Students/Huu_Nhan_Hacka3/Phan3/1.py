import os
import random
def map():
    placement = random.randint(1,50)
    print (*map_[0:10], sep=" ")
    print (*map_[11:21], sep=" ")
    print (*map_[21:31], sep=" ")
    print (*map_[31:41], sep=" ")
    print (*map_[40:51], sep=" ")
list = ['P','D','K']
map_ = ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-']
for i in list:
    placement = random.randint(0,49)
    del map_[placement]
    map_.insert(placement, i )
def control():
    a = input("ejd")
    if a == "A":



