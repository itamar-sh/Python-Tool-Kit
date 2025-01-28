"""
We are given a 2D integer array of events where each event starts at startTime, ends at endTime, and pays a value if attended. Return the maximum profit possible from picking up to 2 non-overlapping events.
"""

class Solution:
    def maxTwoEvents(self, events):
        events.sort()
        dp = [[-1] * 3 for _ in range(len(events))]
        return self.find_events(events, 0, 0, dp)

    # Recursive function to find the greatest sum for the pairs.
    def find_events_binary_search(self, events, idx, cnt, dp):
        """
        Let n be the number of events in the events array.

        Time Complexity: O(n⋅logn)

        The algorithm sorts the array of events by their starting times, which takes O(n⋅logn) time. Calculating the maximum value for each event index involves solving recursive subproblems. For each of the n events, we compute the result for 3 states (0, 1, or 2 elements picked), and finding the next valid event using binary search takes O(logn) time.

        Memoization ensures that each subproblem is solved only once, avoiding redundant computations. Therefore, the overall time complexity is given by O(n⋅logn).

        Space complexity: O(n)

        The algorithm requires O(n) space for the memo array, which stores the precomputed values of subproblems to avoid redundant calculations during recursion. Also, the recursion depth contributes O(n) stack space.

        Apart from this, the space complexity of the sorting algorithm depends on the programming language.
            In Python, the sort method sorts a list using the Timsort algorithm which is a combination of Merge Sort and Insertion Sort and has O(l) additional space, where l is the size of the list.
            In Java, Arrays.sort() is implemented using a variant of the Quick Sort algorithm which has a space complexity of O(logn) for sorting two arrays.
            In C++, the sort() function is implemented as a hybrid of Quick Sort, Heap Sort, and Insertion Sort, with a worse-case space complexity of O(logn).

        Therefore, the total space complexity is given by O(n).

        """
        if cnt == 2 or idx >= len(events):
            return 0
        if dp[idx][cnt] == -1:
            end = events[idx][1]
            lo, hi = idx + 1, len(events) - 1
            while lo < hi:
                mid = lo + ((hi - lo) >> 1)
                if events[mid][0] > end:
                    hi = mid
                else:
                    lo = mid + 1
            include = events[idx][2] + (
                self.find_events(events, lo, cnt + 1, dp)
                if lo < len(events) and events[lo][0] > end
                else 0
            )
            exclude = self.find_events(events, idx + 1, cnt, dp)
            dp[idx][cnt] = max(include, exclude)
        return dp[idx][cnt]


    def maxTwoEventsMinHeap(self, events: List[List[int]]) -> int:
        """
        Let n be the number of events in the events array.

        Time Complexity: O(n⋅logn)

        The algorithm sorts the events by their start times, which takes O(n⋅logn). While iterating through the event list, the algorithm performs operations related to the priority queue (min-heap) for each event. Popping from the heap and pushing a new event both take O(logn), leading to a total of O(n⋅logn) for all these operations.

        Combining all steps, the overall time complexity is given by O(n⋅logn).

        Space complexity: O(n)

        The algorithm requires O(n) space for the priority queue in the worst case.

        Apart from this, the space complexity of the sorting algorithm depends on the programming language.
            In Python, the sort method sorts a list using the Timsort algorithm which is a combination of Merge Sort and Insertion Sort and has O(l) additional space, where l is the size of the list.
            In Java, Arrays.sort() is implemented using a variant of the Quick Sort algorithm which has a space complexity of O(logn) for sorting two arrays.
            In C++, the sort() function is implemented as a hybrid of Quick Sort, Heap Sort, and Insertion Sort, with a worse-case space complexity of O(logn).

        Therefore, the total space complexity is given by O(n).

        """
        # Create a list to store the pair (end time, value) for events
        pq = []

        # Sort the events by their start time
        events.sort(key=lambda x: x[0])

        max_val = 0
        max_sum = 0

        for event in events:
            # Pop all valid events from the priority queue and take their maximum
            while pq and pq[0][0] < event[0]:
                max_val = max(max_val, pq[0][1])
                heapq.heappop(pq)

            # Calculate the maximum sum by adding the current event's value and the best previous event's value
            max_sum = max(max_sum, max_val + event[2])

            # Push the current event's end time and value into the heap
            heapq.heappush(pq, (event[1], event[2]))

        return max_sum

    def maxTwoEventsGreedy(self, events):
        """
        Let n be the number of events in the events array.

        Time Complexity: O(n⋅logn)

        For each event, we create two entries (start and end) in the times array. Since there are n events, this step takes O(n) time. The times array contains 2*n elements (start and end times for each event). Sorting this array takes O((2n)⋅log2n)=O(n⋅logn) time.

        After sorting, we traverse the times array once to compute the result. This step takes O(2⋅n)=O(n) time. Combining all steps, the overall time complexity is given by O(n⋅logn).

        Space complexity: O(n)

        Since there are exactly 2⋅n values in the times array, the algorithm requires O(2⋅n)=O(n) space for the times array in the worst case.

        Apart from this, the space complexity of the sorting algorithm depends on the programming language.
            In Python, the sort method sorts a list using the Timsort algorithm which is a combination of Merge Sort and Insertion Sort and has O(l) additional space, where l is the size of the list.
            In Java, Arrays.sort() is implemented using a variant of the Quick Sort algorithm which has a space complexity of O(logn) for sorting two arrays.
            In C++, the sort() function is implemented as a hybrid of Quick Sort, Heap Sort, and Insertion Sort, with a worse-case space complexity of O(logn).

        Therefore, the total space complexity is given by O(n).

        """
        times = []
        for e in events:
            # 1 denotes start time.
            times.append([e[0], 1, e[2]])
            # 0 denotes end time.
            times.append([e[1] + 1, 0, e[2]])

        ans, max_value = 0, 0
        times.sort()

        for time_value in times:
            # If current time is a start time, find maximum sum of maximum end
            # time till now.
            if time_value[1]:
                ans = max(ans, time_value[2] + max_value)
            else:
                max_value = max(max_value, time_value[2])

        return ans