import numpy as np
import matplotlib.pyplot as plt
from math import sqrt
from random import uniform
from skspatial.objects import Vector, Plane, Point

LOW = -1
HIGH = 1
COORDS = [LOW, HIGH]
RESULTS_DIR = "projections/"

# L = [li1+[i] for i in [-1,1] for li1 in [li2+[j] for j in [-1,1] for li2 in [[-1],[1]]]]
def matrix_L():
    return [Point([x, y, z]) for x in COORDS for y in COORDS for z in COORDS]

def random_vector():
    return Vector.from_points([0,0,0], [
        uniform(LOW, HIGH),
        uniform(LOW, HIGH),
        uniform(LOW, HIGH)
    ]).unit()

def random_ortonormal_base():
    n1 = random_vector()
    n2 = random_vector()
    n3 = n1.cross(n2).unit()
    n2 = n1.cross(n3).unit()
    return [n1, n2, n3]

def matrix_A():
    A = np.random.rand(2,3) # Normal distribution
    return A * (1/sqrt(2))


# L = matrix_L()
# print(L)


if __name__ == "__main__":
    print("---[ ex49a ]---")
    base = random_ortonormal_base()
    with open(RESULTS_DIR + "49a_vectors.txt", 'w') as f:
        for vec in base:
            print(vec)
            f.write(str(vec) + "\n")
    plane = Plane.from_vectors([0,0,0],base[0],base[1])
    L = matrix_L()
    _, ax = plt.subplots()
    for point in L:
        point_proj = plane.project_point(point)
        point_proj.plot_2d(ax, s=50)
    plt.savefig(RESULTS_DIR + "49a_graph.png", dpi=300)
    plt.close()

    print("---[ ex49b ]---")
    A = matrix_A()
    with open(RESULTS_DIR + "49b_matrix.txt", 'w') as f:
        for row in A:
            print(row)
            f.write(str(row) + "\n")
    # L_proj = []
    _, ax = plt.subplots()
    for point in L:
        point_proj = Point(A.dot(point))
        print
        point_proj.plot_2d(ax, s=50)
    plt.savefig(RESULTS_DIR + "49b_graph.png", dpi=300)
    plt.close()

