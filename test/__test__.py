# import tqdm
# from time import sleep
# n = 10
# g = (i for i in tqdm.tqdm(range(n), ascii="0123456789X"))
# for i in range(n):
#     print(i, end="\r")
#     sleep(.1)
#     next(g)


# Print iterations progress
# import time


# def printProgressBar(iteration, total, prefix='', suffix='', decimals=1, length=100, fill='█', printEnd="\r"):
#     """
#     Call in a loop to create terminal progress bar
#     @params:
#         iteration   - Required  : current iteration (Int)
#         total       - Required  : total iterations (Int)
#         prefix      - Optional  : prefix string (Str)
#         suffix      - Optional  : suffix string (Str)
#         decimals    - Optional  : positive number of decimals in percent complete (Int)
#         length      - Optional  : character length of bar (Int)
#         fill        - Optional  : bar fill character (Str)
#         printEnd    - Optional  : end character (e.g. "\r", "\r\n") (Str)
#     """
#     percent = ("{0:." + str(decimals) + "f}").format(100 *
#                                                      (iteration / float(total)))
#     filledLength = int(length * iteration // total)
#     bar = fill * filledLength + '-' * (length - filledLength)
#     print(f'\r{prefix} |{bar}| {percent}% {suffix}', end=printEnd)
#     # Print New Line on Complete
#     if iteration == total:
#         print()


# # A List of Items
# items = list(range(0, 57))
# l = len(items)

# # Initial call to print 0% progress
# printProgressBar(0, l, prefix='Progress:', suffix='Complete', length=50)
# for i, item in enumerate(items):
#     # Do stuff...
#     time.sleep(0.1)
#     # Update Progress Bar
#     printProgressBar(i + 1, l, prefix='Progress:',
#                      suffix='Complete', length=50)

import os
from string import punctuation
# print(all([1, 2, 3, 4]) in [1, 2, 3, 4])

# for item in os.listdir("/home/flu/Project/module/test"):
#     t = str.maketrans(" ", " ", punctuation)
#     item = item[:item.rfind(".")]
#     item = item.translate(t)
#     # print("item: ", item, "\n",
#     #       "download_name: ", download_name)
#     des = [i.strip() for i in item.split()]
#     print(des)
import sys

print(sys.argv[1] if len(sys.argv) > 1 else 2)
