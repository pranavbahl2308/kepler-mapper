import km

data = km.np.genfromtxt('cat-reference.csv',delimiter=',')

mapper = km.KeplerMapper()


lens = mapper.fit_transform(data)

graph = mapper.map(lens,
                   data,
                   clusterer=km.cluster.DBSCAN(eps=0.1, min_samples=5),
                   nr_cubes=15,
                   overlap_perc=0.2)

mapper.visualize(graph,
                path_html="cat_keplermapper_output.html")

# You may want to visualize the original point cloud data in 3D scatter too
"""
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(data[:,0],data[:,1],data[:,2])
plt.savefig("cat-reference.csv.png")
plt.show()
"""
