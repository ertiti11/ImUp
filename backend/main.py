from fastapi import FastAPI, File, UploadFile
from fastapi.responses import FileResponse
import os
from pydantic import BaseModel
from listdir import listimages
from routers import image


app = FastAPI()


app.include_router(image.router)





# 






