import re

def extract_discount_and_code_with_conditions(text):
    result = {}

    # ดึงตัวเลขหลังคำว่า "ลด"
    discount_match = re.search(r'ลด\s*฿?(\d+)', text)
    if discount_match:
        result['discount'] = int(discount_match.group(1))
    else:
        result['discount'] = None

    # ดึงโค้ดหลังคำว่า "กรอกโค้ด"
    code_match = re.search(r'กรอกโค้ด:\s*([A-Z0-9]+)', text)
    if code_match:
        result['code'] = code_match.group(1)
    else:
        result['code'] = None

    # ดึงจำนวนเงินที่ต้องช็อปครบหลังคำว่า "เมื่อช็อปครบ"
    shop_condition_match = re.search(r'เมื่อช็อปครบ\s*฿?([\d,]+)', text)
    if shop_condition_match:
        result['shop_condition'] = shop_condition_match.group(1).replace(',', '')  # เอา , ออก
    else:
        result['shop_condition'] = None

    # ดึงเงื่อนไขหลังคำว่า "เฉพาะวันสั่งซื้อ" และก่อน "-สิทธิพิเศษ"
    condition_match = re.search(r'เฉพาะวันสั่งซื้อ(.*?)\s*- สิทธิพิเศษ', text, re.DOTALL)
    if condition_match:
        result['condition'] = condition_match.group(1).strip()
    else:
        result['condition'] = None

    return result



text = '''
                                ลด ฿180

                                Copy

กรอกโค้ด: MAYST3

                                    เมื่อช็อปครบ ฿3,000/ใบเสร็จ

T&C


 ลด ฿180

เมื่อช็อปครบ ฿3,000/ใบเสร็จ
เฉพาะวันสั่งซื้อ: 1 พ.ค. 2568 - 31 พ.ค. 2568




- สิทธิพิเศษเฉพาะสมาชิกเดอะวัน
'''

output = extract_discount_and_code_with_conditions(text)
print(output)
