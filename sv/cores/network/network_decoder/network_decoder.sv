/* Network Decoder
 *
 *  Takes in data from the MAC and will attempt to parse out all relevant
 *  information to pass onto specific modules
 *
 *
 *
 *
 */
module network_decoder
(
    input logic CLK, 
    input logic RST,

    //Input bus from MAC
    input logic i_valid,
    input logic [127:0] i_data,
    input logic i_sop, 
    input logic i_eop, 
    input logic i_ebp,
    input logic [5:0] i_byte_cnt,

    output logic [47:0] o_mac_destination,
    output logic [47:0] o_mac_source,
    output logic [15:0] o_ether_type
);


logic [127:0] data_a;
logic [7:0] word_count_a;
logic valid_a;

always_ff@(posedge CLK) begin 
    if(RST) begin 
        word_count_a <= 8'd0;
    end else begin 
        if(i_valid) begin 
            if(i_eop || i_sop) begin 
                word_count_a <= 8'd0;
            end else begin 
                word_count_a <= word_count_a + 8'd1;
            end
        end 
    end
end


always_ff@(posedge CLK) begin 
    data_a <= i_data;
    valid_a <= i_valid;
end

//Note - Currently we do not support any VLANs
always_ff@(posedge CLK) begin 
    o_mac_destination <= data_a[127-:48];
    o_mac_source <= data_a[(127-48)-:48];
    o_ether_type <= data_a[(127-96)-:16];
end



endmodule