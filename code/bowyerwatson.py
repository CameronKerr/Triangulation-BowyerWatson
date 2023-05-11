# Cameron Kerr: May 11 2023 #
# Generates triangulaiton using bowyer watson algorithm #

import math
import matplotlib.pyplot as plt

class Point:
    def __init__(self, x, y):
        '''
        Initializes the x and y coordinates for the point
        '''
        self.x = x
        self.y = y
    def distance(self, p):
        '''
        Returns the distance between self and p
        '''
        return math.sqrt((p.x - self.x)**2 + (p.y - self.y)**2)
        
    def plot_point(self):
        '''
        Plots x,y coordinates of self
        '''
        plt.plot([self.x], [self.y], 'ro')
        
class Triangle:
    def __init__(self, p1, p2, p3):
        '''
        Initializes points, edges, and rearranges order until points are in a
        counter-clockwise order
        '''
        self.points = [p1, p2, p3]
        self.edges = [(p1, p2), (p1, p3), (p2,p3)]
        while self.ccw():
            self.points = [p1, p3, p2]
    
    def ccw(self):
        '''
        Returns whether self's points are in clockwise order
        '''
        p1 = self.points[0]
        p2 = self.points[1]
        p3 = self.points[2]
        return ((p2.x - p1.x)*(p3.y - p1.y) - (p3.x - p1.x)*(p2.y - p1.y)) > 0
    
    def in_circumcircle(self, p4):
        '''
        Checks if p4 is in the circumcircle created by the triangle self
        '''
        p1, p2, p3 = self.points
        d1x = p1.x - p4.x
        d1y = p1.y - p4.y
        d2x = p2.x - p4.x
        d2y = p2.y - p4.y
        d3x = p3.x - p4.x
        d3y = p3.y - p4.y
        det = ((d1x*d1x + d1y*d1y) * (d2x*d3y-d3x*d2y) - 
               (d2x*d2x + d2y*d2y) * (d1x*d3y-d3x*d1y) + 
               (d3x*d3x + d3y*d3y) * (d1x*d2y-d2x*d1y)) 
        return det < 0       

    def plot_triangle(self):
        '''
        Plots closed triangle self
        '''
        plt.plot([self.points[0].x, self.points[1].x, self.points[2].x, self.points[0].x], 
                 [self.points[0].y, self.points[1].y, self.points[2].y, self.points[0].y], "ro-")
    
def bowyer_watson(points, testing = False):
    '''
    Plots the delaunay triangulation of points using the bowyer watson algorithm
    '''
    # Sorts all points in terms of x coordinate
    points.sort(key=lambda p: p.x)
    
    # Generates super triangle to surround all points
    min_x = min(point.x for point in points)
    min_y = min(point.y for point in points)
    max_x = max(point.x for point in points)
    max_y = max(point.y for point in points)
    
    # Calculate the ranges for x and y
    range_x = max_x - min_x
    range_y = max_y - min_y
    
    # Find the maximum range value
    max_range = max(range_x, range_y)
    
    # Calculate the center point of the range
    center_x = (min_x + max_x) / 2
    center_y = (min_y + max_y) / 2
    
    # Calculate the vertices of the super-triangle
    p1 = Point(center_x - 20 * max_range, center_y - max_range)
    p2 = Point(center_x, center_y + 20 * max_range)
    p3 = Point(center_x + 20 * max_range, center_y - max_range)
    
    super_triangle = Triangle(p1, p2, p3)
    
    # Initial triangulation is the super_triangle
    triangles = [super_triangle]
    
    # Loop over all points
    for point in points:
        bad_triangles = []
        bad_edges = []
        # Loop over triangles to check if point is in its circumcircle
        for triangle in triangles:
            if triangle.in_circumcircle(point):
                bad_triangles.append(triangle)
        polygon = []
        # Get boundary of the new polygon boundary
        for triangle in bad_triangles:
            not_triangle = [x for x in bad_triangles if x != triangle]
            for edge in triangle.edges:
                shared_count = 0
                for other_triangle in not_triangle:
                    for other_edge in other_triangle.edges:
                        if set(edge) == set(other_edge):
                            shared_count += 1
                if shared_count == 0:
                    polygon.append(edge)
        # Remove bad triangles
        for triangle in bad_triangles:
            triangles.remove(triangle)
        for edge in polygon:
            triangle = Triangle(edge[0], edge[1], point)
            triangles.append(triangle)

    # Remove triangles which share boundaries with the super triangle
    triangles_to_remove = []
    for i in range(len(triangles)):
        triangle = triangles[i]
        for point in triangle.points:
            if point in super_triangle.points:
                triangles_to_remove.append(i)
    
    for index in sorted(list(set(triangles_to_remove)), reverse=True):
        del triangles[index]
        
    # Double check for non-delaunay triangles
    for triangle in triangles:
        for point in points:
            if triangle.in_circumcircle(point):
                return "Error: Non-delaunay triangle"
    if testing == False:
        # Plot triangles
        for triangle in triangles:
            triangle.plot_triangle()

if __name__ == '__main__':
    
    import random
    
    n = input("How many points would you like to generate?")
    # Generate random sample point data
    num_points = int(n)  # Number of points
    min_coord = 0  # Minimum coordinate value
    max_coord = 1000  # Maximum coordinate value
    
    points = []
    x_list = []
    y_list = []
    for _ in range(num_points):
        x = random.uniform(min_coord, max_coord)
        y = random.uniform(min_coord, max_coord)
        point = Point(x, y)
        points.append(point)
    bowyer_watson(points)
    plt.show()