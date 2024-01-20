import cocotb
from cocotb.triggers import RisingEdge
from cocotb.queue import Queue, QueueFull
import random


#Having aa block comment is a nice to have, but
# it's not something I want to deal with right now.
"""
class Packet_bus_if:
    _signals = ["valid","sop","eop","data"]
    def __init(vail)
"""
class Packet_bus_frame:
     def __init__ (self, tdata=b''):
          self.data = bytearray(tdata)

class Packet_bus_diver:

    #Driver constructor. 
    #Still not fully fleshed out. 
    #Variables needed and why
    #Clock - Passing in the clock will allow for us to synchronize to the testbench
    #Reste - Using global reset
    def __init__(self,clock, reset,valid,sop,eop,data,ebp,byte_count):
        self.queue = Queue()
        #TODO: We will want to have this in some sort of reset function.
        #but for now this is something that can live here. 
        self._run = cocotb.start_soon(self._run())
        self.clock = clock
        self.reset = reset
        self.valid = valid
        self.sop = sop
        self.eop = eop
        self.data = data
        self.ebp = ebp
        self.byte_count = byte_count


    async def _run(self):
    
        clock_edge_event = RisingEdge(self.clock)
        #Spin in a cycle
        while True:
            #until we have a synchronoizing event
            await clock_edge_event
            #If there's data in the queue for us to process
            # go into the loop.
            if not self.queue.empty():
                frame = self.queue.get_nowait()
                data = len(frame.data)
                self.log.info("TX Data Sent: %s", data)            
