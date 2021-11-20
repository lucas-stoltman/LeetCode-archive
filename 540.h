#pragma once

#include <iostream>
#include <vector>

// begin solution
int singleNonDuplicate(std::vector<int>& nums) {
   int size = nums.size();

   if (size == 1) {
      return nums[0];
   }

   for (int i = 0; i < nums.size(); i++) {
      // nums[0] check right
      if (nums[0] != nums[1]) {
         return nums[0];
      }

      // check left and right
      if (i > 0) {
         if ((nums[i - 1] != nums[i]) && (nums[i] != nums[i + 1])) {
            return nums[i];
         }
      }

      // nums[size()] check left
      if (nums[size - 2] != nums[size - 1]) {
         return nums[size - 1];
      }
   }
   return 0;
}
// end solution