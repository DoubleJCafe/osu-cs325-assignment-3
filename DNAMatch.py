# Name: Joshua Jansen
# OSU Email: Jansejos@oregonstate.edu
# Course: CS325_402
# Homework 3: Dynamic Programming

def dna_match_topdown(DNA1, DNA2):
    """
    Tests two strings for their longest common subsequence utilizing a top-down approach.
    :param DNA1: String.
    :param DNA2: String.
    :return: Integer representing the length of the longest common subsequence.
    """
    m = len(DNA1)
    n = len(DNA2)
    cache = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
    return dna_match_topdown_helper(DNA1, DNA2, m, n, cache)


def dna_match_topdown_helper(DNA1, DNA2, m, n, cache):
    """
    Helper function for dna_match_topdown.
    :param DNA1: String.
    :param DNA2: String.
    :param m: Length of param DNA1.
    :param n: Length of param DNA2.
    :param cache: 2-D array to store already computed subproblems.
    :return: Integer representing the length of the longest common subsequence.
    """
    if m == 0 or n == 0:
        return 0

    if cache[m][n] != 0:
        return cache[m][n]
    if DNA1[m - 1] == DNA2[n - 1]:
        cache[m][n] = 1 + dna_match_topdown_helper(DNA1, DNA2, m - 1, n - 1, cache)
        return cache[m][n]
    else:
        cache[m][n] = max(dna_match_topdown_helper(DNA1, DNA2, m - 1, n, cache),
                          dna_match_topdown_helper(DNA1, DNA2, m, n - 1, cache))
        return cache[m][n]


def dna_match_bottomup(DNA1, DNA2):
    """
    Tests two strings for their longest common subsequence utilizing a bottom-up approach.
    :param DNA1: String.
    :param DNA2: String.
    :return: Integer representing the length of the longest common subsequence.
    """
    m = len(DNA1)
    n = len(DNA2)
    cache = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0 or j == 0:
                cache[i][j] = 0
            elif DNA1[i - 1] == DNA2[j - 1]:
                cache[i][j] = cache[i - 1][j - 1] + 1
            else:
                cache[i][j] = max(cache[i - 1][j], cache[i][j - 1])
    return cache[m][n]

