//
// This is example code from Chapter 2.2 "The classic first program" of
// "Programming -- Principles and Practice Using C++" by Bjarne Stroustrup
//
// This program outputs the message "Hello, World!" to the monitor

#include "other.h"
#include "std_lib_facilities.h"
//------------------------------------------------------------------------------'

// C++ programs start by executing the function main
int main() {
    cout << "Hello from main!" << endl;
    messageFromOtherFile();
    return 0;
}

//------------------------------------------------------------------------------
