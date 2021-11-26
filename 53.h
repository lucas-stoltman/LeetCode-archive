// https://leetcode.com/problems/maximum-subarray/
#pragma once

#include <iostream>
#include <vector>

// begin solution
int maxSubArray(std::vector<int>& nums) {
       return -1; 
    }

// end solution

void run53() {
   std::cout << "53: Maximum Subarray" << std::endl;
   std::vector<int> vect{2, 5, 2, 6, 3, 4, 6};

   std::cout << "Before:\t";
   for (int x : vect) {
      std::cout << x << " ";
   }
   std::cout << std::endl;

   std::cout << "After:\t";
   // for (int x : maxSubArray(vect)) {
   //    std::cout << x << " ";
   // }
   std::cout << std::endl;
}