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
	input s_axis_tvalid,
	output reg s_axis_tready,
	input [P_DATA_WIDTH-1:0] s_axis_tdata,
	input s_axis_tlast,
	
   //
	output reg m_axis_tvalid,
	input m_axis_tready,
	output reg [P_DATA_WIDTH-1:0] m_axis_tdata,
	output reg m_axis_tlast
);

`ifdef COCOTB_SIM
   initial begin
      $dumpfile("unit_test.vcd");
      $dumpvars(0,sync_fifo);
      #1;
   end
`endif

wire input_valid;
reg output_valid;


assign input_valid = s_axis_tvalid & s_axis_tready;

//FIFO Logic 
reg [$clog2(P_FIFO_DEPTH)-1:0]   write_pointer;
reg [$clog2(P_FIFO_DEPTH)-1:0]   read_pointer;
reg [$clog2(P_FIFO_DEPTH)-1:0]   fill_level;
reg [P_DATA_WIDTH:0] ram [P_FIFO_DEPTH-1:0];

//Input flow management. 
always@(posedge clk) begin 
   if(fill_level == P_FIFO_DEPTH-1) begin 
      s_axis_tready <= 1'b0;
   end else begin 
      s_axis_tready <= 1'b1; 
   end
end

//output flow management
always@(posedge clk) begin 
   if(rst) begin 
      m_axis_tvalid <= 1'b0;
   end else begin 
      if(fill_level == 0) begin 
         m_axis_tvalid <= 1'b0;
      end else if(fill_level == 1 && !input_valid && output_valid) begin 
         m_axis_tvalid <= 1'b0; 
      end else begin 
         m_axis_tvalid <= 1'b1; 
      end
   end
end

//assign m_axis_tvalid = (fill_level == 0) ? 1'b0 : 1'b1;

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
         if(fill_level !=  0) begin
            fill_level <= fill_level - 1;
         end
      end
   end
end


always@(posedge clk) begin 
   if(rst) begin 
      write_pointer <= '0;
   end else begin
      if(input_valid) begin 
			ram[write_pointer] <= {s_axis_tdata,s_axis_tlast};
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
		{m_axis_tdata,m_axis_tlast} <= ram[read_pointer];
      if(output_valid) begin 
		   {m_axis_tdata,m_axis_tlast} <= ram[read_pointer+1];
         if(read_pointer == P_FIFO_DEPTH-1) begin 
            read_pointer <= '0;
         end else begin
            read_pointer <= read_pointer+1;
         end
      end
   end
end

assign output_valid = m_axis_tvalid & m_axis_tready;

endmodule
