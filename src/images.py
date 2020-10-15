import os
from keras.models import load_model
from keras.preprocessing.image import load_img,img_to_array
import tensorflow as tf
from tqdm import tqdm
import csv

model = load_model("modelg")


def image_resize(img_path):
    '''
    resize the img to have the same pixels as the trained model imput
    '''
    img = load_img(img_path,color_mode="grayscale",target_size=(50,50))
    img = img_to_array(img)
    img = tf.expand_dims(img, axis=0)
    return img

def get_clases():
    '''
    get the clases names from the directorie they are loaded
    '''
    dirs = [x for x in os.listdir("data/cifar-10-python/cifar-10/train2")]
    return sorted(dirs)

def get_folder_imgs_pred(path):
    '''
    load the images of a folder and make the prediction for each one qhich is added into a dictionary
    '''
    imgs=[]
    for item in os.listdir(path):
        imgs.append(path +"/"+item)
    iters = get_limit(len(imgs))
    dic = {}
    for item in tqdm(range(iters)):
        prediction = get_prediction(imgs[item])
        dic.update({f"{item+1}": prediction})
    return dict_to_csv(dic)

def get_limit(itnum):
    iters = -1
    while iters < 0:
        iters = int(input(f"how many files you want to precits from a total of {itnum} '0' means all the files: "))
    if iters == 0 or iters > itnum:
        iters = itnum
    return iters


def get_prediction(img_path):
    clases = get_clases()
    img = image_resize(img_path)
    prediction = model.predict(img).tolist()[0]
    index = prediction.index(max(prediction))
    return clases[index]

def dict_to_csv(dictionary):
    csv_colums = ["id", "prediction"]
    csv_file = "predictions.csv"
    try:
        with open(csv_file, 'w') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=csv_colums)
            writer.writeheader()
            for id,data in dictionary.items():
                writer.writerow({"id":id, "prediction" : data})
    except IOError:
        print("I/O error")

if __name__ == "__main__":
    get_folder_imgs_pred("../data/cifar-10-python/cifar-10/test")