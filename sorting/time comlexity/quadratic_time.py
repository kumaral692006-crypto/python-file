def quadratic_time(n):
    print("\nO(n^2)-quadratic time example")

    for i in range(n):
        for j in range(n):
            print(f"({i},{j})",end=" ")

n=int(input('enter value of n:'))
quadratic_time(n)