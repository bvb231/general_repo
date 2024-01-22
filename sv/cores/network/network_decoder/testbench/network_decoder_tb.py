import cocotb
from cocotb.triggers import Timer

from cocotb.clock import Clock
from cocotb.runner import get_runner
from cocotb.triggers import RisingEdge 
from scapy.all import * 
from bitstring import BitArray

import sys

#Importing User Libraries 
sys.path.insert(0,"network_decoder_tb")
#We import the big file that holds all of the imports for us
from import_list import *


@cocotb.test()
async def smoke_test(dut):
    """Try accessing the design."""

    #creating a testbench object for this dut. __init__ function is run automatically
    #By having this, we effectively has some sort of "setup" functionality within COCO-TB
    tb = TB(dut)
    driver = Packet_bus_diver(dut.CLK, dut.RST, dut.i_valid, dut.i_sop,dut.i_eop, dut.i_data,dut.i_ebp,dut.i_byte_cnt)

    #Becuase the cycle reset function is async, we need the await keyword for it
    await tb.cycle_reset()
 
    
    for cycle in range(10):
      await RisingEdge(dut.CLK)
    

    packet = Ether(src='aa:bb:cc:dd:ee:ff', dst='88:11:22:33:44:55')/IP(dst='8.8.8.8')/UDP(dport=123)


    #Raw converts the packet to a byte array
    test = bytearray(raw(packet))
    
    test_frame = Packet_bus_frame(test)
    await driver.drive_to_bus(test_frame)
    foo = test.hex()
    print(foo)

    bar = test[0:16].hex()
    print(bar)


    bar = test[8:16].hex()
    print(bar)

    test = int.from_bytes(test[0:16], "big")
    print(test)
    #dut.i_data.value = test
    await RisingEdge(dut.CLK)
        
#    dut._log.info("my_signal_1 is %s", dut.count.value)

