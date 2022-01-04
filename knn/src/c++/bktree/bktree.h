#ifndef BK_TREE_H
#define BK_TREE_H

#include "utils.h"

class BKTree
{
    public:
        BKTree(vector<string> &candidates);
        ~BKTree();
        vector<pair<string, int>> search(const string &target, int radius) const;
    private:
        struct BKNode
        {
            string data;
            vector<BKNode*> children;
            BKNode(const string &d) : data(d) {}
            ~BKNode()
            {
                for(auto &node : children)
                    if(node)
                        delete node;
            }
        };
        void buildTree(const vector<string> &candidates);
        void insert(const string &candidate, BKNode*&node);
        void search(const string &target, int radius, BKNode *node, vector<pair<string, int>> &) const;
        BKNode *root_;
};

#endif // BK_TREE_H
