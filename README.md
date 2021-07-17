#### 安裝所需套件
- `pip install -r requirements.txt`

安裝alembic:
- `pip install alembic`

初始化alembic:
- `alembic init .`

初始化alembic目錄:
- `alembic init alembic`

建立修訂版本:
- `alembic revision -m "create account table"`

切換alembic目錄:
- `cd .\alembic\`

新增資料庫欄位:
- `alembic upgrade head`

