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
    double loan, monthlyPayment, annualRate;

    cout << "Enter loan amount > 0" << endl;
    loan = readDouble(0.0, INFINITY);

    cout << "Enter monthly payment > 0" << endl;
    monthlyPayment = readDouble(0.0, INFINITY);

    cout << "Enter annual interest rate (0-100)" << endl;
    annualRate = readDouble(0.0, 100.0);

    double monthlyRate = annualRate / 12 / 100.0;
    double totalInterest = 0.0;
    int months = 0;

    while (loan > 0)
    {
        loan += loan * monthlyRate;
        loan = loan - monthlyPayment;
        if (loan < 0)
        {
            loan = 0;
        }
        totalInterest += loan * monthlyRate;
        months++;
    }

    cout << "Months to pay: " << months << endl;
    cout << "Total interest paid: " << totalInterest << endl;
    return 0;
}
