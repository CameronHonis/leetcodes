#include <vector>
#include "linked_list.h"

using namespace std;

ListNode* linkedListFromVector(vector<int> vec) {
    if (vec.empty()) {
        return nullptr;
    }

    ListNode* head = new ListNode(vec[0]);
    ListNode* curr = head;
    for (int i = 1; i < vec.size(); i++) {
        curr->next = new ListNode(vec[i]);
        curr = curr->next;
    }

    return head;
}

vector<int> vectorFromLinkedList(ListNode* head) {
    vector<int> rtn;
    ListNode* curr = head;
    while (curr != nullptr) {
        rtn.push_back(curr->val);
        curr = curr->next;
    }
    return rtn;
}