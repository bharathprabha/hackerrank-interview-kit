
#include <iostream>
using namespace std;

class Empty
{
private:
    /* data */
public:
    Empty(/* args */);
    ~Empty();
};

Empty::Empty(/* args */)
{
}

Empty::~Empty()
{
}
int main()
{
    cout << sizeof(Empty);
}