# For example, suppose you had the following report:
#
# 199
# 200
# 208
# 210
# 200
# 207
# 240
# 269
# 260
# 263
# 190
# 188
# 186
# 185
# 184
# 184
# 176
# 174
# 173
# 172
# (...)
#
# In this example, there are 7 measurements that are larger \
# than the previous measurement.
#
# How many measurements are larger than the previous measurement?


def solve(measurements):
    count = 0
    for i in range(1, len(measurements)):
        if measurements[i] > measurements[i - 1]:
            count += 1
    return count


measurements = [
    199,
    200,
    208,
    210,
    200,
    207,
    240,
    269,
    260,
    263,
    190,
    188,
    186,
    185,
    184,
    184,
    176,
    174,
    173,
    172,
]

print(
    f"The number of numbers larger than the preceeding number is: {solve(measurements)}"
)
