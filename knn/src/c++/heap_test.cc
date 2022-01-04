#include <vector>
#include <iostream>
#include <chrono>
#include <algorithm>
#include <climits>
#include <random>
#include <functional>

using namespace std;

static const int k = 3000, COUNT = 1000000;

void print_array(const vector<int> &data) {
    for(int n : data)
        cout<< n<< " ";
    cout<< endl;
}

vector<int> generate_random() {
    std::default_random_engine generator;
    std::uniform_int_distribution<int> distribution(0,INT_MAX);
    vector<int> result(COUNT);
    for(int i = 0; i < COUNT; i++)
        result[i] = distribution(generator);
    return result;
}


void test_directly_sort(vector<int> &data, vector<int> &result) {
    sort(data.begin(), data.end());
    result.assign(data.begin(), data.begin() + k);
}

void test_insertion_sort(vector<int> &data, vector<int> &result) {
    result.resize(k+1);
    for(int i = 0; i < data.size(); i++ ) {
        int j = min(i - 1, k - 1);
        for(; j >= 0 && result[j] > data[i]; j--) {
            result[j+1] = result[j];
        }
        result[j+1] = data[i];
    }
    result.pop_back();
}

void test_heap(vector<int> &data, vector<int> &heap) {
    for(int n : data) {
        if(heap.size() < k) {
            heap.push_back(n);
            push_heap(heap.begin(), heap.end());
        } else if(heap[0] > n) {
            pop_heap(heap.begin(), heap.end());
            heap[heap.size() - 1] = n;
            push_heap(heap.begin(), heap.end());
        }
    }
    sort_heap(heap.begin(), heap.end());
}


int time_cost(function<void(vector<int>&, vector<int>&)> func, const vector<int> &data) {
    vector<int> result, data_copy = data;
    auto t1 = chrono::system_clock::now();
    func(data_copy, result);
    auto t2 = chrono::system_clock::now();
    //print_array(result);
    return chrono::duration_cast<chrono::milliseconds>(t2 - t1).count();
}


void test_performance(const vector<int> &data) {
    int t1 = time_cost(test_directly_sort, data),
        t2 = time_cost(test_insertion_sort, data),
        t3 = time_cost(test_heap, data);
    cout<< "Directly sort hole array cost time:"<< t1<< "ms"<< endl;
    cout<< "Use insertion sort to maintain cost time:"<< t2<< "ms"<< endl;
    cout<< "Use heap to maintain cost time:"<< t3<< "ms"<< endl;
}



int main()
{
    //vector<int> data{3, 1, 7, 2, 5, 4, 9, 0, 6};
    vector<int> data = generate_random();
    test_performance(data);
    return 0;
}

