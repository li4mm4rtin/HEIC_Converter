import pillow_heif
import cv2
import numpy as np
import glob
import os


def convertHEIC(filenames, out_path, type='jpg'):
    for i in filenames:
        heif_file = pillow_heif.open_heif(i, convert_hdr_to_8bit=False, bgr_mode=True)
        np_array = np.asarray(heif_file)
        new_filename = out_path + os.path.basename(i)[:-4] + type
        cv2.imwrite(new_filename, np_array)


folderPath = './TestImages/'
outPath = './outImages/'
heicFiles = glob.glob(os.path.join(folderPath, '*.heic'))
heicFiles += glob.glob(os.path.join(folderPath, '*.HEIC'))

convertHEIC(heicFiles, outPath)

