#include <iostream>
#include <string>

using namespace std;

int main()
{
    // int num;
    // cout << "Enter an integer:" << endl;
    // cin >> num;
    // cout << "You entered:" << num << endl;
    // char ch = ' ';
    // string message = "Hi World!";
    // double num = 1.0;

    // bool a = 1 > 2;
    // cout << bool(a) << endl;
    string msg = "How old are you?";
    cout << msg << endl;
    int age;
    cin >> age;
    if (age > 18)
    {
        cout << "Adult" << endl;
    }
    else
    {
        cout << "Not Adult" << endl;
    }
    return 0;
}