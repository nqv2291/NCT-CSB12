#Nát;-;
#(Còn nhiều lỗi nếu thiếu K hoặc D hoặc P thì reset game)
#(W và S có vấn đề)
#(Muốn di chuyển phải cần in hoa chữ đó)

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
map()
def control():
    a = input("Move")
    if a == "W":
        d = map_.index("P")
        del map_[d]
        map_.insert(d, "-" )
        del map_[d - 10]
        map_.insert(d - 10, "P" )
    if a == "D":
        d = map_.index("P")
        del map_[d]
        map_.insert(d, "-" )
        del map_[d + 1]
        map_.insert(d + 1, "P" )
    if a == "A":
        d = map_.index("P")
        del map_[d]
        map_.insert(d, "-" )
        del map_[d - 1]
        map_.insert(d - 1, "P" )
    if a == "S":
        d = map_.index("P")
        del map_[d]
        map_.insert(d, "-" )
        del map_[d + 10]
        map_.insert(d + 10, "P" )
    print (map())
    f = map_.index("K")
while True:
    control()


