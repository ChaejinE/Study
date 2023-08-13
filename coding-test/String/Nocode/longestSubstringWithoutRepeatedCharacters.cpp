#include <vector>
#include <string>

using namespace std;

class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        unordered_map<char, int> hash;
        for (char& ch : s) {
            if (hash.find(ch) == hash.end()) {
                hash[ch] = -1;
            }
        }
        int start = 0, end = 0;
        int maxLength = 0;
        
        while (!s.empty() && end <= s.length() - 1) {
            if (hash[s[end]] >= start) {
                while (s[start] != s[end]) {
                    ++start;
                }
                ++start;
            }

            maxLength = max(maxLength, end - start + 1);
            hash[s[end]] = end;
            ++end;
        }

        return maxLength;
    }
};