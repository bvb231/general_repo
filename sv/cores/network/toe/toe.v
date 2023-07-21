//TCP 
//Offload
//Engine

module toe
#(
   parameter P_DATA_WIDTH = 64
)
(
   input clk,
   input rst_n,
   input i_valid,
   output reg i_read,
   input [P_DATA_WIDTH-1:0] i_data,
   

   output reg [P_DATA_WIDTH-1:0] o_data,
   output reg o_en
);

`ifdef COCOTB_SIM
   initial begin
      $dumpfile("unit_test.vcd");
      $dumpvars(0,toe);
      #1;
   end
`endif

reg pipe_ready; 

assign pipe_ready = 1'b1;

always @(posedge clk) begin 
   if(!rst_n) begin 
      i_read <= 1'b0;
   end else begin 
      if(i_valid && pipe_ready) begin 
         i_read <= 1'b1;
      end
   end
end


endmodule
