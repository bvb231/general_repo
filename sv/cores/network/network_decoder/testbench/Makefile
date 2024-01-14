SIM ?= verilator
TOPLEVEL_LANG ?= verilog

VERILOG_SOURCES += $(PWD)/../network_decoder.sv
# use VHDL_SOURCES for VHDL files

# TOPLEVEL is the name of the toplevel module in your Verilog or VHDL file
TOPLEVEL = network_decoder 

# MODULE is the basename of the Python test file
MODULE = network_decoder_tb 

EXTRA_ARGS += --trace 
EXTRA_ARGS += --trace-structs
# include cocotb's make rules to take care of the simulator setup
include $(shell cocotb-config --makefiles)/Makefile.sim
