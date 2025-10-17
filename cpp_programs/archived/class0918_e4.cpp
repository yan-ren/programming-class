#include <iostream>
#include <fstream>
#include <iomanip>

using namespace std;

int main()
{
    ifstream inFile("ventes.txt");
    ofstream outFile("facture.txt");

    string clientName;
    getline(inFile, clientName);

    string product;
    int quantity;
    double price, subtotal = 0.0;

    for (int i = 0; i < 3; i++)
    {
        inFile >> product >> quantity >> price;
        subtotal = subtotal + quantity * price;
    }

    double taxes = subtotal * 0.15;
    double total = subtotal + taxes;
    outFile << clientName << endl;
    outFile << "SOUS-TOTAL" << setw(10) << fixed << setprecision(2) << subtotal << " $" << endl;
    outFile << "TAXES" << setw(15) << fixed << setprecision(2) << taxes << " $" << endl;
    outFile << "TOTAL" << setw(15) << fixed << setprecision(2) << total << " $" << endl;
    return 0;
}