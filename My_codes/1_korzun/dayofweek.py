import sys

y, m, d = int(sys.argv[1]),int(sys.argv[2]),int(sys.argv[3])

y1 = y - (14 - m) // 12
x = y1 + y1 // 4 - y1 // 100 + y1 // 400
m1 = m + 12 * ((14 - m) // 12) - 2
d1 = (d + x + 31 * m1 // 12) % 7

is_leap = y % 400 == 0 or (y % 100 != 0 and y % 4 == 0)

days_in_month = 31 if (m == 1 or m == 3 or m == 5 or m == 7 or m == 8 or m == 10 or m == 12) else 28 if (m == 2 and not is_leap) else 29 if (m == 2 and is_leap) else 30

if (m <= 12 and m >= 1 and d >= 1 and d <= days_in_month):
    s = 'Sunday' if d1 == 0 else 'Monday' if d1 == 1 else 'Tuesday' if d1 == 2 else 'Wednesday' if d1 == 3 else 'Thursday' if d1 == 4 else 'Friday' if d1 == 5 else 'Sunday'
else:
    s = 'Invalid date'

print (s)