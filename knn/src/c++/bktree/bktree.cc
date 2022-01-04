
#include <algorithm>

#include "bktree.h"


BKTree::BKTree(vector<string> &candidates)
    : root_(nullptr)
{
    random_shuffle(candidates.begin(), candidates.end());
    buildTree(candidates);
}

BKTree::~BKTree()
{
    if(root_)
        delete root_;
}

void BKTree::buildTree(const vector<string> &candidates)
{
    for(auto &candidate : candidates)
        insert(candidate, root_);
}

void BKTree::insert(const string &candidate, BKTree::BKNode *&node)
{
    if(!node)
        node = new BKTree::BKNode(candidate);
    else
    {
        int distance = edit_distance(candidate, node->data);
        if(node->children.size() <= distance)
            node->children.resize(distance + 1, nullptr);
        insert(candidate, node->children[distance]);
    }
}

vector<pair<string, int>> BKTree::search(const string &target, int radius) const
{
    vector<pair<string, int>> result;
    search(target, radius, root_, result);
    return result;
}

void BKTree::search(const string &target, int radius, BKTree::BKNode *node,
                    vector<pair<string, int>> &result) const
{
    if(!node)
        return;
    int distance = edit_distance(target, node->data);
    if(distance <= radius)
        result.push_back(make_pair(node->data, distance));
    /*
     *   node
     *    |   \
     *    |    \ d
     *    |     \
     *   res----target
     *       r
     * 1. the furthest distance between node and res is d + r
     *                  d         r
     *    that is  node----target----res
     * 2. the closest distance between node and res is d - r
     *    2.1 what if d <= r, that means node is one of the result
     *    2.2 else if d > r, that is
     *          d-r      r
     *      node----res-----target
     * */
    for(int next = distance <= radius ? 1 : distance - radius; next <= distance + radius; next++)
        if(next >= node->children.size())
            break;
        else
            search(target, radius, node->children[next], result);
}


