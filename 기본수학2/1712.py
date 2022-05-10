#손익분기점

a,b,c = map(int, input().split(' '))

pc = 1
cnt = 0
while True:
    total = a+b*pc
    money = c*pc


    if b > c or b == c:
        print(-1)
        break

    elif total < money:
        print(pc)
        break

    elif cnt == 0:
        cnt =1
        pc = int(a/(c-b))

    pc += 1