def convertion(bnum):
    dnum=0
    i = 1
    while bnum!=0:
        rem = bnum%10
        dnum = dnum + rem*i
        i = i*2
        bnum = int(bnum/10)
    return dnum
a=int(input("Enter the Binary Number: "))
convertion(a)
