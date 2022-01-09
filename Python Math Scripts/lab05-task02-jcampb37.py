#1/usr/bin/python3
import math
import statistics

numStr = [38,12,43,144,1024,76,1920,1080,255,1440,93,32,64]
numStr = sorted(numStr)

countStr = len(numStr)

medStr = countStr // 2

print("Max:",max(numStr))
print("Min:",min(numStr))
print("Sum:",sum(numStr))
print("Avg:",round(sum(numStr)/countStr, 2))
# I imported the statistics module for this, otherwise the code would've been heftier
print("Median:",statistics.median(numStr))
