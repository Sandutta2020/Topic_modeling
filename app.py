from fastapi import FastAPI, Form, Request
from fastapi import FastAPI, File, UploadFile
from fastapi.responses import PlainTextResponse, HTMLResponse, FileResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import uvicorn
import shutil
import pandas as pd
from main import main_funct

# initialization
app = FastAPI()

# mount static folder to serve static files
app.mount("/static", StaticFiles(directory="static"), name="static")

# Jinja2 template instance for returning webpage via template engine
templates = Jinja2Templates(directory="templates")

# serve webpage, GET method, return HTML
@app.get("/", response_class=HTMLResponse)
async def get_webpage(request: Request):
    return templates.TemplateResponse(
        "form.html",
        {"request": request, "Res": "Please upload a Review file in csv format"},
    )


@app.post("/uploadfiles", response_class=HTMLResponse)
async def uploadfiles(request: Request, files: UploadFile = Form(...)):
    with open("destination.csv", "wb") as buffer:
        shutil.copyfileobj(files.file, buffer)
    df = pd.read_csv("destination.csv")
    lst = df.columns.to_list()
    return templates.TemplateResponse(
        "form1.html",
        {
            "request": request,
            "tab": df.head(2).to_html(border=1, index=False, show_dimensions=True),
            "Res": files.filename,
            "list": lst
        },
    )

@app.post("/column_selection", response_class=HTMLResponse)
async def column_selection(request: Request, column_select: str = Form(...)):
    df = pd.read_csv("destination.csv")
    df1 =pd.DataFrame() 
    df1['review'] =df[column_select].copy()
    df1.rename(columns={column_select:'review' })
    main_funct(df1,False)
    report_tab =pd.read_csv("report/topics.csv")
    with open('report/lda.html', 'r') as f:
        html_string = f.read()

    return templates.TemplateResponse(
        "form2.html",
        {
            "request": request,
            "reptab" : report_tab.to_html(border=1, index=False, show_dimensions=True),
            "graph" : html_string,
        },
    )


# main
if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
