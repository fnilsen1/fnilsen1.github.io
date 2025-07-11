# Compiler and flags
CXX = g++
CXXFLAGS = -Wall -Wextra -std=c++17

# Source and object files
SRCS = $(wildcard *.cpp)
OBJS = $(SRCS:.cpp=.o)

# Output binary
TARGET = main

# Default target
all: $(TARGET)

# Link object files to create the final binary and delete .o files
$(TARGET): $(OBJS)
	$(CXX) $(CXXFLAGS) -o $@ $^
	@rm -f $(OBJS)

# Clean up manually
clean:
	rm -f $(OBJS) $(TARGET)
