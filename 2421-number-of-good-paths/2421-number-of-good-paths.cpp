class Solution {
public:
    int numberOfGoodPaths(vector<int>& vals, vector<vector<int>>& edges) {
        int res{0};
        vector<vector<int>> adjencency(vals.size(), vector<int>());
        for (const auto& item : edges) {
            if (vals[item.front()] >= vals[item.back()])
                adjencency[item.front()].push_back(item.back());
            if (vals[item.front()] <= vals[item.back()])
                adjencency[item.back()].push_back(item.front());
        }
        map<int, vector<int>> val2nodes;
        for (int i = 0; i < vals.size(); ++i)
            val2nodes[vals[i]].push_back(i);
        
        vector<int> par(vals.size());
        vector<int> rank(vals.size(), 0);
        iota(par.begin(), par.end(), 0);
        function<int(int)> find = [&](int index) {
            if (par[index] == index) return index;
            return par[index] = find(par[index]);
        };
        function<void(int, int)> unite = [&](int lhs, int rhs) {
            lhs = find(lhs);
            rhs = find(rhs);
            if (lhs == rhs) return;
            if (rank[lhs] < rank[rhs]) {
                par[lhs] = rhs;
            } else {
                par[rhs] = lhs;
                if (rank[lhs] == rank[rhs]) ++rank[lhs];
            }
        };
        for (const auto& item : val2nodes) {
            for (const auto& index : item.second) 
                for (const auto& neighbor : adjencency[index])
                    unite(index, neighbor);
            unordered_map<int, int> group2size;
            for (const auto& index : item.second)
                ++group2size[find(index)];
            for (const auto& [groupID, size] : group2size)
                res += size * (size + 1) / 2;
        }
        
        return res;
    }
};