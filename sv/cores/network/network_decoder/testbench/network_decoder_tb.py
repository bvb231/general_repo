import cocotb
from cocotb.triggers import Timer

from cocotb.clock import Clock
from cocotb.runner import get_runner
from cocotb.triggers import RisingEdge 


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
    

    #Becuase the cycle reset function is async, we need the await keyword for it
    await tb.cycle_reset()
 
    
    for cycle in range(10):
      await RisingEdge(dut.CLK)
    
#    dut._log.info("my_signal_1 is %s", dut.count.value)

