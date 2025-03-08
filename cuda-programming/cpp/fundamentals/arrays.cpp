#include <iostream>
#include <vector>
using namespace std;

int main() {

  vector<int> arr = {1, 2, 3, 4, 5, 6};

  int sum = 0;

  for (int num : arr) {
    sum += num;
  }

  double avg = static_cast<double>(sum) / arr.size();

  cout << "Average: " << avg << endl;
}
