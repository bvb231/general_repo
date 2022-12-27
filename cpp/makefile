# *****************************************************
# Variables to control Makefile operation
#Compiler of choice 
CC = g++
CFLAGS = -Wall
CFLAGS += -g
# ****************************************************
#Managing Directories
PROJDIR := $(realpath($(CURDIR))
SOURCEDIR := $(PROJDIR)/sources

DIRS = Folder0 Folder1 Folder2
SOURCEDIRS = $(foreach dir, $(DIRS), $(addprefix $(SOURCEDIR)/, $(dir)))
# ****************************************************
# Targets needed to bring the executable up to date

#My final executable
TARGET = app.exe

all: $(TARGET)

#TODO: I want to link something within a subdirectory

main: main.cpp test/doPrint.cpp
	$(CC) $(CFLAGS) -o main_build main.cpp test/doPrint.cpp
	#$(CC) $(CFLAGS)  -o test main.cpp doPrint.cpp -I.

