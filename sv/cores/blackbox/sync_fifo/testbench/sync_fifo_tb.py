import cocotb
import random 

from cocotb.clock import Clock
from cocotb.runner import get_runner
from cocotb.triggers import RisingEdge 

from cocotbext.axi import AxiStreamBus
from cocotbext.axi import AxiStreamSource
from cocotbext.axi import AxiStreamSink

@cocotb.test()

async def run_test(dut):
    clock = Clock(dut.clk, 10, units="us")  # Create a 10us period clock on port clk

    axis_source = AxiStreamSource(AxiStreamBus.from_prefix(dut, "s_axis"), dut.clk, dut.rst)
    axis_sink = AxiStreamSink(AxiStreamBus.from_prefix(dut, "m_axis"), dut.clk, dut.rst)
    

    cocotb.start_soon(clock.start())  # Start the clock 
    await RisingEdge(dut.clk)

    for cycle in range(10):
      dut.rst.value = 1;
      await RisingEdge(dut.clk)

    dut.rst.value = 0;
    await RisingEdge(dut.clk)

    data = [0x09,0x00, 0x00, 0x00, 0x01,0x01,0x55,0xaa,0x12,0x34]
    #await cocotb.start(axis_source.send(data))
    await axis_source.send(data)
    #await axis_source.wait()
    axis_sink.wait()
    foo  = await axis_sink.recv()
    print(foo.tdata)
    if foo.tdata == data :
      print("huzza")
  
    #drive_data(clk, data);





def generate_data_set
  data_set[][];
  random.randint(2,200)

  return data_set
  


# @cocotb.coroutine
# def drive_data (clk, signal, data):
#   await axis_source.send(data)


