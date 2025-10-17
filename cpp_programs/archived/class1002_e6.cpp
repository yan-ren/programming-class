#include <iostream>
#include <fstream>
#include <string>
using namespace std;

struct Word
{
    string mot;
    string nature;
    string definition;
};

int main()
{
    int N = 50; // assume max dictionary size, can be changed
    Word dict[N];
    int count = 0;

    ifstream file("dictionnaire.txt");
    while (count < N)
    {
        getline(file, dict[count].mot, '\t');
        getline(file, dict[count].nature, '\t');
        getline(file, dict[count].definition);
        count++;
    }

    // similiar problem: given an array of string, find the longest string from it
    int longestIndex = 0;
    for (int i = 0; i < count; i++)
    {
        if (dict[i].mot.size() > dict[longestIndex].mot.size())
        {
            longestIndex = i;
        }
    }

    cout << dict[longestIndex].mot << " " << dict[longestIndex].nature << " " << dict[longestIndex].definition << endl;

    return 0;
}
