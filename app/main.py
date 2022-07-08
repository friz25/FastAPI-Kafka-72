from fastapi import FastAPI
import router
import asyncio

app = FastAPI()

@app.get('/')
async def Home():
    return "welcome home master friz"

app.include_router(router.route)
asyncio.create_task(router.consume())

# uvicorn main:app --reload
