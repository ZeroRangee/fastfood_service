import uvicorn

def start():
    uvicorn.run("core.asgi:application", host="0.0.0.0", port=8000, reload=True)