#include <iostream>
using namespace std;

double area(double length, double width = 1.0);

void printInfo(double x) { cout << "\nDouble: " << x; }

void printInfo(int x) { cout << "\nIngeger: " << x; }

int main() {

  double a, b;
  cout << "\nEnter the sides: ";
  cin >> a >> b;

  double ar = area(a, b);

  cout << "\nArea: " << ar;

  printInfo(10);
  printInfo(4.5);

  return 0;
}

double area(double length, double width) { return length * width; }
