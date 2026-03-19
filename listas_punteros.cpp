#include<iostream>

using namespace std;

#define N 2

int main() {
  int matriz[N][N] = {
    {1, 2},
    {3, 4}
  };

  int *y = &matriz[0][0]; 
  
  for (int i = 0; i < N; i++) {
    for (int j = 0; j < N; j++){
      cout << *(y + i*N + j) << endl;
    }
  }
}
