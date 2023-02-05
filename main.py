n = int(input())
total = 0
    if n % 25 == 0:
        total += (n // 25)
        n = n % 25
        while n % 10 == 0:
            total += (n // 10)
            n = n % 10
            while n % 5 == 0:
                total += (n // 5)
                n = n % 5
                total += n
print(total)