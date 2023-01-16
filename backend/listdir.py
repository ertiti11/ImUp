import os

def listimages():
    dir_path = './images'
    res = []

    for path in os.listdir(dir_path):
        if os.path.isfile(os.path.join(dir_path, path)):
            res.append("/image/"+path)
    
    return res
