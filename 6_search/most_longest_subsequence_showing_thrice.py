
def solution(nums):
    freq_map = dict()
    start = 0
    max_sequence_len = 0
    max_sequence_val = 0
    for num_index in range(1, len(nums)):
        if nums[num_index] != nums[num_index-1]:
            # insert sequence to map
            sequence_length = num_index - start
            if nums[num_index-1] not in freq_map:
                freq_map[nums[num_index-1]] = [sequence_length, sequence_length-1, sequence_length-2]
            else: # alrady seen this num
                if sequence_length > max_sequence_len and sequence_length in freq_map[nums[num_index-1]]:
                    # if sequence_length not in map[nums[num_index-1]] there is no way there is higher number there
                    if sequence_length == freq_map[nums[num_index-1]][0]:
                        freq_map[nums[num_index-1]][0] = None
                        freq_map[nums[num_index-1]][1] = sequence_length
                        freq_map[nums[num_index-1]][2] = sequence_length-1
                    elif sequence_length == freq_map[nums[num_index-1]][1]:
                        freq_map[nums[num_index-1]][1] = None
                        freq_map[nums[num_index-1]][2] = sequence_length
                    else:
                        freq_map[nums[num_index-1]][0] = sequence_length
                        freq_map[nums[num_index-1]][1] = sequence_length-1
                        freq_map[nums[num_index-1]][2] = sequence_length-2
                    if freq_map[nums[num_index-1]][2] > max_sequence_len:
                        max_sequence_len = sequence_length
                        max_sequence_val = freq_map[nums[num_index-1]][2]
    if sequence_length > max_sequence_len and sequence_length in freq_map[nums[num_index-1]]:
        # if sequence_length not in map[nums[num_index-1]] there is no way there is higher number there
        if sequence_length == freq_map[nums[num_index-1]][0]:
            freq_map[nums[num_index-1]][0] = None
            freq_map[nums[num_index-1]][1] = sequence_length
            freq_map[nums[num_index-1]][2] = sequence_length-1
        elif sequence_length == freq_map[nums[num_index-1]][1]:
            freq_map[nums[num_index-1]][1] = None
            freq_map[nums[num_index-1]][2] = sequence_length
        else:
            freq_map[nums[num_index-1]][0] = sequence_length
            freq_map[nums[num_index-1]][1] = sequence_length-1
            freq_map[nums[num_index-1]][2] = sequence_length-2
        if freq_map[nums[num_index-1]][2] > max_sequence_len:
            max_sequence_len = sequence_length
            max_sequence_val = freq_map[nums[num_index-1]][2]
    return max_sequence_val
