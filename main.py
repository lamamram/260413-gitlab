from fastapi import FastAPI
from app.models.database import engine, Base
from app.routes.main import router
from app.routes.employees import router as employees_router

# Create database tables
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="FastAPI SQLAlchemy App",
    description="A simple FastAPI application with SQLAlchemy",
    version="1.0.0",
)

app.include_router(router)
app.include_router(employees_router)


@app.get("/")
async def root():
    return {"message": "Hello World"}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
