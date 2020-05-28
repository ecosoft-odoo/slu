# slu
**วิธีการดึง source code มาใช้งาน**
* กำหนด repos.yaml ใน repository directory
* กำหนด addons.yaml
* เข้าไปที่ repository directory แล้วใช้คำสั่ง gitaggregate -c repos.yaml (พิม ls ดู เราจะเห็น repository ทั้งหมดตามที่เรากำหนดไว้ใน repos.yaml)
* Run script addons-link.py สำหรับคัดลอก addons จาก repository directory ทั้งหมดที่เรากำหนดใน addons.yaml และจะถูกเก็บไว้ที่ auto-addons directory
* addons ที่เฉพาะเจาะจงสำหรับ project จะถูกเก็บไว้ที่ custom-addons directory
* ใน odoo.conf ให้ reference ถึง auto-addons และ custom-addons
