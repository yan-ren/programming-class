#include <iostream>
using namespace std;

int main()
{
    int size = 10;
    int arr[size], result[size];

    cout << "Enter 10 integers:" << endl;
    for (int i = 0; i < size; i++)
    {
        cin >> arr[i];
    }

    int index = 0;
    // loop through array, only for even number
    for (int i = 0; i < size; i++)
    {
        if (arr[i] % 2 == 0)
        {
            result[index] = arr[i];
            index++;
        }
    }

    // loop through array, only for odd number
    for (int i = 0; i < size; i++)
    {
        if (arr[i] % 2 != 0)
        {
            result[index] = arr[i];
            index++;
        }
    }

    cout << "Reulst array: " << endl;
    for (int i = 0; i < size; i++)
    {
        cout << result[i] << " ";
    }

    return 0;
}