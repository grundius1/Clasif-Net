import argparse
import os
from src.images import image_resize,get_clases, get_prediction,get_folder_imgs_pred
import sys 
    

def main():
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group(required = True)
    group.add_argument('--fil', dest='file', help= 'singel image path use for precition', default=None)
    group.add_argument('--fol', dest='folder', help= 'folder of the images you wana make all the predictions', default= None)




    args = parser.parse_args()
    print(args)
    file_path = args.file
    folder_path = args.folder

    if file_path != None:
        if os.path.isfile(file_path):
            print(get_prediction(file_path))
            sys.exit()
        else:
            raise FileNotFoundError("check the path for the file")
        
    if folder_path != None:
        if os.path.isdir(folder_path):
            get_folder_imgs_pred(folder_path)
            sys.exit()
        else:
            raise FileNotFoundError("check the path for the folder")



def check_path(path):
    return os.path.exists(path)


if __name__ == "__main__":
    main()