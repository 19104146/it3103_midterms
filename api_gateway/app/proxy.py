import requests
from fastapi import HTTPException, Request, status
from fastapi.responses import JSONResponse


async def forward_request(request: Request, url: str) -> JSONResponse:
    method = request.method.lower()
    body = await request.body()
    headers = dict(request.headers)
    headers.pop("host", None)

    try:
        response = requests.request(
            method=method,
            url=url,
            data=body,
            headers=headers,
            params=request.query_params,
        )
        return JSONResponse(
            content=response.json() if response.content else None,
            status_code=response.status_code,
            headers=dict(response.headers),
        )
    except requests.RequestException as e:
        raise HTTPException(
            detail=str(e),
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
        )
