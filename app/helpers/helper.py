from datetime import datetime
import pytz
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hashing_bcrypt(password: str):
    return pwd_context.hash(password)


def timestamp():
    """Mengembalikan waktu saat ini dalam zona Asia/Jakarta"""
    return datetime.now(pytz.timezone("Asia/Jakarta"))