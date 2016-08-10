CC=g++

CXXFLAGS= -g -Wall -std=c++0x

INCLUDES= -I/../h 

SRCS= init.cpp init_worker_from_file.cpp read_csv.cpp output.cpp core_functions.cpp optimize.cpp main.cpp 
OBJS= $(SRCS:.cpp=.o)
#main_h: main.cpp ../h/init.h ../h/var.h ../h/output.h ../h/init_worker_from_file.h

TARGET= main

all:$(TARGET)

$(TARGET): $(OBJS) 
	$(CC) $(CXXFLAGS) $(INCLUDES) -o $(TARGET) $(OBJS)

clean:
	$(RM) *.o $(TARGET)


.c.o: $(CC) $(CFLAGS) $(INCLUDES) -c $<  -o $@
