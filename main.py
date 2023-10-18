"""Fastio app"""
import socket
import uvicorn
from fastapi import FastAPI, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse, Response

app = FastAPI(
    title="fastio", description="fastio app", docs_url="/docs", debug=True
)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# health check
@app.get("/health")
async def health() -> Response:
    """health check endpoint

    Returns:
        Response: returns OK and 200 status code
    """
    return Response(
        content="OK",
        status_code=status.HTTP_200_OK,
        headers={"content-type": "text/plain"},
    )


@app.get("/")
async def root() -> JSONResponse:
    """root endpoint

    Returns:
        JSONResponse: return the hostname and the ip of the pod
    """
    return JSONResponse(
        content={
            "hostname": socket.gethostname(),
            "ip": socket.gethostbyname(socket.gethostname())
        }
    )

if __name__ == "__main__":
    uvicorn.run(app="main:app", host="0.0.0.0", port=5000, reload=True)  # nosec
