#include <stdio.h>

#include <stdlib.h>

float media(float v[], int n)

{
  int i;
  float suma = 0;
  for (i = 0; i < n; i++)
    suma += v[i];
  return suma / n;
}

int main() {
  int i;
  int n;
  float *v;
  printf("Número de elementos del vector: ");
  scanf("%d", &n);
  // Creación del vector
  
  v = new float(n);

  // Manejo del vector
  for (i = 0; i < n; i++)
    v[i] = i;

  printf("Media = %f\n", media(v, n));
  // Liberación de memoria

  free(v);
  return 0;
}
