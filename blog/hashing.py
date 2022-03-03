from passlib.context import CryptContext

pwd_cont = CryptContext(schemes=["bcrypt"], deprecated="auto")


class Hash():
    def bcrypt(pwd: str):
        return pwd_cont.hash(pwd)
