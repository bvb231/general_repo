# *****************************************************
# Variables to control Makefile operation
#Compiler of choice 
CC = g++
CFLAGS = -Wall
CFLAGS += -g
# ****************************************************
#Other make file related stuff
TOPDIR := .

# ****************************************************
# Targets needed to bring the executable up to date

TARGET = main

all: $(TARGET)

#TODO: I want to link something within a subdirectory

main: main.cpp test/doPrint.cpp
	$(CC) $(CFLAGS) -o main_build main.cpp test/doPrint.cpp
	#$(CC) $(CFLAGS)  -o test main.cpp doPrint.cpp -I.

