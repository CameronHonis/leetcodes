#include <vector>
#include <string>
#include <unordered_map>
#include <cassert>
#include <iostream>

using namespace std;

class Solution {
public:
    static vector<int> findSubstring(const string &s, vector<string> &words) {
        if (words.empty())
            return {};

        vector<int> substr_idxs;

        int m = words[0].length();
        int substr_len = m * words.size();

        unordered_map<string, int> init_unused{};
        for (string word : words) {
            bool is_first_appearance = init_unused.find(word) == init_unused.end();
            if (is_first_appearance) {
                init_unused.insert({word, 1});
            } else {
                init_unused[word]++;
            }
        }

        for (int i = 0; i < s.length() - substr_len + 1; i++) {
            unordered_map<string, int> unused = init_unused;
            for (int k = i; k < s.length(); k += m) {
                string word = s.substr(k, m);
                bool is_in_unused = unused.find(word) != unused.end();
                if (!is_in_unused)
                    break;
                unused[word]--;
                if (unused[word] == 0)
                    unused.erase(word);
                if (unused.empty()) {
                    substr_idxs.push_back(i);
                    break;
                }
            }
        }
        return substr_idxs;
    }
};

void testFindSubstring() {
    vector<string> v0 {"ab", "cd", "ef"};
    vector<int> v0_out = Solution::findSubstring("abcdef", v0);
    assert(v0_out.size() == 1);
    assert(v0_out[0] == 0);

    vector<string> v1{"foo", "bar"};
    vector<int> v1_out = Solution::findSubstring("barfoothefoobarman", v1);
    assert(v1_out.size() == 2);
    assert(v1_out[0] == 0);
    assert(v1_out[1] == 9);

    vector<string> v2{"word", "good", "best", "word"};
    vector<int> v2_out = Solution::findSubstring("wordgoodgoodgoodbestword", v2);
    assert(v2_out.empty());

    vector<string> v3{"bar", "foo", "the"};
    vector<int> v3_out = Solution::findSubstring("barfoofoobarthefoobarman", v3);
    assert(v3_out.size() == 3);
    assert(v3_out[0] == 6);
    assert(v3_out[1] == 9);
    assert(v3_out[2] == 12);
}

int main() {
    testFindSubstring();
    return 0;
}