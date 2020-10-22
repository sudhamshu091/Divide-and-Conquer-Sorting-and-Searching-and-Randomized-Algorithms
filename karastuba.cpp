#include <string>
#include <iostream>
using namespace std;
int karastuba(int X, int Y)
{
    string x = to_string(X);
    string y = to_string(Y);
    int result = 0;


    for (int i = 0; i < y.length(); i++)
    {
        int carry = 0;
        string temp = "";


        for (int j = x.length() - 1; j >= 0; j--)
        {

            int num = (y[i] - '0') * (x[j] - '0') + carry;

            if (num > 9 && j > 0)
            {
                temp = to_string(num % 10) + temp;
                carry = num / 10;
            }

            else
            {
                temp = to_string(num) + temp;
                carry = 0;
            }
        }


        result *= 10;
        result += stoi(temp);
    }
    return result;
}
int main()
{
    cout << karastuba(3141592653589793238462643383279502884197169399375105820974944592,2718281828459045235360287471352662497757247093699959574966967627);
}
