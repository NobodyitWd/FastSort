import sys
sys.setrecursionlimit(999999999)
def fastSort(x,y):
    if x % y == 0: # Определим базовый случай.
        return max(x,y)-min(x,y)
    else:
        return fastSort(x%y,y%x) # Определим рекурсивный случай
print("Программа равномерно делит площадь на максимально большие квадратные участки.")
x = input("Введите X:   ")
y = input("Введите Y:   ")
print(fastSort(x,y))