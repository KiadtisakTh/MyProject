# S heart laundry service
MyProject 64<br>

# Freze version env<br>
python -m pip freeze > requirements.txt<br>

# install env <br>
1.สร้าง env เปล่าไว้ก่อน<br>
2.เข้าenv ด้วยคำสั่ง conda activate ['ชื่อ  envนั้น ']<br>
3.ใช้คำสั่ง<br>
python -m pip install -r requirements.txt<br>
เสร็จ<br>

# install Crispy form <br>
pip install django-crispy-forms <br>

# install Crispy tailwind <br>
pip install crispy-tailwind <br>

# Realtime Django Channels and Daphne <br>
pip install daphne <br>
pip install channels <br>


# How to open server <br>
daphne -b 0.0.0.0 -p 8000 myproject.asgi:application <br>
python manage.py runserver  <br>
