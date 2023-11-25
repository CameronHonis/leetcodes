#include <vector>
#include <algorithm>
#include <cassert>

using namespace std;

struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};

class Solution {
public:
    ListNode* mergeKLists(vector<ListNode*>& heads) {
        if (heads.empty()) {
            return nullptr;
        }
        if (heads.size() == 1) {
            return heads[0];
        }

        ListNode* nodes[heads.size()];
        int nodes_idx = 0;
        for (int i = 0; i < heads.size(); i++) {
            ListNode* curr = heads[i];
            while (curr != nullptr) {
                nodes[nodes_idx++] = curr;
                curr = curr->next;
            }
        }
        sort(nodes, nodes + nodes_idx, [](ListNode* a, ListNode* b) {
            return a->val < b->val;
        });
        for (int i = 0; i < nodes_idx - 1; i++) {
            nodes[i]->next = nodes[i + 1];
        }
    }
};

int main() {
    Solution s;
    vector<ListNode*> heads = {
    };
    ListNode* result = s.mergeKLists(heads);
    assert(result)
}