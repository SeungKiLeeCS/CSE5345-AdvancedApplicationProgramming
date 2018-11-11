import matrix
import matplotlib.pyplot as plt

"""
@moduledoc

Creates a matrix with random integers
Transposes the matrix 3 ways and prints the results
Prints and graphs the results
"""

# Small
# s = matrix.np.random.rand(200,200)
# small = matrix.Matrix(s)
# small_simple = small.transpose()
# small_zip = small.zip_transpose()
# small_numpy = small.numpy_transpose()
# print('Small.Simple: {0:.7f} sec'.format(small_simple))
# print('Small.Zip:    {0:.7f} sec'.format(small_zip))
# print('Small.Numpy:  {0:.7f} sec'.format(small_numpy))
# print("")
sx = ["simple", "zip", "numpy"]
sy = [0.0325670, 0.0001280, 0.0000136]
fig = plt.figure(figsize=(10,12))
plt.bar(sx, sy, color='red')
plt.xlabel("Transpose Algorithms")
plt.ylabel("Time")
plt.title("Small Matrix")
ax = fig.add_subplot(111)
for i,j in zip(sx,sy):
    ax.annotate(str("{0:.7f}".format(j)),xy=(i,j))
plt.show()

# Medium
# m = matrix.np.random.rand(2000,2000)
# medium = matrix.Matrix(m)
# medium_simple = medium.transpose()
# medium_zip = medium.zip_transpose()
# medium_numpy = medium.numpy_transpose()
# print('Medium.Simple: {0:.7f} sec'.format(medium_simple))
# print('Medium.Zip:    {0:.7f} sec'.format(medium_zip))
# print('Medium.Numpy:  {0:.7f} sec'.format(medium_numpy))
# print("")
mx = ["simple", "zip", "numpy"]
my = [1.8836133,  0.0077522, 0.0000145]
fig = plt.figure(figsize=(10,12))
plt.bar(mx, my, color='red')
plt.xlabel("Transpose Algorithms")
plt.ylabel("Time")
plt.title("Medium Matrix")
ax = fig.add_subplot(111)
for i,j in zip(mx,my):
    ax.annotate(str("{0:.7f}".format(j)),xy=(i,j))
plt.show()


# Large
# l = matrix.np.random.rand(20000,20000)
# large = matrix.Matrix(l)
# large_simple = large.transpose()
# large_zip = large.zip_transpose()
# large_numpy = large.numpy_transpose()
# print('Large.Simple: {0:.7f} sec'.format(large_simple))
# print('Large.Zip:    {0:.7f} sec'.format(large_zip))
# print('Large.Numpy:  {0:.7f} sec'.format(large_numpy))
# print("")
lx = ["simple", "zip", "numpy"]
ly = [109.8974702, 0.0053387, 0.0000145]
fig = plt.figure(figsize=(10,12))
plt.bar(lx, ly, color='red')
plt.xlabel("Transpose Algorithms")
plt.ylabel("Time")
plt.title("Large Matrix")
ax = fig.add_subplot(111)
for i,j in zip(lx,ly):
    ax.annotate(str("{0:.7f}".format(j)),xy=(i,j))
plt.show()


# Really Large
# r = matrix.np.random.rand(50000,50000)
# really = matrix.Matrix(r)
# really_simple = really.transpose()
# really_zip = really.zip_transpose()
# really_numpy = really.numpy_transpose()
# print('ReallyLarge.Simple: {0:.7f} sec'.format(really_simple))
# print('ReallyLarge.Zip:    {0:.7f} sec'.format(really_zip))
# print('ReallyLarge.Numpy:  {0:.7f} sec'.format(really_numpy))
# print("")
rx = ["simple", "zip", "numpy"]
ry = [712.7052824, 0.0239172, 0.0000145]
fig = plt.figure(figsize=(10,12))
plt.bar(rx, ry, color='red')
plt.xticks(sx)
plt.xlabel("Transpose Algorithms")
plt.ylabel("Time")
plt.title("Really Large Matrix")
ax = fig.add_subplot(111)
for i,j in zip(rx,ry):
    ax.annotate(str("{0:.7f}".format(j)),xy=(i,j))
plt.show()

fullx = ["small (200x200)", "medium(2000x2000)", "large(20000x20000)", "reallylarge(50000x50000)"]
simpley = [sy[0], my[0], ly[0], ry[0]]
zipy = [sy[1], my[1], ly[1], ry[1]]
numpyy= [sy[2], my[2], ly[2], ry[2]]
df = pd.dataframe({"fullx": range(0, 720), "simpley": simpley, "zipy": zipy, "numpyy"=numpyy})

plt.plot( 'fullx', 'simpley', marker='o', markerfacecolor='red', markersize=6, color='red', linewidth=2, label="simple")
plt.plot( 'fullx', 'zipy', marker='o', markerfacecolor='blue', color='blue', linewidth=2, label="zip")
plt.plot( 'fullx', 'numpyy', marker='o', markerfacecolor='gold', color='gold', linewidth=2, linestyle='dashed', label="numpy")
plt.legend()
