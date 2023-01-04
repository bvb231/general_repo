/************************************************/
// Sync FIFO 
//
//
//
// General
/************************************************/

module sync_fifo 
#(
	parameter P_DATA_WIDTH = 16,
	parameter P_FIFO_DEPTH  = 16
)
(
	input clk,
	input rst,

	//
	input S_AXIS_T_VALID,
	output reg S_AXIS_T_READY,
	input [P_DATA_WIDTH-1:0] S_AXIS_T_DATA,
	input S_AXIS_T_LAST,
	
   //
	output reg M_AXIS_T_VALID,
	input M_AXIS_T_READY,
	output reg M_AXIS_T_DATA,
	output reg M_AXIS_T_LAST
);

wire input_valid;
reg output_valid;


assign input_valid = S_AXIS_T_VALID & S_AXIS_T_READY;

//FIFO Logic 
reg [$clog2(P_FIFO_DEPTH)-1:0]   write_pointer;
reg [$clog2(P_FIFO_DEPTH)-1:0]   read_pointer;
reg [$clog2(P_FIFO_DEPTH)-1:0]   fill_level;
reg [P_FIFO_DEPTH-1:0] ram [P_FIFO_DEPTH-1:0];

//Input flow management. 
always@(posedge clk) begin 
   if(fill_level == P_FIFO_DEPTH-1) begin 
      S_AXIS_T_READY <= 1'b0;
   end else begin 
      S_AXIS_T_READY <= 1'b1; 
   end
end

//Output flow management
always@(posedge clk) begin 
   if(fill_level == 0) begin 
      M_AXIS_T_VALID <= 1'b0;
   end else begin 
      M_AXIS_T_VALID <= 1'b1; 
   end
end


//Fill Level
always@(posedge clk) begin 
   if(rst) begin 
      fill_level <= '0;
   end else begin
      if(input_valid && output_valid) begin 
      end else if(input_valid && !output_valid) begin 
         write_pointer  <= write_pointer + 1;  
         fill_level <= fill_level + 1;
      end else if(!input_valid && output_valid) begin 
         fill_level <= fill_level - 1;
      end
   end
end

always@(posedge clk) begin 
   if(rst) begin 
      write_pointer <= '0;
      fill_level <= '0;
   end else begin
      if(input_valid) begin 
      end
   end
end

always@(posedge clk) begin 
   if(rst) begin 
      write_pointer <= '0;
   end else begin
      if(input_valid) begin 
         if(write_pointer == P_FIFO_DEPTH-1) begin 
            write_pointer <= '0;
         end else begin
            write_pointer <= write_pointer+1;
         end
      end
   end
end

always@(posedge clk) begin 
   if(rst) begin 
      read_pointer <= '0;
   end else begin
      if(output_valid) begin 
         if(read_pointer == P_FIFO_DEPTH-1) begin 
            read_pointer <= '0;
         end else begin
            read_pointer <= read_pointer+1;
         end
      end
   end
end

assign output_valid = M_AXIS_T_VALID & M_AXIS_T_READY;

endmodule
