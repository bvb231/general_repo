module mac_phy (
    input logic CLK,
    input logic RST,
    /*
        TX AND RX are both are @ 125 MHz
    */
    output logic [7:0] TX_D,
    output logic TX_EN,
    output logic TX_ERR,
    output logic TX_CLK,


    input logic RX_CLK_EN,
    input logic RX_MII_SEL,
    input logic [7:0] RX_D,
    input logic RX_EN,
    input logic RX_ERR,
    input logic RX_CLK
);


  /*TX FIFO Interface*/

  /*RX FIFO Interface*/

  gmii_rx RX_MODULE (
      .CLK(RX_CLK),
      .RST(RST),

      .RX_D  (RX_D),
      .RX_EN (RX_EN),
      .RX_ERR(RX_ERR),

      .o_valid(),
      .o_data(),
      .o_byte_cnt()
  );




  // TX Datapath








  //RX Datapath





endmodule
