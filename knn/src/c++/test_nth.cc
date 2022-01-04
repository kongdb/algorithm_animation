#include <vector>
#include <iostream>

using namespace std;

using Itr = vector<int>::iterator;

void _nth_element(Itr first, Itr nth, Itr last) {
    if(last - first <= 1)
        return;
    auto leLast = first;
    int pivot = *first;
    for(auto itr = first + 1; itr < last; ++itr)
        if(*itr <= pivot)
            swap(*++leLast, *itr);
    swap(*leLast, *first);
    if(leLast > nth)
        _nth_element(first, nth, leLast);
    else if(leLast < nth)
        _nth_element(leLast + 1, nth, last);
}

bool Compare(int a, int b) { return a > b; }
using Cmp = decltype(Compare);

void _nth_element(Itr first, Itr nth, Itr last, Cmp cmp) {
    if(last - first <= 1)
        return;
    auto leLast = first;
    int pivot = *first;
    for(auto itr = first + 1; itr < last; ++itr)
        if(cmp(*itr, pivot))
            swap(*++leLast, *itr);
    swap(*leLast, *first);
    if(leLast > nth)
        _nth_element(first, nth, leLast, cmp);
    else if(leLast < nth)
        _nth_element(leLast + 1, nth, last, cmp);
}

void printVector(const vector<int> &array) {
    for(auto &i : array)
        cout<< i<< " ";
    cout<< endl;
}

int main()
{
    vector<int> array{3, 1, 2, 4, 7, 6};
    _nth_element(array.begin(), array.begin() + 0, array.end(), Compare);
    printVector(array);
    return 0;
}
