from fastapi import FastAPI
import uvicorn

from task import router as task_router

app = FastAPI(title="Address Book App",
    docs_url="/address-book-docs",
    version="0.0.1")


@app.get("/")
async def root():
    return {"message": "Hello Address Book API Jackson"}


app.include_router(task_router.router)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)