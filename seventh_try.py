#判断一个数n能同时被3和5整除
n = int(input())
if n % 3 == 0 and n % 5 == 0 :
    print("yes")
else:
    print("no")