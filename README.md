# String Search & Formatter

โปรแกรม Python GUI สำหรับค้นหาและจัดรูปแบบข้อความ โดยใช้ `customtkinter` และ `re` module

## Features

โปรแกรมมีทั้งหมด 10 Functions

1. Find Text - ค้นหาคำในข้อความ
2. Count Text - นับจำนวนคำที่ค้นหา
3. Replace Text - แทนที่ข้อความ
4. Uppercase - เปลี่ยนเป็นตัวพิมพ์ใหญ่
5. Lowercase - เปลี่ยนเป็นตัวพิมพ์เล็ก
6. Title Case - เปลี่ยนตัวอักษรแรกของแต่ละคำเป็นตัวพิมพ์ใหญ่
7. Remove Extra Spaces - ลบช่องว่างส่วนเกิน
8. Extract Numbers - ค้นหาและแสดงตัวเลขทั้งหมด
9. Extract Emails - ค้นหา Email จากข้อความ
10. Split Words - แยกข้อความออกเป็นคำ

## GUI

โปรแกรมใช้ `customtkinter` เพื่อให้หน้าตา GUI ดูทันสมัยและใช้งานง่าย

สามารถเปลี่ยน Theme ได้ 3 แบบ

- Dark
- Light
- System

## Additional Features

- โหลดไฟล์ `.txt`
- บันทึกผลลัพธ์เป็นไฟล์ `.txt`
- รองรับการค้นหาข้อความ
- รองรับ Regular Expression
- มีการใช้ `try-except` สำหรับจัดการ Error
- มีช่อง Input และ Result แยกกัน
- รองรับ Dark Mode และ Light Mode

## Requirements

- Python 3.x
- customtkinter

ติดตั้ง Library ด้วยคำสั่ง

```bash
pip install customtkinter