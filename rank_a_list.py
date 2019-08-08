
def rank_a_list(original_list, list_to_be_ranked):
    #We need to remove duplicate number from list
    temp_list = list(dict.fromkeys(original_list.copy()))
    rank = [1] * len(list_to_be_ranked)
    for i, n_2 in enumerate(list_to_be_ranked):
        for n_1 in temp_list:
            if n_2 < n_1:
                rank[i] += 1
                continue
    return rank


#Example
# rank_a_list([100, 90, 90, 80, 75, 60], [50, 65, 77, 90, 102])
# will return [6, 5, 4, 2, 1]
