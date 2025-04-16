import sys, math

# counts distance from two points in sphere using vincenti formula

r = 6378.137
f1, l1, f2, l2 = float(sys.argv[1]),float(sys.argv[2]),float(sys.argv[3]),float(sys.argv[4])

f1 = f1 * math.pi / 180
l1 = l1 * math.pi / 180
f2 = f2 * math.pi / 180
l2 = l2 * math.pi / 180

dl = abs(l1 - l2)

delta = math.atan2((math.sqrt((math.cos(f2)*math.sin(dl))**2+(math.cos(f1)*math.sin(f2)-math.sin(f1)*math.cos(f2)*math.cos(dl))**2)), (math.sin(f1)*math.sin(f2)+math.cos(f1)*math.cos(f2)*math.cos(dl)))

print(str(int(r * delta)))