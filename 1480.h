#pragma once

#include <vector>

std::vector<int> runningSum(std::vector<int>& nums) {
        int sum = 0;
        std::vector<int> result = {nums[0]};
        for (int i = 1; i < nums.size(); i++){
            result.push_back(result.back()+nums[i]);
        }
        return result;
    }