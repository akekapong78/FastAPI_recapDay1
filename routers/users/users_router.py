from fastapi import APIRouter

# ประกาศ การเรียกใช้งาน router 
# ประกาศเพื่อการนี้  http://localhost:8000/user/ 
router = APIRouter(
    prefix="/users",
    tags=["users"]
)

# สร้าง DB user เพื่อทดสอบ การ router ครั้งนี้
fake_user_db = [
    {"username": "Akekapong"},
    {"username": "Paytaii"}
]

# สร้าง end-point เป็นจุดสังเกตุ ของไฟล์ โดยใช้ Get
@router.get("/")
def get_all_user():
    return fake_user_db