#include <iostream>
#include <cmath>

using namespace std;

double ln(double x, double precision)
{
    if (x <= 0 || x >= 2)
    {
        cerr << "Invalid number, must be in (0, 2)." << endl;
        exit(1); // program exit with error code 1
    }

    double z = x - 1.0;
    double termPower = z; // (x-1)^n
    int n = 1;
    int sign = 1;
    double sum = 0.0;
    double term = sign * (termPower / n); // compute the first term (x-1)

    while (term > precision || term < -precision)
    {
        sum = sum + term;

        n = n + 1;
        sign = -sign;
        termPower = termPower * z;
        term = sign * (termPower / n);
    }

    return sum;
}

int main()
{
    double precision = 1e-6;

    double test1 = 1.2;
    double result = ln(test1, precision);
    bool ok = fabs(result - log(test1)) < precision;
    cout << boolalpha << ok << endl;

    double test2 = 1.5;
    result = ln(test2, precision);
    ok = fabs(result - log(test2)) < precision;
    cout << boolalpha << ok << endl;

    double test3 = 1.8;
    result = ln(test3, precision);
    ok = fabs(result - log(test3)) < precision;
    cout << boolalpha << ok << endl;

    return 0;
}