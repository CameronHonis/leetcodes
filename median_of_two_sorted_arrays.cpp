double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
        int m = nums1.size();
        int n = nums2.size();

        // Ensure nums1 is the smaller array to simplify the algorithm
        if (m > n) {
            swap(nums1, nums2);
            swap(m, n);
        }

        int left = 0, right = m;
        int mid = (m + n + 1) / 2; // Calculate the midpoint of the combined array

        while (left <= right) {
            int partition1 = left + (right - left) / 2;
            int partition2 = mid - partition1;

            int maxLeft1 = (partition1 == 0) ? INT_MIN : nums1[partition1 - 1];
            int minRight1 = (partition1 == m) ? INT_MAX : nums1[partition1];

            int maxLeft2 = (partition2 == 0) ? INT_MIN : nums2[partition2 - 1];
            int minRight2 = (partition2 == n) ? INT_MAX : nums2[partition2];

            if (maxLeft1 <= minRight2 && maxLeft2 <= minRight1) {
                // Found the correct partitions
                if ((m + n) % 2 == 0) {
                    // If the combined array has an even length, take the average
                    return (max(maxLeft1, maxLeft2) + min(minRight1, minRight2)) / 2.0;
                } else {
                    // If the combined array has an odd length, return the maximum of the left elements
                    return max(maxLeft1, maxLeft2);
                }
            } else if (maxLeft1 > minRight2) {
                // Adjust the partition1 to the left
                right = partition1;
            } else {
                // Adjust the partition1 to the right
                left = partition1 + 1;
            }
        }

        return 0.0; // Return 0.0 if no solution is found (shouldn't normally happen)
    }