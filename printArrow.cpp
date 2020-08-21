#include <iostream>

using namespace std;

void rightArrow(int arrow_length)
{
    for (int row = 1; row <= (2 * arrow_length) - 1; row++)
    {
        if (row < arrow_length)
        {
            for (int column = 1; column <= row; column++)
            {
                if (column == row)
                {
                    cout << "*";
                }
                else
                {
                    cout << " ";
                }
            }
            cout << "\n";
        }
        else if (row == arrow_length)
        {
            for (int column = 1; column <= row; column++)
            {
                cout << "*";
            }
            cout << "\n";
        }
        else
        {
            for (int column = 1; column <= (2 * arrow_length) - row; column++)
            {
                if (column == ((2 * arrow_length)) - row)
                {
                    cout << "*";
                }
                else
                {
                    cout << " ";
                }
            }
            cout << "\n";
        }
    }
}

int main()
{
    int arrow_length;
    cout << "Enter the length of arrow: ";
    cin >> arrow_length;
    rightArrow(arrow_length);
}