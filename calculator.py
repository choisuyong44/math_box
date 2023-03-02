# ## Brute-Force Attack (무차별 대입 공격)
# def max_product(left_cards, right_cards):
#     product = []
#
#     for i in range(len(left_cards)):
#         for j in range(len(right_cards)):
#             product.append(left_cards[i] * right_cards[j])
#
#     return max(product)
#
# # 테스트 코드
# print(max_product([1, 6, 5], [4, 2, 3]))
# print(max_product([1, -9, 3, 4], [2, 8, 3, 1]))
# print(max_product([-1, -7, 3], [-4, 3, 6]))

# 제곱근 사용을 위한 sqrt 함수
# from math import sqrt
#
# # 두 매장의 직선 거리를 계산해 주는 함수
# def distance(store1, store2):
#     return sqrt((store1[0] - store2[0]) ** 2 + (store1[1] - store2[1]) ** 2)

# # 가장 가까운 두 매장을 찾아주는 함수
# def closest_pair(coordinates):
#     shortest = distance(coordinates[0], coordinates[1])
#     for a in range(0, len(coordinates)):
#         for b in range((a + 1), len(coordinates)):
#             if distance(coordinates[a], coordinates[b]) < shortest:
#                 shortest_coordinates = [coordinates[a], coordinates[b]]
#                 shortest = distance(coordinates[a], coordinates[b]) #
#                 return
# # 테스트 코드
#
# test_coordinates = [(2, 3), (12, 30), (40, 50), (5, 1), (12, 10), (3, 4)]
# print(closest_pair(test_coordinates))
