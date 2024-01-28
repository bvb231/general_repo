import cocotb
from cocotb.triggers import RisingEdge
from cocotb.queue import Queue, QueueFull
import random

# General TODO - There should be a base class that moves all common code around. 


#Having a block comment is a nice to have, but
# it's not something I want to deal with right now.
"""
class Packet_bus_if:
    _signals = ["valid","sop","eop","data"]
    def __init(vail)
"""
class Packet_bus_frame:
     def __init__ (self, tdata=b''):
          self.data = bytearray(tdata)

class Packet_bus_driver:

    #Driver constructor. 
    #Still not fully fleshed out. 
    #Variables needed and why
    #Clock - Passing in the clock will allow for us to synchronize to the testbench
    #Reste - Using global reset
    def __init__(self,clock, reset,valid,sop,eop,data,ebp,byte_count):
        self.queue = Queue()
        #TODO: We will want to have this in some sort of reset function.
        #but for now this is something that can live here. 
        self._runfoo = cocotb.start_soon(self._run())
        self.clock = clock
        self.reset = reset
        self.valid = valid
        self.sop = sop
        self.eop = eop
        self.data = data
        self.ebp = ebp
        self.byte_count = byte_count

    
    async def drive_to_bus(self, obj):
        '''
        Main entrant function that's used to push data to
        the bus
        '''
        await self.queue.put(obj)        
        print("hello world")
        #todo


    async def _run(self):
    
        clock_edge_event = RisingEdge(self.clock)
        #Spin in a cycle
        while True:
            #until we have a synchronoizing event
            await clock_edge_event
            sop_set = 0
            #Default values for the bus
            self.valid.value = 0
            self.sop.value = 0
            self.eop.value = 0
            self.ebp.value = 0
            self.byte_count.value = 0
            #If there's data in the queue for us to process
            # go into the loop.
            if not self.queue.empty():
                print("In _run")
                frame = self.queue.get_nowait()

                #While we still have data within the frame,
                #continue on the sending loop
                while(len(frame.data) != 0):                                        
                    await clock_edge_event
                    
                    if(sop_set == 0):
                        self.sop.value = 1
                        sop_set = 1
                    else:
                        self.sop.value = 0

                    self.valid.value = 1
                    if(len(frame.data)<=16):
                        self.data.value = int.from_bytes(frame.data[0:len(frame.data)],"big")
                        self.byte_count.value = len(frame.data)-1
                        self.eop.value = 1
                        
                        #Here we null the frame data for our next check
                        #TODO - There should be a cleaner way to do this as a whole
                        frame.data = frame.data[len(frame.data):] 
                    else:
                        self.data.value = int.from_bytes(frame.data[0:16],"big")
                        frame.data = frame.data[16:]
                        self.byte_count.value = 15
                    #self.log.info("TX Data Sent: %s", data)            




class packet_bus_sink(self):
    print("packet bus sink, hello world")



class packet_bus_monitor(self):
    print("packet bus monitor, hello world")
