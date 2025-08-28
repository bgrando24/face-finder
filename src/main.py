from fastapi import FastAPI, File, UploadFile, HTTPException
from face_detector import FaceDetector
import numpy

# init app
app = FastAPI()

#init face detector
FD = FaceDetector()

# index
@app.get("/")
async def get_root():
    return {"message": "Welcome to Face Detector!"}

# get image metadata
@app.post("/meta-data")
async def post_extract_img_meta(img_file: UploadFile = File(...)):
    # read request contents, convert to numpy array
    contents = await img_file.read()
    img_np_array = numpy.frombuffer(contents, numpy.uint8)
    # pass to face detector class
    return FD.get_img_meta(img_np_array)