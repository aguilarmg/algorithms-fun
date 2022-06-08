#include "stack.h"
#include <iostream>

// Constructor to initialize a stack
Stack::Stack(int size) {
    arr = new int[size];
    capacity = size;
    top = -1;
}

// Destructor to free memory allocated to the stack
Stack::~Stack() {
    delete[] arr;
}

void Stack::push(int x) {
    if (isFull()) {
        std::cout << "Overflow\nProgram Terminated.\n";
        exit(EXIT_FAILURE);
    }

    std::cout << "Inserting " << x << std::endl;
    arr[++top] = x;
}

int Stack::pop() {
    if (isEmpty()) {
        std::cout << "Underflow\nProgram Terminated.\n";
        exit(EXIT_FAILURE);
    }

    std::cout << "Removing " << peek() << std::endl;
    
    // Decrease stack size by 1 and (optionally) return the popped element
    return arr[top--];
}

int Stack::peek() {
    if (!isEmpty()) {
        return arr[top];
    } else {
        exit(EXIT_FAILURE);
    }
}

int Stack::size() {
    return top+1;
}

bool Stack::isEmpty() {
    return top == -1;
}

bool Stack::isFull() {
    return top == capacity - 1;
}
