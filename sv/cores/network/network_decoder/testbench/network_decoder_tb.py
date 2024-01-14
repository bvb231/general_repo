import cocotb
from cocotb.triggers import Timer

from cocotb.clock import Clock
from cocotb.runner import get_runner
from cocotb.triggers import RisingEdge 

#We create this TB object in every test so that all the required functions can be accessed
#from within this class. 
class TB(object):
    #The init method of this class can be used to do some setup like logging etc, start the 
    #toggling of the clock and also initialize the internal to their pre-reset vlaue.
    def __init__(self, dut):
        self.dut = dut
        clock = Clock(dut.CLK, 10, units="ns")  # Create a 10us period clock on port clk0
        cocotb.start_soon(clock.start())  # Start the clock 		
        #cocotb.fork(self.cycle_reset(dut))


    async def cycle_reset(self):
        await RisingEdge(self.dut.CLK)  # Synchronize with the clock0
        self.dut.RST.value = 1
        for cycle in range(10):
            await RisingEdge(self.dut.CLK)
        self.dut.RST.value = 0





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

