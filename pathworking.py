#-*- coding: utf-8 -*-
"""
Name: Bar Dalal
Class: YB4

Script that presents a work with paths
"""

import os
import matplotlib.pyplot as plt


def create_dir():
    """
    The function inputs a path and a name of a directory to create
    If no input is typed, the path will be the desktop as default
    The function creates the given directory in the path, and also two sub-directories: train and test
    """
    path= input("type the path in which you want to create a directory\n") # the path
    if path == "": # no input, so set a default path
        path= r'C:/Users/bard1/OneDrive/Desktop'
    if check_exist(path):
        name= input("type the name of the directory you want to create\n") # the name of the directory
        new_path= os.path.join(path, name) # path of the new directory
        try:
            os.mkdir(new_path) # create the desirable directory
            # creating the sub-directories:
            train_path= os.path.join(new_path, "train") #train_path= path+"\train"
            os.mkdir(train_path)
            test_path= os.path.join(new_path, "test") #test_path= path+"\test"
            os.mkdir(test_path)
        except: # if the directory can't be created
            print("The directory alreday exists")
    else: # if the input path doesn't exist 
        print("The path doesn't exist")
    

def check_exist(path):
    """
    The function gets a path
    The function returns true if the given path exists, and false otherwise
    """
    return os.path.exists(path)

    
def save_files(path_sub, path_img):
    """
    The function gets two paths: 
    the one is supposed to be the path to train/test directory, and the other is supposed to be the path to images directory
    if the path is of the train, so 70% of the images are tranferred to the train directory
    if the path is of the test, so all of the images are transferred to the test directory
    """
    if path_sub[-5:] == "train": # the path is of the train dir
        files= os.listdir(path_img) # list of the files which are in the images dir
        counter= len(files)
        counter= (int) (0.7*counter) # how much 70% of the images in the dir is
        for img in files:
            if counter != 0:
                os.rename(os.path.join(path_img, img), os.path.join(path_sub, img)) # move the file: (src, dst)
                counter-= 1
            else: # 70% of the images were already transferred
                break
        
    if path_sub[-4:] == "test": # the path is of the test dir
        files= os.listdir(path_img) # list of the files which are in the images dir
        for img in files:
            os.rename(os.path.join(path_img, img), os.path.join(path_sub, img)) # move the file: (src, dst)


def print_dir(path):
    """
    The function gets a path that is supposed to be a path to train/test directory
    The function prints the names of the files (images) in the directory and shows them in plots
    """
    print('The names of the files in ', path, ' :')
    for img in os.listdir(path):
        print(img) # print the names
        # display the image:
        plt.imshow(plt.imread(os.path.join(path, img))) 
        plt.show()
    
       
def main():
    create_dir()
    save_files(r'D:\stam\train', r'D:\dataset') # from dataset to train
    print_dir(r'D:\stam\train') # files in train
    
    
if __name__ == "__main__":
    main()
