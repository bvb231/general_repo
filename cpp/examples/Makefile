CC = gcc
CXX = g++
RM = rm -f
CXXFLAGS = -g


SRCS=hello_world.cpp
OBJS=$(subst .cc, .o,$(SRCS))

all : hello_world 

hello_world: $(OBJS)
	$(CXX)  -o hello_world $(OBJS) 


clean: 
	rm hello_world
