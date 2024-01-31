module mac_phy (
    input logic CLK,

    /*
        TX AND RX are both are @ 125 MHz
    */
    output logic [7:0] TX_D,
    output logic TX_EN,
    output logic TX_ERR,
    output logic TX_CLK,

    input logic [7:0] RX_D,
    input logic RX_EN,
    input logic RX_ERR,
    input logic RX_CLK
);


  /*TX FIFO Interface*/

  /*RX FIFO Interface*/




  // TX Datapath








  //RX Datapath





endmodule
