#include <cassert>
#include <tuple>

#include "datastructures/linked_list.cpp"


class Solution {
public:
    ListNode* reverseKGroup(ListNode* head, int k) {
        ListNode* rtn = nullptr;
        ListNode* prev_group_tail = nullptr;
        ListNode* curr_group_head = head;
        while (curr_group_head != nullptr) {
            ListNode* split_group_head;
            ListNode* next_group_head;
            int group_size;
            tie(split_group_head, next_group_head, group_size) = reverseGroup(curr_group_head, k);
            if (group_size < k) {
                tie(split_group_head, ignore, ignore) = reverseGroup(split_group_head, group_size);
                if (rtn == nullptr) {
                    rtn = split_group_head;
                }
                if (prev_group_tail != nullptr) {
                    prev_group_tail->next = split_group_head;
                }
                return rtn;
            }
            if (rtn == nullptr) {
                rtn = split_group_head;
            }
            if (prev_group_tail != nullptr) {
                prev_group_tail->next = split_group_head;
            }
            prev_group_tail = curr_group_head;
            curr_group_head = next_group_head;
        }
        return rtn;
    }

    static tuple<ListNode*, ListNode*, int> reverseGroup(ListNode* group_head, int k) {
        ListNode* prev = nullptr;
        ListNode* curr = group_head;
        for (int i = 0; i < k; i++) {
            if (curr == nullptr) {
                return tuple<ListNode*, ListNode*, int>{prev, curr, i};
            }
            ListNode* next = curr->next;
            curr->next = prev;
            prev = curr;
            curr = next;
        }
        return tuple<ListNode*, ListNode*, int>{prev, curr, k};
    }
};

void compareVectors(vector<int> v1, vector<int> v2) {
    assert(v1.size() == v2.size());
    for (int i = 0; i < v1.size(); i++) {
        int v1_val = v1[i];
        int v2_val = v2[i];
        assert(v1_val == v2_val);
    }
}

void testReverseGroup() {
    Solution s;
    vector<int> vec = {1, 2, 3};
    ListNode* ll = linkedListFromVector(vec);
    const auto out = s.reverseGroup(ll, 3);
    ListNode* rll = get<0>(out);
    ListNode* newHead = get<1>(out);
    assert(newHead == nullptr);
    vector<int> rll_vals = vectorFromLinkedList(rll);
    compareVectors(rll_vals, vector<int>{3,2,1});

    ll = linkedListFromVector(vec);
    const auto out1 = s.reverseGroup(ll, 2);
    rll = get<0>(out1);
    newHead = get<1>(out1);
    assert(newHead->val == 3);
    assert(newHead->next == nullptr);
    rll_vals = vectorFromLinkedList(rll);
    compareVectors(rll_vals, vector<int>{2,1});

    ll = linkedListFromVector(vec);
    const auto out2 = s.reverseGroup(ll, 4);
    rll = get<0>(out2);
    newHead = get<1>(out2);
    assert(newHead == nullptr);
    rll_vals = vectorFromLinkedList(rll);
    compareVectors(rll_vals, vector<int>{3,2,1});
}

void testReverseKGroup() {
    Solution s;
    vector<int> vec = {1, 2, 3, 4, 5};
    ListNode* head = linkedListFromVector(vec);
//    ListNode* result = s.reverseKGroup(head, 2);
//    assert(result->val == 2);
//    assert(result->next->val == 1);
//    assert(result->next->next->val == 4);
//    assert(result->next->next->next->val == 3);
//    assert(result->next->next->next->next->val == 5);

    vec = {1,2,3,4,5};
    head = linkedListFromVector(vec);
    ListNode* result = s.reverseKGroup(head, 3);
    assert(result->val == 3);
    assert(result->next->val == 2);
    assert(result->next->next->val == 1);
    assert(result->next->next->next->val == 4);
    assert(result->next->next->next->next->val == 5);

}

int main() {
//    testReverseGroup();
    testReverseKGroup();
}