module counter
( 
    input clock,
    input reset,
    output reg [3:0]  count
);


`ifdef COCOTB_SIM
   initial begin
      $dumpfile("unit_test.vcd");
      $dumpvars(0,counter);
      #1;
   end
`endif








always @(posedge clock) begin 
   if(reset) begin 
      count <= '0;
   end else begin 
      count <= count + 1;
   end
end

endmodule 
