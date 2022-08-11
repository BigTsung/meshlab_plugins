import sys
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

    if not inputPath:
        sys.exit(0)

    ms.load_new_mesh(inputPath)
    # remove duplicate vertices
    ms.meshing_remove_duplicate_vertices()
    
    # remove unreferenced vertices
    ms.meshing_remove_unreferenced_vertices()
    
    # remove zero area faces
    ms.meshing_remove_null_faces()

    # remove isolated pieces wrt face
    ms.meshing_remove_connected_component_by_face_number(mincomponentsize=10000)

    # delete self intersecting
    ms.compute_selection_by_self_intersections_per_face()
    ms.meshing_remove_selected_faces()		
        
    # 	ms.meshing_remove_selected_vertices()
    #ms.select_small_disconnected_component(nbfaceratio=0.1)
    #ms.meshing_remove_selected_faces()

    # delete non manifold faces
    ms.compute_selection_by_non_manifold_edges_per_face()
    ms.meshing_remove_selected_vertices()
    ms.meshing_remove_selected_faces()

    # delete non manifold vertices
    for i in range(1, 10):
        ms.compute_selection_by_non_manifold_per_vertex()
        ms.meshing_remove_selected_vertices()

    ms.meshing_close_holes(maxholesize=1000)

    print("Export: ", outputPath)
    ms.save_current_mesh(file_name=outputPath, save_face_color=False, save_vertex_color=False)		
    # ms.save_current_mesh(outputPath)
    print("Cleaing Done!")