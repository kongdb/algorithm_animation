#include "bktree.h"
#include "heap.h"

#include <iostream>
#include <chrono>

vector<pair<string, int>>
brute_force(const string &target, const vector<string> &candidates, int radius)
{
    vector<pair<string, int>> result;
    for(const auto &candidate : candidates)
    {
        int distance = edit_distance(target, candidate);
        if(distance <= radius)
            result.push_back(make_pair(candidate, distance));
    }
    return result;
}

void test_bk_tree()
{
    auto names = read_file("../../data/names_unique.txt");
    string target = "Choon Kan Lan";
    auto t1 = chrono::system_clock::now();
    BKTree *tree = new BKTree(names);
    auto t2 = chrono::system_clock::now();
    
    int radius1 = 2, radius2 = 0;

    auto t3 = chrono::system_clock::now();
    auto res1 = brute_force(target, names, radius1);
    auto t4 = chrono::system_clock::now();
    auto res2 = tree->search(target, radius1);
    auto t5 = chrono::system_clock::now();
    cout<< "BKTree create time     :"<< chrono::duration_cast<chrono::milliseconds>(t2 - t1).count()<< "ms"<< endl;
    cout<< "brute force search (radius 2) time:"<< chrono::duration_cast<chrono::milliseconds>(t4 - t3).count()<< "ms"<< endl;
    printResult(res1);
    cout<< "BKTree      search (radius 2) time:"<< chrono::duration_cast<chrono::milliseconds>(t5 - t4).count()<< "ms"<< endl;
    printResult(res2);
    auto t6 = chrono::system_clock::now();
    res1 = brute_force(target, names, radius2);
    auto t7 = chrono::system_clock::now();
    res2 = tree->search(target, radius2);
    auto t8 = chrono::system_clock::now();
    cout<< "brute force search (radius 0) time:"<< chrono::duration_cast<chrono::milliseconds>(t7 - t6).count()<< "ms"<< endl;
    printResult(res1);
    cout<< "BKTree      search (radius 0) time:"<< chrono::duration_cast<chrono::milliseconds>(t8 - t7).count()<< "ms"<< endl;
    printResult(res2);
}

void test_heap()
{
    vector<int> array{3, 2, 7, 1, 5};
    Heap heap(array);
    heap.push(4);
    heap.push(9);
    heap.push(0);
    for(int i = 0; i < array.size() + 3; i++)
        cout<< heap.pop()<< endl;
}

int main()
{
    /*cout<< edit_distance("abc", "bd")<< endl;
    cout<< edit_distance("abc", "abd")<< endl;
    cout<< edit_distance("bc", "de")<< endl;*/
    test_bk_tree();
    //test_heap();
    return 0;
}
