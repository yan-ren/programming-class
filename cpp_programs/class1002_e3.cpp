#include <iostream>
#include <fstream>
#include <iomanip>
#include <cmath>

using namespace std;

double readDouble(double minVal, double maxVal)
{
    double value;
    cout << "Enter a value (" << minVal << " to " << maxVal << " ):";
    cin >> value;

    while (value <= minVal || value >= maxVal)
    {
        cout << "Invalid, enter again:" << endl;
        cin >> value;
    }

    return value;
}

int main()
{
    double g = 9.81;
    double h, c;
    int n;

    cout << "Enter initial height > 0" << endl;
    h = readDouble(0, INFINITY);

    cout << "Enter rebound coefficient (0-1)" << endl;
    c = readDouble(0, INFINITY);

    cout << "Enter number of bounces (>0)" << endl;
    n = (int)readDouble(0, INFINITY);

    for (int i = 0; i < n; i++)
    {
        double v = sqrt(2.0 * g * h);
        v = c * v;
        h = (v * v) / (2.0 * g);
    }

    cout << "Height after " << n << " bounces: " << h << endl;

    return 0;
}
