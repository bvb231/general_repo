import cocotb

from cocotb.clock import Clock
from cocotb.runner import get_runner
from cocotb.triggers import RisingEdge 


async def reset_dut(reset_n, duration_ns):
  reset_n.value = 0
  await cocotb.triggers.Timer(duration_ns, units="ns")
  reset_n.value = 1



@cocotb.test()
async def parallel_example(dut):
  #clock = Clock(dut.clk, 10, units="ns")  # Create a 10us period clock on port clk
  reset_n = dut.rst_n

  
  #This is a blocking mechanism. This will halt simulation, jump
  #into this function, then return
  #await reset_dut(reset_n,500)
  
  # Run reset_dut concurrently
  # Spin up a thread, execute and keep walking 
  #reset_thread = cocotb.start_soon(reset_dut(reset_n, duration_ns=500))



  await cocotb.triggers.Timer(740,units="ns")

