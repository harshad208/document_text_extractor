import uvicorn
from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.middleware.cors import CORSMiddleware

import document_text_extractor.base_model.Model as model
from CommonOperations import *
from Configuration import *
from GetTextFromImage import GetTextFromImage

app = FastAPI(  title="Document Text Extractor",  
    description="This is my custom API description.",
    version="1.0.0")

origins = ["*"] 

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def read_root():
    return {"message": "Hello, World"}


@app.post("/file_for_text_extract/")
async def file_for_text_extract(file: UploadFile = File(...)):
    try:
        file_contents = await file.read()
        base64_string = base64.b64encode(file_contents).decode()
        file_input = convert_to_json(file.filename, file.filename.split(".")[-1], base64_string)
        lstr_file_path = convert_input_to_format(file_input, temp_path)
        lobj_text_from_iamge = GetTextFromImage()
        llist_file_path = lobj_text_from_iamge.get_text_from_image_path(lstr_file_path)

        return model.SuccessResponse(message="Request processed successfully", data=llist_file_path)

    except Exception as e:
        logging.error(f"Error: {str(e)}", exc_info=True)
        raise HTTPException(status_code=400, detail=e)


if __name__ == "__main__":
    uvicorn.run(app, host=host, port=port)
