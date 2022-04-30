from fastapi import APIRouter
from pydantic import BaseModel

# สร้างตัวแปร router มารับ APIRouter เพื่อสร้างการเชื่อมต่อไฟล์
# ประกาศเพื่อการนี้  http://localhost:8000/invetory/ 
router = APIRouter(
    prefix="/invetory",
    tags=["inventory"]
)



# 7. สร้างคลาส เพื่อสืบทอด BaseModel โดยอ้างอิงจาก รูปแบบข้อมูล JSON
# เพื่อใช้เป็นรูปแบบตัวแปร ที่จะใช้รับส่งค่าใน FN
class InventoryBase(BaseModel):
    description: str
    price: float
    stock: int

# การใช้ / เพื่อเป็น path ของ url
# 1. สร้าง API CRUD
# 1.1 GET
# @router.get("/")
# def hello_world():
# return {"Hello": "World"}  # return "Dictionary" -> {}

# 1.2 POST
# @router.post("/")
# def post_api():
#     return {"Hello": "post"}

# 8. ทดสอบการ POST ข้อมูล JSON โดยใช้ BaseModel ที่สร้าง
@router.post("/")
def post_api(inventory: InventoryBase):
    print(inventory)  # แสดงผล terminal เมื่อมีการเรียก post ข้อมูลเข้ามา
    return inventory


# # 1.3 PUT
# @router.put("/")
# def put_api():
#     return {"Hello": "put"}

# # 1.4 DELETE
# @router.delete("/")
# def delete_api():
#     return {"Hello": "delete"}

# 2. ข้อมูลจำลอง DB รายการสินค้า (inventory)  ->   แบบ JSON ใน Array
fake_inventory = [
    {"description": "pencil", "price": 15, "stock": 15},
    {"description": "laptop", "price": 5, "stock": 20},
    {"description": "books", "price": 25, "stock": 30},
]


# 3. สร้าง get API ใหม่ โดย comment FN hello World ด้านบน
# เนื่องจาก 1 CRUD สร้างได้ 1 คำสั่งเท่านั้น ที่เป็น type เดียวกัน ในโปรเจค ()
# @router.get("/")
# def hello_stock():
#     return fake_inventory

# 4. สร้าง Get โดยเริ่มจากระบุ ID ข้อมูล แบบ  ->  Path    เนื่องจาก ระบุตัวแปร ใน url (ดูจาก Swagger UI)
# @router.get("/{id}")
# def hello_id(id: int):       # สร้าง FN ให้รับค่า int ID
#     return {"Hello id": id}  # return "Dictionary" -> {}

# 5. ลองสร้างร GET Stock กับส่งค่า version  -> Query    เนื่องจาก ระบุตัวแปรใน FN ไม่เกี่ยวกับ url (ดูจาก Swagger UI)
# @router.get("/")
# def hello_version(version: int = 1):        # กำหนด defualt เป็น 1
#     print(version)
#     return fake_inventory

"""
    การใช้งานคล้ายกัน เช่น รับค่ามาก่อน เพื่อ if หรือ แสดงผลตามต้องการ
    แต่ส่วนใหญ่จะใช้ Query โดยการรับ key บางอย่าง แล้วนำมา search หาข้อมูลที่ต้องการ
    4. Path type :     http://localhost:8000/3               -> ไม่นิยม เพราะไม่รุ้ว่าค่าที่ส่งไปคืออะไร ต้องไปเกะใส่ใน API ที่เขียนเอาเอง
    5. Query type :    http://localhost:8000/?version=1      -> นิยมมากกว่า เพราะรู้ชื่อตัวแปร สื่อความหมายได้เลย
"""

# 6. ตัวอย่างการใช้งาน GET แบบมีเงื่อนไข (ต้อง comment ข้อ 3,5. ด้วย)
@router.get("/")
def get_all_inventory(version: int = 1):  # กำหนด defualt เป็น 1
    if version > 1:
        return {"msg": "data not avaliable"}
    else:
        return fake_inventory


# 9. สร้าง Get โดยเริ่มจากระบุ ID ระบุ ข้อมูล JSON ใน Array [0-...]
@router.get("/{id}")
def inventory_by_id(id: int):  # สร้าง FN ให้รับค่า int ID
    item = fake_inventory[id - 1]  # ลบ 1 เพราะเริ้มนับจาก index 0
    return item


# 10 DELETE by ID (comment ข้อ 1.4)
@router.delete("/{id}")
def delete_by_id(id: int):
    item = fake_inventory.pop(id - 1)  # .pop คือสั่งลบ array[i]
    return item  # ส่งกลับ arrar ที่ถูกลบ


# 11 Update by ID (comment ข้อ 1.3)
@router.put("/{id}")
def put_by_id(id: int, inventory: InventoryBase):
    fake_inventory[id - 1].update(
        **inventory.dict()
    )  # .update เพื่อเพิ่มค่า แต่จะเพิ่มทั้งชุดของมูลชนิด dict เลย โดยการการ spread ** ช่วย
    item = fake_inventory[id - 1]
    return item
