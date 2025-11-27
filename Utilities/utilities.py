import numpy as np

from scipy.spatial import ConvexHull
from pyntcloud import PyntCloud

# To convert cameras.txt, images.txt, and points3D.txt from COLMAP to a .ply file
def read_points3D(file_path):
    points3D = {}
    with open(file_path, 'r') as f:
        for line in f:
            if line.startswith('#'):
                continue
            parts = line.split()
            point_id = int(parts[0])
            xyz = np.array([float(parts[1]), float(parts[2]), float(parts[3])])
            rgb = np.array([int(parts[4]), int(parts[5]), int(parts[6])])
            points3D[point_id] = (xyz, rgb)
    return points3D

def write_ply(points3D, output_path):
    with open(output_path, 'w') as f:
        f.write('ply\n')
        f.write('format ascii 1.0\n')
        f.write(f'element vertex {len(points3D)}\n')
        f.write('property float x\n')
        f.write('property float y\n')
        f.write('property float z\n')
        f.write('property uchar red\n')
        f.write('property uchar green\n')
        f.write('property uchar blue\n')
        f.write('end_header\n')
        for point_id, (xyz, rgb) in points3D.items():
            f.write(f'{xyz[0]} {xyz[1]} {xyz[2]} {rgb[0]} {rgb[1]} {rgb[2]}\n')
            

# Calculate volume using ConvexHull (.3 files)
def calculate_volume(point_cloud):
    points3D_array = np.array([point.xyz for point in list(point_cloud.values())])
    hull = ConvexHull(points3D_array)
    return hull.volume


# Calculate volume using ConvexHull (.ply)
def calculate_volume_file(file_path, file_name):
    data_mesh = PyntCloud.from_file(file_path + '/' + file_name)

    convex_hull_id = data_mesh.add_structure("convex_hull")
    convex_hull = data_mesh.structures[convex_hull_id]

    data_mesh.mesh = convex_hull.get_mesh()
    data_mesh.to_file(file_path + '/' + 'mesh_hull.ply', also_save=["mesh"])

    volume = convex_hull.volume
    # print("The volume is", round(volume, 3))

    # data_mesh.plot()
    return volume