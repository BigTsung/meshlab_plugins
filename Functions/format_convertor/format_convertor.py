import sys
import pymeshlab
import argparse
import glob, os
from pathlib import Path

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "-input_path", type=str, help="directory of model")
    parser.add_argument("-f", "-format", type=str, help="the target format.(ex: obj ply xyz e57 off stl)")
    parser.add_argument("-o", "-output_path", type=str, help="output path")
    args = parser.parse_args()
    inputPath = args.i
    format = args.f
    outputPath = args.o
    
    if not inputPath:
        sys.exit(0)

    print("Input path: ", inputPath)
    ms = pymeshlab.MeshSet()

    ms.load_new_mesh(inputPath)
    
    fileName = Path(inputPath).stem

    finalOutput = os.path.join(outputPath, fileName + "." + format)

    print("Export: ", finalOutput)
    ms.save_current_mesh(file_name=finalOutput)		
    # ms.save_current_mesh(outputPath)
    print("Converted!")