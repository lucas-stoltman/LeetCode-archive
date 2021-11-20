#pragma once

#include <iostream>

// begin solution
std::vector<int> getConcatenation(std::vector<int>& nums) {
   std::vector<int> result;

   for (int u = 0; u < 2; u++) {
      for (int i = 0; i < nums.size(); i++) {
         result.push_back(nums[i]);
      }
   }
   return result;
}
// end solution


void run1929() {
   std::cout << "1929: Concatenation of Array" << std::endl;
   std::vector<int> vect{2, 5, 2, 6, 3, 4, 6};

   std::cout << "Before:\t";
   for (int x : vect) {
      std::cout << x << " ";
   }
   std::cout << std::endl;

   std::cout << "After:\t";
   for (int x : getConcatenation(vect)) {
      std::cout << x << " ";
   }
   std::cout << std::endl;
}