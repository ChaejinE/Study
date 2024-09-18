#include <vector>

using namespace std;

class Solution
{
public:
    int minSubArrayLen(int target, vector<int> &nums)
    {
        int sum = 0;
        int start = 0;
        int end = 0;
        int ans = INT_MAX;

        while (end < nums.size())
        {
            sum += nums[end++];

            while (sum >= target)
            {
                sum -= nums[start++];
                ans = min(ans, end - start + 1);
            }
        }

        return ans >= INT_MAX ? 0 : ans;
    }
};
