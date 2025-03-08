#include <iostream>
using namespace std;

int main() {
  int a{21}, b{5};
  double c = static_cast<double>(a) / b;
  cout << c;
  return 0;
}
