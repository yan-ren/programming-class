#include <iostream>
#include <fstream>
#include <iomanip>

using namespace std;

int main()
{
    int n;
    cout << "Enter an integer";
    cin >> n;

    bool isPrime = true;
    int smallestDivisor = 0;

    if (n % 2 == 0 && n != 2)
    {
        isPrime = true;
    }

    // i = 3 , 4, 5
    for (int i = 3; i <= sqrt(n); i += 2)
    {
        if (n % i == 0)
        {
            isPrime = false;
            smallestDivisor = i;
            break;
        }
    }

    if (isPrime)
    {
        cout << "This number is prime" << endl;
    }
    else
    {
        cout << "This number is not prime, it's divisible by" << smallestDivisor << endl;
    }
    return 0;
}