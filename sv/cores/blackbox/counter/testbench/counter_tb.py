import cocotb
from cocotb.triggers import Timer

from cocotb.clock import Clock
from cocotb.runner import get_runner
from cocotb.triggers import RisingEdge 

@cocotb.test()
async def my_first_test(dut):
    """Try accessing the design."""

    clock = Clock(dut.clock, 10, units="ns")  # Create a 10us period clock on port clk0
  
    cocotb.start_soon(clock.start())  # Start the clock 
    await RisingEdge(dut.clock)  # Synchronize with the clock0


    dut.reset.value = 1
    for cycle in range(10):
      await RisingEdge(dut.clock)


    dut.reset.value = 0
    
    for cycle in range(10):
      await RisingEdge(dut.clock)
    
    dut._log.info("my_signal_1 is %s", dut.count.value)

