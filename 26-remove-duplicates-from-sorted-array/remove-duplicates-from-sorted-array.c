int removeDuplicates(int* nums, int numsSize) {
   int* top = nums;
   int* bottom = nums;
   int prev = -((*top) + 1);
   while (top - nums < numsSize) {
       if (*top != prev) {
           *bottom = *top;
           bottom++;
       }
       prev = *top;
       top++;
   }
   return bottom-nums;
}