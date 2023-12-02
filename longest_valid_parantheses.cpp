#include <string>
#include <cassert>
#include <vector>
#include <stack>

using namespace std;

class Solution {
public:
    static int longestValidParentheses1(string s) {
        int n = s.size();
        if (n < 2)
            return 0;

        int maxLen = 0;
        vector<int> openIndices;
        int validStartIdx = n;
        for (int i = 0; i < n; i++) {
            char c = s.at(i);
            if (c == ')') {
                if (openIndices.empty()) {
                    int currLen = i - validStartIdx;
                    maxLen = max(maxLen, currLen);
                    validStartIdx = n;
                    openIndices = {};
                    continue;
                }
                int closedIdx = openIndices.back();
                openIndices.pop_back();
                validStartIdx = min(validStartIdx, closedIdx);
            } else {
                openIndices.push_back(i);
            }
        }
        int currLen = n - validStartIdx;
        return max(maxLen, currLen);
    }

    static int longestValidParentheses2(string s) {
        size_t n = s.size();
        if (n < 2)
            return 0;

        vector<pair<size_t, size_t>> groups;
        vector<size_t> openIndices;
        size_t startIdx = n;
        size_t endIdx = 0;
        for (int i = 0; i < n; i++) {
            if (openIndices.empty()) {
                if (startIdx < endIdx) {
                    pair<int, int> next_group = {startIdx, endIdx};
                    groups.emplace_back(next_group);
                }
                startIdx = n;
                endIdx = 0;
            }
            char c = s.at(i);
            if (c == ')') {
                if (openIndices.empty())
                    continue;

                size_t closedOpenIdx = openIndices.back();
                openIndices.pop_back();
                startIdx = min(startIdx, closedOpenIdx);
                endIdx = i;
            } else {
                openIndices.push_back(i);
            }
        }
        if (startIdx < endIdx) {
            pair<int, int> next_group = {startIdx, endIdx};
            groups.emplace_back(next_group);
        }

        size_t maxLen = 0;
        size_t currLen = 0;
        for (int group_idx = 0; group_idx < groups.size(); group_idx++) {
            size_t prev_group_end_idx = group_idx > 0 ? groups[group_idx-1].second : -2;
            auto [start_idx, end_idx] = groups[group_idx];
            if (prev_group_end_idx + 1 != start_idx) {
                maxLen = max(maxLen, currLen);
                currLen = 0;
            }
            currLen += end_idx - start_idx + 1;
        }
        maxLen = max(maxLen, currLen);
        return (int)maxLen;
    }

    static int longestValidParentheses(string s) {
        size_t n = s.length();

        stack<size_t> openIdxs;
        size_t firstValidIdx = 0;
        size_t maxLen = 0;
        for (size_t i = 0; i < n; i++) {
            if (s.at(i) == '(') {
                openIdxs.push(i);
            } else {
                if (openIdxs.empty()) {
                    firstValidIdx = i + 1;
                    continue;
                } else {
                    openIdxs.pop();
                }
                size_t currLen = openIdxs.empty() ? i - firstValidIdx + 1 : i - openIdxs.top();
                maxLen = max(maxLen, currLen);
            }
        }
        return (int)maxLen;
    }
};

void testSolution() {
    int longest0 = Solution::longestValidParentheses("(()");
    assert(longest0 == 2);
    int longest1 = Solution::longestValidParentheses(")()())");
    assert(longest1 == 4);
    int longest2 = Solution::longestValidParentheses(")()())))((()))()");
    assert(longest2 == 8);
    int longest3 = Solution::longestValidParentheses("()(()");
    assert(longest3 == 2);
    int longest4 = Solution::longestValidParentheses("(()(((()");
    assert(longest4 == 2);
}

int main() {
    testSolution();
    return 0;
}
