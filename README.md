# Triangulation-BowyerWatson

# Description
A triangulation of a set of points is the division of the convex hull made from those points into triangles. A Delaunay triangulation is a type of triangulation in which no points lie inside the circumcircle created by each triangle. These triangulations have many applications. For example they are used to created triangulated irregular networks which give a vector representation of a 3D surface in GIS applications.

The Bowyer Watson algorithm is a method for constructing a delaunay triangulation for a set of finite points. It works in the following steps:
1. A super triangle is created such that all points are contained within the super triangle. There are many ways of doing so, depending on if they points are defined in a certain area or not and how efficient you need to be.
2. Points in the set are added one at a time, adding triangles extending from the point to the polygon hole's edge. The triangles which contain the new point in its circumcircle are deleted, creating a new polygon hole.
3. Afer all points are added, triangles which are touching the super triangle are deleted, leaving a delaunay triangulation of the set of points.

---
# Organization

## Tree
```bash
code
   |-- bowyerwatson.py
   |-- runtimevis.py
results
   |-- BowyerWatson_runtime.png
   |-- n100Triangulation.png
   |-- n15Triangulation.png
   |-- n50Triangulation.png
   |-- n5Triangulation.png
```
# Running the project

To run the project download the repository and run:
```
python3 bowyerwatson.py
```
You will then be prompted to enter the desired number of points to be randomly generated and visualized. Once picked the program will run and generate the visualization in a separate window.

To generate an analysis on the runtime complexity of the algorithm download the repository and run:
```
python3 runtimevis.py
```
---
# Results

n = 5                      |  n = 15                   | n = 50
:-------------------------:|:-------------------------:|:-------------------------:|
![](https://github.com/CameronKerr/Triangulation-BowyerWatson/blob/main/results/n5Triangulation.png)  |  ![](https://github.com/CameronKerr/Triangulation-BowyerWatson/blob/main/results/n15Triangulation.png) | ![](https://github.com/CameronKerr/Triangulation-BowyerWatson/blob/main/results/n50Triangulation.png)

![](https://github.com/CameronKerr/Triangulation-BowyerWatson/blob/main/results/BowyerWatson_runtime.png)
