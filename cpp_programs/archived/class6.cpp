#include <iostream>
#include <string>
#include <array>
#include <cmath>

using namespace std;

int main()
{
    int marks[5]; // int marks[5]{} initializea array with length 5 with default values 0, int marks[5] declares an array without initilizing values
    marks[0] = 20;
    // cout << marks[0] << endl;
    // cout << marks[2] << endl;

    // for (int i = 0; i < 5; i++)
    // {
    //     cout << marks[i] << endl;
    // }

    // int numbers[10]{};
    // int numbers[] = {10, 20, 3, 40, 5};

    // for (int i = 0; i < 10; i++)
    // {
    //     numbers[i] = i + 1;
    // }

    // for (int i = 0; i < sizeof(numbers) / sizeof(numbers[0]); i++)
    // {
    //     cout << numbers[i];
    // }

    // C++11
    array<int, 5> numbers = {-10, -20, -3, -40, -5};
    // for (int i = 0; i < numbers.size(); i++)
    // {
    //     cout << numbers[i] << endl;
    // }
    int sum = 0;
    for (int num : numbers)
    {
        sum += num;
    }

    // example: find the largest value inside array
    int max = numbers[0];
    for (int num : numbers)
    {
        if (num > max)
        {
            max = num;
        }
    }
    cout << max << endl;

    // exercise: given an array of numbers, count how many positive inside

    // exercise: create an array using loop with following {1, 4, 9, 16, 25, 36, 49, 64, 81}
    int arr[9];

    for (int i = 0; i < 9; i++)
    {
        arr[i] = (i + 1) * (i + 1);
    }
    double result = pow(2.0, 3.0);

    return 0;
}