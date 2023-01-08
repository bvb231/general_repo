module axis_pipe
#(
   parameter P_DATA_WIDTH = 8;
)
(
	input clk,
	input rst,

	//
   input s_axis_tvalid,
   output reg s_axis_tready,
   input [P_DATA_WIDTH-1:0] s_axis_tdata,

   //
	output reg m_axis_tvalid,
	input m_axis_tready,
	output reg [P_DATA_WIDTH-1:0] m_axis_tdata,
)
reg main_tvalid;
reg [P_DATA_WIDTH-1:0] main_tdata;

reg skid_tvalid;
reg [P_DATA_WIDTH-1:0] skid_tdata;

always @(posedge clk) begin 
   if(rst) begin 
      skid_tvalid <= 1'b0;
      main_tvalid <= 1'b0;
   end else begin 
      if(s_axis_tready) begin
         main_tvalid <= s_axis_tvalid;           
         main_tdata  <= s_axis_tdata;
         if(!m_axis_tready) begin 
            skid_tvalid <=  main_tvalid;
            skid_tdata <= main_tdata;
         end
      end
      
      if(m_axis_tready) begin 
         skid_tvalid <= 1'b0;
      end
   end
end

assign s_axis_tready = !skid_tvalid;

assign m_axis_tvalid = main_tvalid | skid_tvalid;
assign m_axis_tdata = skid_tvalid ? skid_tdata : main_tdata;

endmodule
