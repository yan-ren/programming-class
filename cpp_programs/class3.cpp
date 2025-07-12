#include <iostream>
#include <string>

using namespace std;

/*
control flow:
- conditional
    - if statement
    -
- loop

boolean operator
&& and -> one false, overall is false
|| or -> one true, overall is true
! not

true && true -> true
true && false -> false
false && true -> false
false && false -> false

true || true -> true
true || false -> true
false || true -> true
false || false -> false

*/
int main()
{
    // int a = 3;
    // if (a > 0)
    // {
    //     cout << "Positive" << endl;
    // }
    // else if (a < 0)
    // {
    //     cout << "Negative" << endl;
    // }
    // else
    // {
    //     cout << "Zero" << endl;
    // }

    // int grades = 84;
    // if (grades >= 90)
    // {
    //     cout << "A" << endl;
    // }
    // // 80 <= grade < 90
    // // grade < 80 or grade > 90
    // else if (80 <= grades && grades < 90)
    // {
    //     cout << "B" << endl;
    // }
    // else if (70 <= grades && grades < 80)
    // {
    //     cout << "C" << endl;
    // }
    // else
    // {
    //     cout << "D" << endl;
    // }

    int number = 20;

    // logical error
    if (number > 1)
    {
        cout << "Number is bigger than 1" << endl;
    }
    else if (number > 10)
    {
        cout << "Number is bigger than 10" << endl;
    }
    else if (number > 100)
    {
        cout << "Number is bigger than 100" << endl;
    }

    // fix
    if (number > 100)
    {
        cout << "Number is bigger than 100" << endl;
    }
    else if (number > 10)
    {
        cout << "Number is bigger than 10 Number is bigger than 1" << endl;
    }
    else if (number > 1)
    {
        cout << "Number is bigger than 1" << endl;
    }

    // int a, b;
    // cin >> a;
    // cin >> b;

    // if (a > b)
    // {
    // }
    // else if (a < b)
    // {
    // }
    // else
    // {
    // }

    // int a = 3;
    // int b = 4;
    // cout << a % b << endl;

    // if (a % 2 == 0) {

    // }else if (a % 2 != 0) {

    // }

    int a, b, c;
    // find the largest number out of three numbers

    return 0;
}