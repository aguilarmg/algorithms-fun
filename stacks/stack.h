#ifndef Stack_H
#define Stack_H

// Define a default capacity of the stack
#define SIZE 10

// A class to represent a stack
class Stack 
{
    int *arr;
    int top;
    int capacity;

    public:
    Stack(int size=SIZE);   // constructor
    ~Stack();               // destructor
    
    void push(int);
    int pop();
    int peek();

    int size();
    bool isEmpty();
    bool isFull();
};

#endif
