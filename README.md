# convexhull
In geometry, the convex hull or convex envelope or convex closure of a shape is the smallest convex set that contains it. The convex hull may be defined either as the intersection of all convex sets containing a given subset of a Euclidean space, or equivalently as the set of all convex combinations of points in the subset. For a bounded subset of the plane, the convex hull may be visualized as the shape enclosed by a rubber band stretched around the subset.
This program find the convex hull of any given set of points in the form of the file below. Data is recorded as ASCII text in the output file also. Definition of the Convex Hull is given as "the smallest convex shape containing a set of 2D points” or “to define the boundaries of a set of 2D points”. The order of the convex hull points should be in the form of a clockwise or anti-clockwise polygon order.
The Structure of the Coordinate Data Set File
16
1 4.4 14.0
2 6.7 15.25
3 6.9 12.8
4 2.1 11.1
...
Where the first line(16) indicates the number of coordinates, the first number in the line is point ID, the second number in the line is X coordinate, the third number in the line is Y coordinate. Every coordinate has seperated by spaces(4 space).

The Structure of Output File
14
6
5
2
1
...
Where each line is point ID of the convex hull in correct order.

PseudoCode
Input: a list P of points in the plane.
Precondition: There must be at least 3 points.
Sort the points of P by x-coordinate (in case of a tie, sort by y-coordinate).
Initialize U and L as empty lists.
The lists will hold the vertices of upper and lower hulls respectively.
for i = 1, 2, ..., n:
while L contains at least two points and the sequence of last two points
of L and the point P[i] does not make a counter-clockwise turn:
remove the last point from L
append P[i] to L
for i = n, n-1, ..., 1:
while U contains at least two points and the sequence of last two points
of U and the point P[i] does not make a counter-clockwise turn:
remove the last point from U
append P[i] to U
Remove the last point of each list (it's the same as the first point of the other list).
Concatenate L and U to obtain the convex hull of P.
Points in the result will be listed in counter-clockwise order.
