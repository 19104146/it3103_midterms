from passlib.context import CryptContext
from typing_extensions import List

from app.exceptions.user import UserConflictException, UserNotFoundException
from app.schemas.user import Role, UserRead, UserWrite


class UserService:
    def __init__(self):
        self.users: List[UserRead] = [
            UserRead(
                id=1,
                username="admin",
                password="$2b$12$TWfE0QC6wrSMO09J9R70x.IOQhGZxHIhtBFFdcnHJLf/MzjZUaQeC",
                role=Role.ADMIN,
            )
        ]
        self.next_id = 1
        self.pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

    def list_users(self) -> List[UserRead]:
        return self.users

    def create_user(self, user: UserWrite) -> UserRead:
        if self._is_duplicate(user.username):
            raise UserConflictException()

        new_user = UserRead(
            id=self.next_id,
            username=user.username,
            password=user.password,
        )

        self.users.append(new_user)
        self.next_id += 1
        return new_user

    def read_user(self, user_id: int) -> UserRead:
        existing_user = next((u for u in self.users if u.id == user_id), None)
        if not existing_user:
            raise UserNotFoundException()
        return existing_user

    def update_user(self, user_id: int, updated_user: UserWrite) -> UserRead:
        existing_user = self.read_user(user_id)

        if updated_user.username != existing_user.username:
            if self._is_duplicate(updated_user.username):
                raise UserConflictException()

        existing_user.username = updated_user.username
        existing_user.password = self.pwd_context.hash(updated_user.password)
        return existing_user

    def delete_user(self, user_id: int) -> None:
        user = self.read_user(user_id)
        self.users.remove(user)

    def _is_duplicate(self, username: str) -> bool:
        return any(u.username == username for u in self.users)
