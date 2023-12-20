#include <iostream>
#include <stdlib.h>
using namespace std;

int main(int argc, char *argv[])
{
    int i;
    cout << "quelle est la valeur de i? ";
    cin >> i;

    if (i > 10 && i <= 20) {
        cout << "dans l'interval xd !\n";
    }
    else if (i >= 50 && i <= 100) {
        cout << "dans l'interval !\n";
    }
    else {
        cout << "en dehors de l'interval !\n";
    }

    return 0;
}
