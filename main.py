from fastapi import FastAPI
# ทำการ register router ที่สร้างขึ้นมาใหม่
# from  ชื่อโพลเดอร์.โพลเดอร์    import  ชื่อไฟล์
from routers.inventory import inventory_router
from routers.users import users_router

# 0. สร้าง app รับ FastAPI
app = FastAPI()
app.include_router(inventory_router.router)     # (ชื่อไฟล์.router)
app.include_router(users_router.router)         # (ตาม prefix ที่กำหนดไว้แล้ว)
# การเรียนใช้ CRUD ใดๆ จะไม่ตีกัน เนื่องจากกำหนด prefix ไว้แล้ว

# สร้าง end-point เป็นจุดสังเกตุ ของไฟล์ โดยใช้ Get เวลา RUN ใน Browser
# เพื่อเป็น root path แสดงไว้
@app.get("/")
def hello():
    return {"hello": "FastAPI"}
