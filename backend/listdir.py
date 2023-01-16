
from pathlib import Path
import glob



def listimages():
    images = []

    for name in glob.glob('backend/images/*'):
        images.append(name.replace("\\", "/").replace("backend", ""))

    
    return images

print(listimages())