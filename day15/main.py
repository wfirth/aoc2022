import numpy as np
import sympy as symp
import shapely as shap

class Beacon:
    def __init__(self, x, y) :
        self.x = x
        self.y = y

class Sensor:
    def __init__(self, x, y, beacon: Beacon) :
        self.x = x
        self.y = y
        self.beacon = beacon

    def get_manhattan_distance(self):
        xdiff = self.x - self.beacon.x
        ydiff = self.y - self.beacon.y
        mnhtn = abs(xdiff) + abs(ydiff)
        return(mnhtn)

    def build_points(self):
        d = self.get_manhattan_distance()
        return(
            [(self.x + d, self.y),
            (self.x, self.y + d),
            (self.x - d, self.y),
            (self.x, self.y - d)
            ]
        )



def load_file(pth):
    text_file = open(pth, "r")
    data = text_file.read()
    text_file.close()
    return(data)


def split_by_newline(d: str):
    """Split file by newline"""
    splt = d.split("\n")
    return(splt)[:-1]

def strip_to_x_y(line):
    xindex = line.find("x")
    splt_to_x = line[xindex:]
    x,y = splt_to_x.split(", ")
    x = int(x[2:])
    y = int(y[2:])
    return(x, y)

def get_x(line):
    xindex = line.find("x")
    splt_to_x = line[xindex:]
    splt_x = splt_to_x.split(", ")[0]
    x = int(splt_x[2:])
    return(x)

def get_y(line):
    y = int(line[-2:])
    return(y)

def main():
    lines = [line.split(":") for line in  split_by_newline(load_file("day15/input.txt"))]
    sensors = generate_sensors(lines)
    b = solve_pt2(sensors)
    return(b)


def get_intersections(sensors, y_value):
    xmin, xmax = get_x_extents(sensors)
    intersecting_line = symp.Line(symp.Point(xmin, y_value), symp.Point(xmax, y_value))
    intersection_set = []
    beacons_on_line = []

    for sensor in sensors:
        plane = generate_plane(sensor)
        if sensor.beacon.y == y_value:
            beacons_on_line.append((sensor.beacon.x, sensor.beacon.y))
        intersections = plane.intersection(intersecting_line)

        if len(intersections) == 1:
            intersection_set.append((intersections[0].x, intersections[0].y))
        if len(intersections) > 1:
            startx = intersections[0].x
            endx = intersections[1].x
            for i in range(startx, endx+1):
                intersection_set.append((i, intersections[0].y))


    n_intersections = len(set(intersection_set))
    n_overlying_beacons = len(set(beacons_on_line))
    return(n_intersections - n_overlying_beacons)


def generate_plane(sensor):
    colinear_points = sensor.build_points()
    points = [
        symp.Point(c[0], c[1]) for c in colinear_points
    ]
    plane = symp.Polygon(points[0], points[1], points[2], points[3])
    return(plane)

def get_x_extents(sensors):
    xmin = 999999
    xmax = -99999

    for s in sensors:
        xmin = min(xmin, s.x)
        xmax = max(xmax, s.x)
        xmin = min(xmin, s.beacon.x)
        xmax = max(xmax, s.beacon.x)

    return xmin, xmax


def generate_sensors(lines):
    sensors = [None] * len(lines)
    i = 0
    for line in lines:
        sensor = line[0]
        beacon = line[1]
        sensorX, sensorY = strip_to_x_y(sensor)
        beaconX, beaconY = strip_to_x_y(beacon)

        b = Beacon(beaconX, beaconY)
        s = Sensor(sensorX, sensorY, b)

        sensors[i] =s

        i += 1

    return(sensors)

def solve_pt2(sensors):
    main_poly = shap.Polygon(
        ((0, 0),(0, 4000000),(4000000, 4000000),(4000000, 0))
    )
    for s in sensors:
        colinear_points = s.build_points()
        points = [
            (c[0], c[1]) for c in colinear_points
        ]
        s_poly = shap.Polygon((points[0], points[1], points[2], points[3]))
        new_poly = main_poly.difference(s_poly)
        if new_poly.is_empty:
            print()
        main_poly = new_poly

    x = main_poly.centroid.x
    y = main_poly.centroid.y
    output = x * 4000000 + y
    return(output)



if __name__ == "__main__":
    print(main())
