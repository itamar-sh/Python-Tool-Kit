from typing import List
from heapq import heappush, heappop


class Solution:
    """
    There is a party where n friends numbered from 0 to n - 1 are attending. There is an infinite number of chairs in this party that are numbered from 0 to infinity. When a friend arrives at the party, they sit on the unoccupied chair with the smallest number.

    For example, if chairs 0, 1, and 5 are occupied when a friend comes, they will sit on chair number 2.

    When a friend leaves the party, their chair becomes unoccupied at the moment they leave. If another friend arrives at that same moment, they can sit in that chair.

    You are given a 0-indexed 2D integer array times where times[i] = [arrivali, leavingi], indicating the arrival and leaving times of the ith friend respectively, and an integer targetFriend. All arrival times are distinct.

    Return the chair number that the friend numbered targetFriend will sit on.
    """
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
        combined_entries = []
        for entry in times:
            combined_entries.append((entry[0], 1))  # 1 is enter party, 0 is leaving party
            combined_entries.append((entry[1], 0, entry[0]))  # 1 is enter party, 0 is leaving party
        combined_entries.sort()
        chairs_available_min_heap = [0]
        chairs_occupied_by_entry_time = dict()
        for event in combined_entries:
            if event[1]: # new arrival want to sit
                if len(chairs_available_min_heap) == 1:
                    heappush(chairs_available_min_heap, chairs_available_min_heap[0]+1)  # add next chair
                chairs_occupied_by_entry_time[event[0]] = heappop(chairs_available_min_heap)  # occupy chair
                if times[targetFriend][0] == event[0]:  # target friend was the one trying to sit
                    return chairs_occupied_by_entry_time[event[0]]
            else:  # someone is going to leave
                new_empty_chair = chairs_occupied_by_entry_time[event[2]]
                del chairs_occupied_by_entry_time[event[2]]
                heappush(chairs_available_min_heap, new_empty_chair)
        return -1 # should not get here


