
from unittest import TestCase
from rank_a_list import rank_a_list

class TestGlobaliR(TestCase):
    def test_1_get_rank(self):
        """
        Testing get the correct rank
        :return:
        """
        input_list = [100, 90, 90, 80, 75, 60]
        list_tobe_ranked = [50, 65, 77, 90, 102]
        rank = rank_a_list(input_list, list_tobe_ranked)
        self.assertEqual(rank, [6, 5, 4, 2, 1])
    def test_2_get_same_rank(self):
        """
        Test if we will get the same rank 
        if the list to be ranked is smaller than all elements
        """
        input_list = [100, 90, 90, 80, 75, 60]
        list_tobe_ranked = [0,1,2,3,4]
        rank = rank_a_list(input_list, list_tobe_ranked)
        self.assertEqual(rank, [6, 6, 6, 6, 6])

    def test_3_get_same_rank(self):
        """
        Test if we will get the same rank 
        if the list to be ranked is greater than all elements
        """
        input_list = [100, 90, 90, 80, 75, 60]
        list_tobe_ranked = [101,111,211,311,411]
        rank = rank_a_list(input_list, list_tobe_ranked)
        self.assertEqual(rank, [1, 1, 1, 1, 1])

    def test_4_get_same_rank(self):
        """
        Test if we will get the same rank 
        if the list provided has the same values
        """
        input_list = [100, 100, 100, 100, 100]
        list_tobe_ranked = [33,31,25,21,4]
        rank = rank_a_list(input_list, list_tobe_ranked)
        self.assertEqual(rank, [2, 2, 2, 2, 2])


    def test_5_get_correct_rank(self):
        """
        Test if we will get a correct rank
        if the list to be ranked is not sorted
        """
        input_list = [100, 90, 90, 80, 75, 60]
        list_tobe_ranked = [50, 65, 77, 90, 102]
        list_tobe_ranked.reverse()
        rank = rank_a_list(input_list, list_tobe_ranked)
        expected_list = [6, 5, 4, 2, 1]
        expected_list.reverse()
        self.assertEqual(rank, expected_list)

