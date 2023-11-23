#include <string>
#include <cassert>
#include <vector>

using namespace std;

struct MatcherPointers {
    int contentIdx;
    int patternIdx;
};

class Solution {
public:
    bool isMatch(string content, string pattern) {
        vector<MatcherPointers> matcherPointersList = {MatcherPointers{0, 0}};
        while (!matcherPointersList.empty()) {
            MatcherPointers matcherPointers = matcherPointersList.back();
            matcherPointersList.pop_back();

            if (matcherPointers.patternIdx >= pattern.length()) {
                if (matcherPointers.contentIdx == content.length()) {
                    return true;
                } else {
                    continue;
                }
            }

            bool isStarred = false;
            if (matcherPointers.patternIdx < pattern.length() - 1) {
                char nextP = pattern.at(matcherPointers.patternIdx + 1);
                if (nextP == '*') {
                    isStarred = true;
                }
            }

            if (matcherPointers.contentIdx == content.length()) {
                if (!isStarred) {
                    continue;
                }
                matcherPointersList.push_back(MatcherPointers{matcherPointers.contentIdx, matcherPointers.patternIdx + 2});
                continue;
            }

            char p = pattern.at(matcherPointers.patternIdx);
            char c = content.at(matcherPointers.contentIdx);
            bool doesMatch = p == '.' || p == c;

            if (isStarred) {
                if (doesMatch) {
                    matcherPointersList.push_back(MatcherPointers{matcherPointers.contentIdx + 1, matcherPointers.patternIdx});
                    matcherPointersList.push_back(MatcherPointers{matcherPointers.contentIdx, matcherPointers.patternIdx + 2});
                } else {
                    matcherPointersList.push_back(MatcherPointers{matcherPointers.contentIdx, matcherPointers.patternIdx + 2});
                }
            } else {
                if (doesMatch) {
                    matcherPointersList.push_back(MatcherPointers{matcherPointers.contentIdx + 1, matcherPointers.patternIdx + 1});
                } else {
                    continue;
                }

            }
        }
        return false;
    }

    bool isMatch(string content, string pattern, int contentIdx, int patternIdx) {
        if (patternIdx >= pattern.length()) {
            if (contentIdx == content.length()) {
                return true;
            } else {
                return false;
            }
        }

        char p = pattern.at(patternIdx);
        bool isStarred = false;
        if (patternIdx < pattern.length() - 1) {
            char nextP = pattern.at(patternIdx + 1);
            if (nextP == '*') {
                isStarred = true;
            }
        }

        if (contentIdx == content.length()) {
            if (!isStarred) {
                return false;
            }
            return isMatch(content, pattern, contentIdx, patternIdx + 2);
        }

        char c = content.at(contentIdx);

        bool doesMatch = p == '.' || p == c;

        if (isStarred) {
            if (doesMatch) {
                return isMatch(content, pattern, contentIdx + 1, patternIdx) ||
                       isMatch(content, pattern, contentIdx, patternIdx + 2);
            } else {
                return isMatch(content, pattern, contentIdx, patternIdx + 2);
            }
        } else {
            if (doesMatch) {
                return isMatch(content, pattern, contentIdx + 1, patternIdx + 1);
            } else {
                return false;
            }
        }
    }
};

int main() {
    bool isMatch = Solution().isMatch("aa", "a");
    assert(!isMatch);

    isMatch = Solution().isMatch("aa", "a*");
    assert(isMatch);

    isMatch = Solution().isMatch("aaaaaaaaaaaaaaabbba", "a*b*a");
    assert(isMatch);

    isMatch = Solution().isMatch("bb", "a*bb");
    assert(isMatch);

    isMatch = Solution().isMatch("abc", "abcd*");
    assert(isMatch);

    isMatch = Solution().isMatch("abc", "abc*");
    assert(isMatch);

    isMatch = Solution().isMatch("aaaaabcddddd", "a*e*c*d*");
    assert(!isMatch);

    isMatch = Solution().isMatch("ab", ".*c");
    assert(!isMatch);

    isMatch = Solution().isMatch("ab", ".*");
    assert(isMatch);
}