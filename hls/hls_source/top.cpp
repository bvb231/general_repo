#include "top.h"
#include "general_functions.h"

void top(mystream& A, mystream& B) {
#pragma HLS INTERFACE axis register_mode=off  port = A
#pragma HLS INTERFACE axis register_mode=off port = B

    data_t tmp_a;
	data_t zero;
	zero.data.real(0);
	zero.data.imag(0);

	data_t pipeline[10];
    
	//if(A.read_nb(tmp_a)) {
		A.read(tmp_a);
    	B.write(tmp_a);
    	for(int i=0;i<5;i++){
			#pragma HLS PIPELINE style=frp
    		B.write(zero);
    	}


}
