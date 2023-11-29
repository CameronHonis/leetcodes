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

        vector<ListNode*> nodes;
        for (int i = 0; i < heads.size(); i++) {
            ListNode* curr = heads[i];
            while (curr != nullptr) {
                nodes.push_back(curr);
                curr = curr->next;
            }
        }
        if (nodes.empty()) {
            return nullptr;
        }
        sort(nodes.begin(), nodes.end(), [](ListNode* a, ListNode* b) {
            return a->val < b->val;
        });
        for (int i = 0; i < nodes.size() - 1; i++) {
            if (i == nodes.size() - 1) {
                nodes[i]->next = nullptr;
            } else {
                nodes[i]->next = nodes[i + 1];
            }
        }
        return nodes[0];
    }
};

ListNode* linkedListFromVector(vector<int> vec) {
    ListNode* head = nullptr;
    ListNode* curr = nullptr;
    for (int i : vec) {
        if (head == nullptr) {
            head = new ListNode(i);
            curr = head;
        } else {
            curr->next = new ListNode(i);
            curr = curr->next;
        }
    }
    return head;
}

int main() {
    Solution sol;
    vector<ListNode*> heads = {nullptr, nullptr};
    ListNode* result = sol.mergeKLists(heads);
    assert(result == nullptr);

    ListNode* ll1 = linkedListFromVector(vector<int>({1, 4, 5}));
    vector<ListNode*> vec1 = {ll1};
    ListNode* result1 = sol.mergeKLists(vec1);
    assert(result1->val == 1);
    assert(result1->next->val == 4);
    assert(result1->next->next->val == 5);
    assert(result1->next->next->next == nullptr);

    ListNode* ll2 = linkedListFromVector(vector<int>({1, 3, 4}));
    ListNode* ll3 = linkedListFromVector(vector<int>({2, 6}));
    vector<ListNode*> vec2 = {ll1, ll2, ll3};
}