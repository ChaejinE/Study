#include <vector>

using namespace std;

class Solution
{
public:
    void moveZeroes(vector<int> &nums)
    {
        int zeroIdx = 0;
        for (int idx = 0; idx < nums.size(); ++idx)
        {
            if (nums[idx])
            {
                swap(nums[zeroIdx], nums[idx]);
                ++zeroIdx;
            }
        }
    }
};