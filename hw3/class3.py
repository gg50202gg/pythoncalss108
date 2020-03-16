print("九九乘法表.......\n")

for i in range(1, 10):
    print("%d  ..." % (i), end="\t")
print("")

for i in range(1, 10):
    for j in range(1, 10):
        print("%dx%d=%d" % (j, i, i*j), end="\t")
    print("")


print("\n執行完畢...\n")
