#include<iostream>

using namespace std;

// Esta es la manera C de escribirlo
void funcion(int *valor){
  *valor = 15;
}

// Manera más moderna de escribirlo
void funcion2 (int &valor) {
  valor = 20;
}

int main() {
  int x = 10;
  int *y = &x;
  
  // dereferencia
  cout << y << endl;
  funcion(&x);
  cout << "Utilizando int*" << endl;
  cout << x << endl;
  funcion2(x);
  cout << "Utilizando int&" << endl;
  cout << x << endl;
  return 0;
}
