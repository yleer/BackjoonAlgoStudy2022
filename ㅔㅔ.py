m = 0.1
r = 0.17


m2 = 0.285 * 9.806
w = [11.08,11.67,11.96]

a = []
for i in w:
    # print(m*r*i*i)
    a.append(m*r*i*i)

kk = []
print(a)
for j in a:
    # print(m2,j)
    print((m2 - j) / m2 * 100)
    kk.append((m2 - j) / m2 * 100)

print(sum(kk)/3)
