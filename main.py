# #1 задание
k = int(input("Введите левую границу : "))
m = int(input("Введите правую границу : "))
sum = 0
for i in range(k, m + 1):
 sum += pow(i,2)
print("Сумма квадратов = " + str(sum))
# 2 задание
import math
print ("Введите натуральное число N")
n=int(input())
if n>=1:
    for k in range(n+1):
        if math.factorial(k)>n:
            print('Наибольшее K:', k-1)
            break
#3 задание
for i in range(1, 11):
   for j in range(2, 11):
       print(j, '*', i, '=', i * j, end='\t\t')
   print()
   '''
   # 3 задание
   n = int(input())
   for i in range(1, n + 1):
    for j in range(1, n + 1):
     print(i * j, " " * (5 - len(str(i * j))), end=" ")
    print("\n", end="")
   '''
   # 4 задание
text = input("Введите символы")
C = input("Выберите символ")
print(text.count(C))
   #5 задание
s = [int(input("Число:")) for i in range(10)]
s.sort()
print(s)
#7 задание
import math
x=float(input("Введите число"))
y=float(input("Введите число"))
c = float(math.sqrt((x**2+y**2)))
print(c)
#Задание 8
x = int(input("Введите натуральное число: "))
y = int(input("Введите натуральное число: "))
if (x == 0 or y == 0):
   print("x * y = "+ str(0))
else:
    p = 0
    n = abs(y)
    for i in range(1, n + 1):
       p += x
       if y < 0:
            p = -p
    print("x * y ="+ str(p))
#9 Задание
def func(n):
    print(int(n, base=2))
if __name__ == '__main__':
    n=input("Введите двоичное число")
    func(n)
#9 задание
print(int(input("Введите двоичное число:"), base=2))

