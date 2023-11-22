#include <string>
#include <cassert>

using namespace std;

class Solution {
public:
    bool isMatch(string content, string pattern) {
        return isMatch(content, pattern, 0, 0, -1);
    }

    bool isMatch(string content, string pattern, int contentIdx, int patternIdx, int lastPatternIdx) {
        if (contentIdx == content.length()) return true;
        if (patternIdx >= pattern.length()) return false;
        char c = content.at(contentIdx);
        char p = pattern.at(patternIdx);
        bool isStarred = false;
        if (patternIdx < pattern.length() - 1) {
            char nextP = pattern.at(patternIdx + 1);
            if (nextP == '*') {
                isStarred = true;
            }
        }
        bool doesMatch;
        if (p == '.') {
            if (patternIdx == lastPatternIdx) {
                char prevC = content.at(contentIdx - 1);
                doesMatch = (prevC == c);
            } else {
                doesMatch = true;
            }
        } else {
            doesMatch = (p == c);
        }
        if (isStarred) {
            if (doesMatch) {
                return isMatch(content, pattern, contentIdx + 1, patternIdx, patternIdx) ||
                       isMatch(content, pattern, contentIdx, patternIdx + 2, patternIdx);
            } else {
                return isMatch(content, pattern, contentIdx, patternIdx + 2, patternIdx);
            }
        } else {
            if (doesMatch) {
                return isMatch(content, pattern, contentIdx + 1, patternIdx + 1, patternIdx);
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