# *****************************************************
# Variables to control Makefile operation
#Compiler of choice 
CC = g++
CFLAGS = -Wall -g
#CFLAGS += -g
# ****************************************************
# Targets needed to bring the executable up to date

TARGET = main

all: $(TARGET)


$(TARGET): $(TARGET).cpp 
	$(CC) $(CFLAGS) -o $(TARGET) $(TARGET).cpp

clean: 
	$(RM) $(TARGET) 
