#include "heap.h"

#include <cassert>

Heap::Heap(const vector<int> &array) : heap(array)
{
    buildHeap();
}

void Heap::buildHeap()
{
    for(int i = heap.size() / 2 - 1; i >= 0; --i)
        percolateDown(i);
}

void Heap::percolateDown(int hole)
{
    int tmp = heap[hole];
    for(int child; hole + 1 <= heap.size() / 2; hole = child)
    {
        child = 2 * hole + 1;
        if(child + 1 < heap.size() && heap[child+1] < heap[child])
            ++child;
        if(heap[child] < tmp)
            heap[hole] = heap[child];
        else
            break;
    }
    heap[hole] = tmp;
}

void Heap::percolateUp(int hole)
{
    int tmp = heap[hole];
    for(int parent; hole > 0; hole = parent)
    {
        parent = (hole - 1) / 2;
        if(heap[parent] > tmp)
            heap[hole] = heap[parent];
        else
            break;
    }
    heap[hole] = tmp;
}

void Heap::push(int val)
{
    heap.push_back(val);
    percolateUp(heap.size() - 1);
}

int Heap::pop()
{
    assert(!heap.empty());
    int result = heap.front();
    heap[0] = heap.back();
    heap.pop_back();
    if(!heap.empty())
        percolateDown(0);
    return result;
}
