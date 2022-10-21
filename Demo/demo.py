# import threading
# import time
#
# start = time.perf_counter()
#
# def do_something():
#     time.sleep(1)
#
# t1 = threading.Thread(target=do_something)
# t2 = threading.Thread(target=do_something)
#
# t1.start()
# t2.start()
#
# t1.join()
# t2.join()
#
#
# finish = time.perf_counter()
#
# print(f"Total time taken: {round(finish - start)}s")

prices = [1, 3, 6, 9, 0, 7, 299, 979, 8479]
k = 2

newPrices = [-1] * len(prices)
# for i in range(len(prices)):
#     greater = []
#     j = i + 1
#
#     while j < len(prices) and len(greater) < k:
#         if prices[j] > prices[i]:
#             greater.append(prices[j])
#
#         j += 1
#
#     if len(greater) == k:
#         newPrices[i] = greater.pop()

print(newPrices)


