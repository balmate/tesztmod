from algorithms.dp import (
    max_profit_naive, max_profit_optimized,
    climb_stairs, climb_stairs_optimized,
    count,
    combination_sum_topdown, combination_sum_bottom_up,
    edit_distance,
    egg_drop,
    fib_recursive, fib_list, fib_iter,
    hosoya_testing, print_hosoya,
    house_robber,
    Job, schedule,
    Item, get_maximum_value,
    longest_increasing_subsequence,
    longest_increasing_subsequence_optimized,
    longest_increasing_subsequence_optimized2,
    subarray_with_max_product,
    min_cost,
    num_decodings, num_decodings2,
    int_divide,find_k_factor,
    planting_trees, regex_matching,
    word_break
)


import io
import unittest
import unittest.mock


class TestBuySellStock(unittest.TestCase):
    def test_max_profit_naive(self):
        self.assertEqual(max_profit_naive([7, 1, 5, 3, 6, 4]), 5)
        self.assertEqual(max_profit_naive([7, 6, 4, 3, 1]), 0)

    def test_max_profit_optimized(self):
        self.assertEqual(max_profit_optimized([7, 1, 5, 3, 6, 4]), 5)
        self.assertEqual(max_profit_optimized([7, 6, 4, 3, 1]), 0)


class TestClimbingStairs(unittest.TestCase):
    def test_climb_stairs(self):
        self.assertEqual(climb_stairs(2), 2)
        self.assertEqual(climb_stairs(10), 89)

    def test_climb_stairs_optimized(self):
        self.assertEqual(climb_stairs_optimized(2), 2)
        self.assertEqual(climb_stairs_optimized(10), 89)


class TestCoinChange(unittest.TestCase):
    def test_count(self):
        self.assertEqual(count([1, 2, 3], 4), 4)
        self.assertEqual(count([2, 5, 3, 6], 10), 5)


class TestCombinationSum(unittest.TestCase):
    def test_combination_sum_topdown(self):
        self.assertEqual(combination_sum_topdown([1, 2, 3], 4), 7)

    def test_combination_sum_bottom_up(self):
        self.assertEqual(combination_sum_bottom_up([1, 2, 3], 4), 7)


class TestEditDistance(unittest.TestCase):
    def test_edit_distance(self):
        self.assertEqual(edit_distance('food', 'money'), 4)
        self.assertEqual(edit_distance('horse', 'ros'), 3)


class TestEggDrop(unittest.TestCase):
    def test_egg_drop(self):
        self.assertEqual(egg_drop(1, 2), 2)
        self.assertEqual(egg_drop(2, 6), 3)
        self.assertEqual(egg_drop(3, 14), 4)


class TestFib(unittest.TestCase):
    def test_fib_recursive(self):
        self.assertEqual(fib_recursive(10), 55)
        self.assertEqual(fib_recursive(30), 832040)

    def test_fib_list(self):
        self.assertEqual(fib_list(10), 55)
        self.assertEqual(fib_list(30), 832040)

    def test_fib_iter(self):
        self.assertEqual(fib_iter(10), 55)
        self.assertEqual(fib_iter(30), 832040)

    def test_fib_iter_1(self):
        self.assertEqual(fib_iter(1), 1)


class TestHosoyaTriangle(unittest.TestCase):
    """[summary]
    Test for the file hosoya_triangle

    Arguments:
        unittest {[type]} -- [description]
    """

    def test_hosoya(self):
        self.assertEqual([1], hosoya_testing(1))
        self.assertEqual([1,
                         1, 1,
                         2, 1, 2,
                         3, 2, 2, 3,
                         5, 3, 4, 3, 5,
                         8, 5, 6, 6, 5, 8],
                         hosoya_testing(6))
        self.assertEqual([1,
                          1, 1,
                          2, 1, 2,
                          3, 2, 2, 3,
                          5, 3, 4, 3, 5,
                          8, 5, 6, 6, 5, 8,
                          13, 8, 10, 9, 10, 8, 13,
                          21, 13, 16, 15, 15, 16, 13, 21,
                          34, 21, 26, 24, 25, 24, 26, 21, 34,
                          55, 34, 42, 39, 40, 40, 39, 42, 34, 55],
                         hosoya_testing(10))

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_print_hosoya(self, mock_stdout: io.StringIO):
        print_hosoya(3)
        self.assertEqual("1 \n1 1 \n2 1 2 \n", mock_stdout.getvalue())


class TestHouseRobber(unittest.TestCase):
    def test_house_robber(self):
        self.assertEqual(44, house_robber([1, 2, 16, 3, 15, 3, 12, 1]))


class TestJobScheduling(unittest.TestCase):
    def test_job_scheduling(self):
        job1, job2 = Job(1, 3, 2), Job(2, 3, 4)
        self.assertEqual(4, schedule([job1, job2]))


class TestKnapsack(unittest.TestCase):
    def test_get_maximum_value(self):
        item1, item2, item3 = Item(60, 10), Item(100, 20), Item(120, 30)
        self.assertEqual(220, get_maximum_value([item1, item2, item3], 50))

        item1, item2, item3, item4 = Item(60, 5), Item(50, 3), Item(70, 4), Item(30, 2)
        self.assertEqual(80, get_maximum_value([item1, item2, item3, item4],
                                               5))


class TestLongestIncreasingSubsequence(unittest.TestCase):
    def test_longest_increasing_subsequence(self):
        sequence = [1, 101, 10, 2, 3, 100, 4, 6, 2]
        self.assertEqual(5, longest_increasing_subsequence(sequence))


class TestLongestIncreasingSubsequenceOptimized(unittest.TestCase):
    def test_longest_increasing_subsequence_optimized(self):
        sequence = [1, 101, 10, 2, 3, 100, 4, 6, 2]
        self.assertEqual(5, longest_increasing_subsequence_optimized(sequence))


class TestLongestIncreasingSubsequenceOptimized2(unittest.TestCase):
    def test_longest_increasing_subsequence_optimized2(self):
        sequence = [1, 101, 10, 2, 3, 100, 4, 6, 2]
        self.assertEqual(5, longest_increasing_subsequence_optimized2(sequence))


class TestMaxProduct(unittest.TestCase):
    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_subarray_with_max_product(self, mock_stdout: io.StringIO):
        subarray_with_max_product([2,3,6,-1,-1,9,5])
        self.assertEqual("max_product_so_far: 45, [-1, -1, 9, 5]\n", mock_stdout.getvalue())

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_subarray_with_max_product_all_negative(self, mock_stdout: io.StringIO):
        subarray_with_max_product([-4,-3,-2,-1])
        self.assertEqual("max_product_so_far: 24, [-4, -3, -2, -1]\n", mock_stdout.getvalue())


class TestMinCostPath(unittest.TestCase):
    def test_min_cost(self):
        costs = [
            [ 0, 15, 80, 90],
            [-1,  0, 40, 50],
            [-1, -1,  0, 70],
            [-1, -1, -1,  0]
        ]
        self.assertEqual(65, min_cost(costs))


class TestNumDecodings(unittest.TestCase):
    def test_num_decodings(self):
        self.assertEqual(2, num_decodings("1024"))

    def test_num_decodings_0(self):
        self.assertEqual(0, num_decodings("0"))

    def test_num_decodings2(self):
        self.assertEqual(2, num_decodings2("1024"))

    def test_num_decodings2_0(self):
        self.assertEqual(0, num_decodings2("0"))


class TestIntDivide(unittest.TestCase):
    def test_int_divide(self):
        self.assertEqual(5, int_divide(4))
        self.assertEqual(42, int_divide(10))
        self.assertEqual(204226, int_divide(50))


class Test_dp_K_Factor(unittest.TestCase):
    def test_kfactor(self):
        # Test 1
        n1 = 4
        k1 = 1
        self.assertEqual(find_k_factor(n1, k1), 1)

        # Test 2
        n2 = 7
        k2 = 1
        self.assertEqual(find_k_factor(n2, k2), 70302)

        # Test 3
        n3 = 10
        k3 = 2
        self.assertEqual(find_k_factor(n3, k3), 74357)

        # Test 4
        n4 = 8
        k4 = 2
        self.assertEqual(find_k_factor(n4, k4), 53)

        # Test 5
        n5 = 9
        k5 = 1
        self.assertEqual(find_k_factor(n5, k5), 71284044)

    def test_kfactor_n1_k1(self):
        self.assertEqual(find_k_factor(1, 1), 0)


class TestPlantingTrees(unittest.TestCase):
    def test_simple(self):
        # arrange
        trees = [0, 1, 10, 10]
        L = 10
        W = 1

        # act
        res = planting_trees(trees, L, W)

        # assert
        self.assertEqual(res, 2.414213562373095)

    def test_simple2(self):
        # arrange
        trees = [0, 3, 5, 5, 6, 9]
        L = 10
        W = 1

        # act
        res = planting_trees(trees, L, W)

        # assert
        self.assertEqual(res, 9.28538328578604)
    
class TestRegexMatching(unittest.TestCase):
    def test_none_0(self):
        s = ""
        p = ""
        self.assertTrue(regex_matching.is_match(s, p))

    def test_none_1(self):
        s = ""
        p = "a"
        self.assertFalse(regex_matching.is_match(s, p))

    def test_no_symbol_equal(self):
        s = "abcd"
        p = "abcd"
        self.assertTrue(regex_matching.is_match(s, p))

    def test_no_symbol_not_equal_0(self):
        s = "abcd"
        p = "efgh"
        self.assertFalse(regex_matching.is_match(s, p))

    def test_no_symbol_not_equal_1(self):
        s = "ab"
        p = "abb"
        self.assertFalse(regex_matching.is_match(s, p))

    def test_symbol_0(self):
        s = ""
        p = "a*"
        self.assertTrue(regex_matching.is_match(s, p))

    def test_symbol_1(self):
        s = "a"
        p = "ab*"
        self.assertTrue(regex_matching.is_match(s, p))

    def test_symbol_2(self):
        # E.g.
        #   s a b b
        # p 1 0 0 0
        # a 0 1 0 0
        # b 0 0 1 0
        # * 0 1 1 1
        s = "abb"
        p = "ab*"
        self.assertTrue(regex_matching.is_match(s, p))


class TestWordBreak(unittest.TestCase):
    def test_word_break_true(self):
        self.assertEqual(True, word_break("helloworld", ["hello", "world"]))

    def test_word_break_false(self):
        self.assertEqual(False, word_break("abc", ["a", "b"]))


if __name__ == '__main__':
    unittest.main()
