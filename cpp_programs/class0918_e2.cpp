#include <iostream>

using namespace std;

int main()
{
    int price, amount;

    cout << "Enter price: ";
    cin >> price;

    cout << "Enter amount given: ";
    cin >> amount;

    bool isEnough = amount >= price;

    cout << "Payment sufficient: " << boolalpha << isEnough << endl;

    if (isEnough)
    {
        int change = amount - price;
        cout << "Change to give:" << endl;
        cout << " 100$ bills" << change / 100 << endl;
        cout << " 20$ bills" << (change % 100) / 20 << endl;
        cout << " 10$ bills" << (change % 20) / 10 << endl;
        cout << " 5$ bills" << (change % 10) / 5 << endl;
        cout << " 1$ bills" << (change % 5) << endl;
    }
}
