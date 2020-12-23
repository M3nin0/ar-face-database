"""
As funções listadas neste arquivo foram retiradas do seguinte repositório: https://github.com/matheustguimaraes/organize-AR-face-db

O repositório tem outros utilitários disponíveis, porém, para o contexto de uso com AutoEncoder, apenas
a primera etapa, de conversão dos dados ".raw" para ".jpeg" utilizando ImageMagick está sendo utilizada.
"""

import os
from argparse import ArgumentParser
from sys import argv


def list_files(base_path, valid_exts=None, contains=None):
    """ Return the set of files with a given extension in a path """
    # loop over the directory structure
    for (rootDir, dirNames, filenames) in os.walk(base_path):
        # loop over the filenames in the current directory
        for filename in filenames:
            # if the contains string is not none and the filename does not
            # contain the supplied string, then ignore the file
            if contains is not None and filename.find(contains) == -1:
                continue

            # determine the file extension of the current file
            ext = filename[filename.rfind("."):].lower()

            # check to see if the file is an image and should be processed
            if valid_exts is None or ext.endswith(valid_exts):
                # construct the path to the image and yield it
                image_path = os.path.join(rootDir, filename)
                yield image_path


def convert_raw(args):
    # Set a path to save the images in jpeg, if you want.
    # If not pass the --save argument, the jpeg images will be saved in the
    # same folder of .raw images
    ds = args["dataset"]
    save_path = args["save"]

    if args["save"]:
        save_path = save_path
    else:
        save_path = os.path.dirname(ds)

    # List dataset images
    image_paths = list(list_files(ds, valid_exts='.raw'))

    # ImageMagick command to convert from .raw to .jpeg
    convert = 'convert -depth 8 -interlace plane -size 768x576'

    # Loop over the image paths
    for i, path in enumerate(image_paths):
        print("[INFO] Converting image {}".format(i + 1))
        img_folder = path.replace(ds, '').replace('.raw', '.jpeg')

        # Check if folder exists, if not, create folder
        created_folder = os.path.join(save_path, os.path.dirname(img_folder))
        os.makedirs(created_folder, exist_ok=True)

        # Convert using ImageMagick and store all images in defined folder
        os.system('{} rgb:{} {}{}'.format(convert, path, save_path,
                                          img_folder))


if __name__ == '__main__':
    convert_raw({
        "dataset": "merge",
        "save": "ar_out"
    })
