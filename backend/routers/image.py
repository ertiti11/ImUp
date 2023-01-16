from fastapi import APIRouter, File
from pydantic import BaseModel
from fastapi.responses import FileResponse
from pydantic import BaseModel
from listdir import listimages
from config.db import conn
from models.image import image
print("si")
router = APIRouter()


class Image(BaseModel):
    id: int
    title: str
    url: str



@router.get("/image/{id}")
async def getimage(id):
    return FileResponse("./images/"+ id)



@router.get("/images")
async def images():
    return  listimages()





@router.post("/files/")
async def create_files(
    files: list[bytes] = File(description="Multiple files as bytes"),
):
    return {"file_sizes": [len(file) for file in files]}




