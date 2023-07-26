import sys
sys.path.append(r"../../../simulation_support/python")

import axis_tb



import cocotb
from cocotb.triggers import Timer

from cocotb.clock import Clock
from cocotb.runner import get_runner
from cocotb.triggers import RisingEdge 

@cocotb.test()
async def axis_pipe_tb(dut):
    """Try accessing the design."""

    clock = Clock(dut.clk, 10, units="ns")  # Create a 10us period clock on port clk0
  
    cocotb.start_soon(clock.start())  # Start the clock 
    await RisingEdge(dut.clk)  # Synchronize with the clock0

    for cycle in range(10):
        dut.rst.value = 1;
        await RisingEdge(dut.clk)
