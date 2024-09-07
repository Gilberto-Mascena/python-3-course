import numpy as np

matriz_A = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]);

print(matriz_A);
print("\nTransposição de Matrizes");
#Transposição de Matrizes

matriz_T = matriz_A.transpose();
print(matriz_T);

print("\nSoma de Matrizes");

#Soma de Matrizes
matriz_A + matriz_T
print(matriz_A + matriz_T);

print("\nSubtração de Matrizes");

#Subtração de Matrizes
matriz_A - matriz_T
print(matriz_A - matriz_T);

print("\nMultiplicação de Matrizes");
#Multiplicação de Matrizes
np.dot(matriz_A, matriz_T)
print(np.dot(matriz_A, matriz_T));

#Divisão de Matrizes nâo existe.