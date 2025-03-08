#include <iostream>

int main() {

  int age{25};
  float salary{50000.50};
  bool isEmployed{true};
  char grade{'A'};

  const double TAX_RATE{0.20};

  auto result = age * salary;

  std::cout << "Age: " << age << "\n"
            << "Salary: " << salary << "\n"
            << "Employed: " << isEmployed << "\n"
            << "Grade: " << grade << "\n"
            << "Tax Rate: " << TAX_RATE << "\n"
            << "Result: " << result << "\n";

  return 0;
}
