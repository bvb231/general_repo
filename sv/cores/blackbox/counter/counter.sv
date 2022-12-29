module counter
( 
    input clock,
    input reset,
    output reg [3:0]  count
);


always @(posedge clock) begin 
   if(reset) begin 
      count <= '0;
   end else begin 
      count <= count + 1;
   end
end

endmodule 
