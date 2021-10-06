# bounce.py
#
# Exercise 1.5

ORIGINAL_DROP = 100
bounce = ORIGINAL_DROP
bounce_hight = 3/5

for bounces in range(10):
    bounce = bounce * bounce_hight
    bounce = round(bounce, 4)
    print(bounces + 1, bounce)
