#include <iostream>

int main() {
  // using a basic for loop
  int h{3};
  for (int i{0}; i < h; i++) {
    std::cout << i << " ";
  }
  std::cout << "\n";

  // range based for loop
  int arr[] = {1, 2, 3};
  for (int num : arr) {
    std::cout << num << " ";
  }
  std::cout << "\n";

  int choice;

  std::cout << "Menu\n"
            << "1. Add\n"
            << "2. Sub\n"
            << "Enter choice: ";

  std::cin >> choice;

  int a, b;

  std::cout << "\nEnter the numbers: ";
  std::cin >> a >> b;

  switch (choice) {
  case 1:
    std::cout << "\nSum: " << a + b;
    break;
  case 2:
    std::cout << "\nDiff: " << a - b;
    break;
  default:
    std::cout << "\nExiting...";
    break;
  }

  return 0;
}
