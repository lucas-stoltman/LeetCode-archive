// https://leetcode.com/problems/single-element-in-a-sorted-array/
#pragma once

#include <algorithm>  // sort
#include <iostream>   // output
#include <vector>     // vector

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

      // nums[size()-1] check left
      if (nums[size - 2] != nums[size - 1]) {
         return nums[size - 1];
      }
   }
   return 0;
}
// end solution

// random helper method
int randNext() { return rand() % 50; }

std::vector<int> vectBuilder(int length) {
   std::vector<int> result;
   std::vector<int> alreadyAdded;
   srand(time(0));

   int coinflip = 0;

   for (int i = 0; i < length; i++) {
      int r = randNext();

      // separate random number to decouple from numbers added
      int coinR = randNext();

      // check if a value has already been added
      if (std::find(alreadyAdded.begin(), alreadyAdded.end(), r) !=
          alreadyAdded.end()) {
      } else {
         // check if it only adds one value
         if ((coinR <= 2) && (coinflip == 0)) {
            result.push_back(r);
            alreadyAdded.push_back(r);
            coinflip++;
         } else {
            result.push_back(r);
            result.push_back(r);
            alreadyAdded.push_back(r);
         }
      }
   }
   // in case the coinflip never succeeds
   if (coinflip != 1) {
      result.pop_back();
      std::cout << result[length - 1] << std::endl;

      coinflip++;
      assert(coinflip == 1);
   }

   // sort
   sort(result.begin(), result.end());
   return result;
}

void run540() {
   std::cout << "540: Single Element in a Sorted Array" << std::endl;
   std::vector<int> vect = vectBuilder(10);

   std::cout << "Before:\t";
   for (int x : vect) {
      std::cout << x << " ";
   }
   std::cout << std::endl;

   std::cout << "After:\t" << singleNonDuplicate(vect);

   std::cout << std::endl;
}