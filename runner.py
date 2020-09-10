if __name__ == '__main__':
    n = int(input())
    lst = input().split()

maxi = -99999999999999999
for i in lst:
    if int(i) > maxi:
        maxi = int(i)

ess = 3
while ess == 3:
    maxi = maxi-1
    if str(maxi) in lst:
        print(maxi)
        ess = 0
