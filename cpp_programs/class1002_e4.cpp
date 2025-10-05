#include <iostream>
#include <cstdlib>
#include <ctime>
#include <cmath>
#include <iomanip>
using namespace std;

// generate a random number between -1 to 1
double randRange()
{
    return -1.0 + (2.0 * rand()) / (double)RAND_MAX; // cmath
}

int main()
{
    srand(time(0)); // use timestamp as seed
    // cout << randRange() << endl;
    int iterations;
    cout << "Enter number of iterations: ";
    cin >> iterations;

    int insideCircle = 0;
    for (int i = 0; i < iterations; i++)
    {
        double x = randRange();
        double y = randRange();
        if (x * x + y * y < 1.0)
        {
            insideCircle++;
        }
    }

    double p = 4.0 * (double)insideCircle / (double)iterations;

    cout << "Approximation of pi " << p << endl;

    double realP = 3.141593;
    double error = fabs(p - realP) / realP;

    cout << "Error: " << fixed << setprecision(6) << error << endl;
    return 0;
}
