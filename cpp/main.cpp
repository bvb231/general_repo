#include <iostream>
 
// preferred version
int main()
{
	std::cout << "Enter an integer: ";
 
	int num{ 0 };
	std::cin >> num;
 
	std::cout << "Double that number is: " <<  num * 2 << '\n'; // use an expression to multiply num * 2 at the point where we are going to print it
 
	return 0;
}


// Definition of user-defined function doPrint()
void doPrint() // doPrint() is the called function in this example
{
    std::cout << "In doPrint()\n";
}