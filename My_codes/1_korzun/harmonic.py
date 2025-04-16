import sys, math

# counts approximate value of harmonic row using Nuton method and Eular formula

a = float(sys.argv[1])

l = 0.5772156649_0153286060_6512090082_4024310421_5933593992_3598805767_2348848677_2677766467_0936947063_2917467495_1463144724_9807082480_9605040144_8654283622_4173997644_9235362535_0033374293_7337737673_9427925952_5824709491_6008735203_9481656708_5323315177_6611528621

xp = 1
f = - a + math.log(xp) + l
eps = 0.1
xn = xp + eps*2

while abs(xn - xp) > eps:
    f = - a + math.log(xn) + l
    df = 1 / xn

    xp = xn
    xn = xn - f / df

    if (int(math.log10(xn)) > int(math.log10(eps))+12): # <- This is for approximate answer for big numbers (shows first 12 digits of number)
        eps = 10**(int(math.log10(xn)) - 12)

if (eps >= 1):
    xp = int(xp/eps)*eps

print(round(xp))