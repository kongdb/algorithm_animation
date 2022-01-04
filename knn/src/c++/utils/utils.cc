#include "utils.h"

int edit_distance(const string &s1, const string &s2)
{
    vector<int> row1(s1.size() + 1, 0), row2(s1.size() + 1, 0);
    for(int i = 1; i <= s1.size(); i++)
        row1[i] = row1[i-1] + 1;
    for(int i = 1; i <= s2.size(); i++)
    {
        row2[0] = i;
        for(int j = 1; j <= s1.size(); j++)
        {
            if(s1[j-1] == s2[i-1])
                row2[j] = row1[j-1];
            else
                row2[j] = 1 + min(row2[j-1], min(row1[j], row1[j-1]));
        }
        swap(row1, row2);
    }
    return row1.back();
}

vector<string> read_file(const string &name) {
    vector<string> content;
    ifstream f(name);
    string line;
    while(!f.eof()) {
        getline(f, line);
        content.push_back(line);
    }
    return content;
}

void printResult(const vector<pair<string, int>> &result)
{
    for(const auto &p : result)
        cout<< "("<< p.first<< ","<< p.second<< ")  ";
    cout<< endl;
}

