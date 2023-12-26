module network_engine
(
    input logic CLK,
    input logic RST,

    output logic IS_IP
);


	logic [7:0] count;

//IP Detector
   always_ff@(posedge CLK) begin 
      if(RST) begin 
         IS_IP <= 1'b0;
	      count	<= 8'd0;
		end else begin
	      count	<= count+8'd1;
      end
   end


endmodule 
