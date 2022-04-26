import pymeshlab
import argparse
import glob, os

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "-input_path", type=str, help="directory of model")
    parser.add_argument("-o", "-output_path", type=str, help="output path")
    args = parser.parse_args()
    inputPath = args.i
    outputPath = args.o
    print("input path: ", inputPath)
    print("output path: ", outputPath)
    ms = pymeshlab.MeshSet()

    ms.load_new_mesh(inputPath)
    ms.compute_normal_by_function_per_vertex(x="nx", y="ny", z="nz")
    ms.generate_surface_reconstruction_screened_poisson(depth=12, pointweight=6)

    print("Export: ", outputPath)
    ms.save_current_mesh(file_name=outputPath, save_face_color=False, save_vertex_color=False)		
    # ms.save_current_mesh(outputPath)
    print("Cleaing Done!")