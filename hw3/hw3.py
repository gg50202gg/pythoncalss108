import math

lists = []

while True:
    number = input("請輸入一個數，如果不是正整數，將停止本程式 ...")
    try:
        if number == str(int(number)):
            if int(number) > 0:
                lists.append(int(number))
            else:
                break
        else:
            break
    except:
        break


print("\n停止輸入...\n")
print(lists)
try:
    print("\nmax = %d ; min = %d\n" % (max(lists), min(lists)))
    for i in range(len(lists)):
        lists[i] += i
    print("將序列依序加上 0,1,2,...的結果\n")
    print(lists)
except:
    pass
