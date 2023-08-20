import sys
sys.path.append(r"../../../simulation_support/python")

from  axis_tb import axis_source, axis_sink



import cocotb
from cocotb.triggers import Timer

from cocotb.clock import Clock
from cocotb.runner import get_runner
from cocotb.triggers import RisingEdge 
from cocotb.triggers import Join 

import random
import numpy as np

NUM_DATA = 10

@cocotb.test()
async def axis_pipe_tb(dut):
    """Try accessing the design."""
    global NUM_DATA
    clock = Clock(dut.clk, 10, units="ns")  # Create a 10us period clock on port clk0
  
    cocotb.start_soon(clock.start())  # Start the clock 
    await RisingEdge(dut.clk)  # Synchronize with the clock0


    for cycle in range(10):
        dut.rst.value = 1
        await RisingEdge(dut.clk)

    dut.rst.value = 0


    data_in = np.random.randint(0, 255, size=(NUM_DATA), dtype=np.uint8)
    
    task_source = cocotb.start_soon(axis_source(data_in, NUM_DATA)) # Drives values
    task_sink   = cocotb.start_soon(axis_sink(data_in, NUM_DATA)) # Catches values
    
    await Join(task_source)
    await Join(task_sink)
    

    cocotb.log.info("Done")