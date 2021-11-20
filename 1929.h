#pragma once

#include <iostream>


   vector<int> getConcatenation(vector<int>& nums) {
        vector<int> result;
    
        for (int u = 0; u < 2; u++){
            for (int i = 0; i < nums.size(); i++){
                result.push_back(nums[i]);
            }
        }
        return result;
    }