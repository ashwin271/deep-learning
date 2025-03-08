#include <iostream>

int main() {

  int a{10}, b{3};

  int sum = a + b;

  int x{5};
  x += 3;

  int y{x++};

  bool result{(a > b) && (x != y)};

  int max{(a > b) ? a : b};

  std::cout << "a:" << a << "\n"
            << "b:" << b << "\n"
            << "x:" << x << "\n"
            << "y:" << y << "\n"
            << "result:" << result << "\n"
            << "max:" << max;
  return 0;
}
