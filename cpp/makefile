# *****************************************************
# Variables to control Makefile operation
#Compiler of choice 
CC = g++
CFLAGS = -Wall
CFLAGS += -g
# ****************************************************
# Targets needed to bring the executable up to date
$INCLUDES = -I.

all: TARGET

#My final executable
TARGET: main.o doPrint.o
	$(CC) -o game main.o doPrint.o	

main.o: main.cpp 
	$(CC) $(CFLAGS) -c main.cpp 

doPrint.o: test/doPrint.cpp
	$(CC) $(CFLAGS) -c test/doPrint.cpp


clean: 
	rm -f game *.o
