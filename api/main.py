from fastapi import FastAPI

from api.routers import done, task

from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.include_router(task.router)
app.include_router(done.router)

# CORS設定
app.add_middleware(
  CORSMiddleware,
  allow_origins=["*"],
  allow_credentials=True,
  allow_methods=["*"],
  allow_headers=["*"]
)