#pragma once

#include <iostream>
#include <vector>

std::vector<int> runningSum(std::vector<int>& nums) {
   int sum = 0;
   std::vector<int> result = {nums[0]};
   for (int i = 1; i < nums.size(); i++) {
      result.push_back(result.back() + nums[i]);
   }
   return result;
}

void run1480() {
   std::cout << "1480: Running Sum of 1d Array" << std::endl;
   std::vector<int> vect{2, 5, 2, 6, 3, 4, 6};

   for (int x : vect) {
      std::cout << x << " ";
   }
   std::cout << std::endl;

   for (int x : runningSum(vect)) {
      std::cout << x << " ";
   }
   std::cout << std::endl;
}