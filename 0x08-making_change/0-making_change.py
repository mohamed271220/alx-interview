#!/usr/bin/python3

"""
    a function that returns the fewest number of coins needed to meet a total
"""


def makeChange(coins, total):
    """
    Returns: fewest number of coins needed to meet total
        If total is 0 or less, return 0
        If total cannot be met by any number of coins you have, return -1
    """
    if not coins or coins is None:
        return -1
    if total <= 0:
        return 0
    change = 0
    coins = sorted(coins)[::-1]
    for coin in coins:
        while coin <= total:
            total -= coin
            change += 1
        if total == 0:
            return change
    return -1

# /**
#  * A function that returns the fewest number of coins needed to meet a total
#  */

# function makeChange(coins: number[], total: number): number {
#     /**
#      * Returns: fewest number of coins needed to meet total
#      * If total is 0 or less, return 0
#      * If total cannot be met by any number of coins you have, return -1
#      */
#     if (!coins || coins.length === 0) {
#         return -1;
#     }
#     if (total <= 0) {
#         return 0;
#     }
#     let change = 0;
#     coins = coins.sort((a, b) => b - a);
#     for (let coin of coins) {
#         while (coin <= total) {
#             total -= coin;
#             change += 1;
#         }
#         if (total === 0) {
#             return change;
#         }
#     }
#     return -1;
# }