from fastapi import FastAPI


app = FastAPI(title="Address Book App",
    docs_url="/address-book-docs",
    version="0.0.1")


@app.get("/")
async def root():
    return {"message": "Hello Address Book API"}