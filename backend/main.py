from fastapi import FastAPI, File, UploadFile
from fastapi.responses import FileResponse
import os


app = FastAPI()
import glob



def listimages():
    images = []

    for name in glob.glob('backend/images/*'):
        images.append(name.replace("\\", "/").replace("backend", ""))

    
    return images
print(listimages())
# 





@app.post("/file/")
async def create_upload_file(file: UploadFile | None = None):
    if not file:
        return {"message": "No upload file sent"}
    else:
        with open("./images/"+file.filename, 'wb') as f:
            f.write(file.file.read())
        return {"filename": file.filename}

@app.get("/image/{id}")
async def getimage(id):
    return FileResponse("./images/"+ id)

@app.get("/images")
async def images():
    images = listimages()

    return images





@app.post("/files/")
async def create_files(
    files: list[bytes] = File(description="Multiple files as bytes"),
):
    return {"file_sizes": [len(file) for file in files]}


@app.post("/uploadfiles/")
async def create_upload_files(
    files: list[UploadFile] = File(description="Multiple files as UploadFile"),
):
    return {"filenames": [file.filename for file in files]}


