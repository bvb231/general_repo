#include "top.h"

int main(){

	data_t A,B;

	A.data.real(5);
	A.data.imag(5);


	mystream A_in,B_out;

	for(int i=0;i<100;i++){
		A_in.write(A);
		top(A_in,B_out);
		B_out.read();
	}
}
