from typing import List
from copy import deepcopy


class Subsets:
    def get_all_subsets_using_bfs_iteratively(self, unique_numbers: List[int]) -> List[List[int]]:
        """
        Going from empty list to one item in each list and so on.
        Each time adding all numbers to all current lists.
        Lists inserted to result even if they are not completed.
        """
        all_subsets = [[]]
        for num in unique_numbers:
            all_subsets += [subset + [num] for subset in all_subsets]
        return all_subsets

    def get_all_subsets_using_dfs_recuresively(self, unique_numbers: List[int]) -> List[List[int]]:
        """
        Insert every path on the way. Going from empty list to full path.
        Each i step we take i numbers less so the rest of the pathes will be
        shorter, such way we avoid duplicates, permutations of full pathes.
        """
        def all_subsets_dfs(all_subsets, numbers_to_insert, current_set):
            all_subsets.append(current_set)
            for number_index in range(len(numbers_to_insert)):
                all_subsets_dfs(all_subsets, numbers_to_insert[number_index+1:], current_set + [numbers_to_insert[number_index]])

        all_subsets = []
        all_subsets_dfs(all_subsets, unique_numbers, [])
        return all_subsets


    def get_all_permutations_of_all_subsets_using_dfs_recuresively(self, unique_numbers):
        """
        Insert every path on the way. Going from empty list to full path.
        Each step we omit the used number behind so we find all the options to
        complete the current path.
        """
        def all_subsets_dfs(all_subsets, numbers_to_insert, current_set):
            all_subsets.append(current_set)
            if len(numbers_to_insert) == 1:
                all_subsets.append(current_set + numbers_to_insert)
                return

            for num in numbers_to_insert:
                new_numbers_to_insert = numbers_to_insert[:]
                new_numbers_to_insert.remove(num)
                all_subsets_dfs(all_subsets, new_numbers_to_insert, current_set + [num])

        all_subsets = []
        all_subsets_dfs(all_subsets, unique_numbers, [])
        return all_subsets
