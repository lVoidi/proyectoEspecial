#include <iostream>

// #define N 10
#define N 2
using namespace std;

void ejemplo_matriz() {
  int matriz[N][N] = {
    {1, 2}, // 0
    {3, 4}, // 1
  // 0  1
  };

  for (int i = 0; i < N; i++){
    for (int j = 0; j < N; j++){
      cout << matriz[i][j] << endl;
    }
  }

}

int main() {
  ejemplo_matriz();
}
