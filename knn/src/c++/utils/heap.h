#ifndef HEAP_H
#define HEAP_H

#include "utils.h"

class Heap
{
public:
    Heap() {};
    explicit Heap(const vector<int> &array);
    void push(int val);
    int pop();
private:
    vector<int> heap;
    void buildHeap();
    void percolateDown(int hole);
    void percolateUp(int hole);
};

#endif
