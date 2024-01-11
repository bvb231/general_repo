`timescale 1ns/1ns

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

   initial begin
      if ($test$plusargs("trace") != 0) begin
         $display("[%0t] Tracing to logs/vlt_dump.vcd...\n", $time);
         $dumpfile("logs/vlt_dump.vcd");
         $dumpvars(0,network_engine);
      end
      $display("[%0t] Model running...\n", $time);
   end


endmodule 
