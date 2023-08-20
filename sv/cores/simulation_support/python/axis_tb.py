import cocotb
from cocotb.triggers import RisingEdge
import random


'''
Signal Driver
'''

async def axis_source(data, NUM_DATA, VALID_PROB=0.5):
    dut = cocotb.top

    def reset():
        dut.s_axis_tvalid.value = 0
        dut.s_axis_tdata.value = 0 
        # = dut.s_axis_tlast.value = 0
    reset()


    i_data, i_clk = 0,0

    while True: 
        if i_data == NUM_DATA:
            break
       
        valid = random.choices([0,1], [1-VALID_PROB, VALID_PROB])[0]
        dut.s_axis_tvalid.value = valid

        if valid: 
            dut.s_axis_tvalid.value = valid
            dut.s_axis_tdata.value = int(data[i_data])

            #if i_data == NUM_DATA-1:
            #    dut.s_axis_tlast.value = 1
            if dut.s_axis_tvalid.value == 1 and dut.s_axis_tready.value == 1:
                i_data += 1
    
        await RisingEdge(dut.clk)
        i_clk += 1
    reset()


    '''
    Signal Monitor
    '''


async def axis_sink(data, NUM_DATA, READY_PROB=0.5):
        
    dut = cocotb.top
    dut.m_axis_tready.value = 1
        
    NUM_DATA = len(data)
    i_data, i_clk = 0,0


    while True: 
        if i_data == NUM_DATA: 
            break

        ready = random.choices([0,1], [1-READY_PROB, READY_PROB])[0]
        dut.m_axis_tready.value = ready

        await RisingEdge(dut.clk)
        i_clk += 1

        #if ready and dut.m_axis_tvalid.value:
        #    assert dut.m_axis_tdata.value == data[i_data], f'AXIS Sink failed at aclk={i_clk}. Expected: {data[i_data]}, received {int(dut.m_data.value)}'
        

        #if i_data == NUM_DATA -1:
        #    assert dut.m_axis_tlast.value == 1 , f'AXIS m_last not received'
        #else : 
        #    assert dut.m_axis_tlast.value == 0, f'AXIS m_last raised at aclk={i_clk}'
        if dut.m_axis_tvalid.value == 1 and dut.m_axis_tready.value == 1:
            i_data += 1
    
    dut.m_axis_tready.value = 0 