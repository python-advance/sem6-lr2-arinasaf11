import threading
import numpy as np

def multi(matrix1, matrix2, n):
  """
  функция выполняет произведение двух квадратных матриц произвольной размерности
  """
  matrix3 = np.zeros((n,n)) #создаем массив nхn с нулями
  lst = []
  for i in range(n):
    for j in range(n):
      row = matrix1[i] #берем i-ю строку
      col = matrix2[j] #берем j-й столбец
      elem = sum([a*b for a,b in zip(row,col)]) #переумножаем строку на столбец и складываем - получается i,j элемент новой матрицы
      matrix3[i][j]=elem 
  return matrix3

if __name__ == "__main__":
  X = int(input("Введите размерность квадратных матриц: "))
  A = np.random.randint(10, size=(X,X))
  print(A, "\n")
  B = np.random.randint(10, size=(X,X))
  print(B, "\n")

  threading.Thread(target=lambda a, b, n:print(multi(a,b,n)),args=(A, B, X)).start() #используем lambda-функцию для вывода матрицы на экран
