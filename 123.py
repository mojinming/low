c=1
while c==1:
    a=int(input("请输入次数"))
    for b in range(a):
        if b % 7 ==0 or b%10==7:
            continue
        print(b)
    c==input("继续请按“1”,结速请按“2”")