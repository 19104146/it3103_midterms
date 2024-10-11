import jwt
from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from typing_extensions import Annotated, Any, Dict

from app.config import config

security = HTTPBearer()


def decode_token(token: str) -> Dict[str, Any]:
    try:
        return jwt.decode(
            token,
            config.JWT_SECRET,
            algorithms=[config.JWT_ALGORITHM],
        )
    except jwt.ExpiredSignatureError:
        raise HTTPException(
            detail="Token has expired",
            status_code=status.HTTP_401_UNAUTHORIZED,
        )
    except jwt.PyJWTError:
        raise HTTPException(
            detail="Could not validate credentials",
            headers={"WWW-Authenticate": "Bearer"},
            status_code=status.HTTP_401_UNAUTHORIZED,
        )


def verify_token(
    credentials: Annotated[HTTPAuthorizationCredentials, Depends(security)],
) -> Dict[str, Any]:
    token = credentials.credentials
    try:
        return decode_token(token)
    except Exception as e:
        raise HTTPException(
            detail=f"Invalid authentication credentials: {str(e)}",
            status_code=status.HTTP_401_UNAUTHORIZED,
        )


def get_current_user(payload: Dict[str, Any] = Depends(verify_token)) -> Dict[str, Any]:
    user_id = payload.get("id")

    if user_id is None:
        raise HTTPException(
            detail="Invalid token payload",
            status_code=status.HTTP_401_UNAUTHORIZED,
        )

    return {"id": user_id, "role": payload.get("role")}
