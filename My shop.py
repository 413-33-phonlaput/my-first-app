import streamlit as st

# ระบบตะกร้าสินค้า
if "cart" not in st.session_state:
    st.session_state.cart = []

st.title("🛒 ร้านเครื่องเขียนราคากู้ก")
st.write("จัดทำโดย: กลุ่มที่ 5")
st.divider()

# ---------------------------------------------------------
# 1. รายการสินค้าและราคาตามรูปภาพ
# ---------------------------------------------------------
products = [
    {"name": "สมุด", "price": 13},
    {"name": "ปากกา", "price": 10},
    {"name": "ดินสอ", "price": 7},
    {"name": "ยางลบ", "price": 5},
    {"name": "ลิควิดน้ำ", "price": 15},
    {"name": "ลิควิดเทป", "price": 20},
    {"name": "ไม้บรรทัด", "price": 16},
    {"name": "สีไม้ 24 สี", "price": 239},
    {"name": "กระเป๋าดินสอ", "price": 39},
    {"name": "แฟ้ม", "price": 20},
    {"name": "กบเหลา", "price": 25},
]

st.subheader("📝 เลือกซื้อสินค้า")

# แสดงรายการสินค้าแบบปุ่มกดง่ายๆ
for item in products:
    col1, col2 = st.columns([3, 1])
    with col1:
        st.write(f"• **{item['name']}** - ราคา {item['price']} บาท")
    with col2:
        if st.button("หยิบใส่ตะกร้า", key=item["name"]):
            st.session_state.cart.append(item)
            st.success(f"เพิ่ม {item['name']} แล้ว")

st.divider()

# ---------------------------------------------------------
# 2. ตะกร้าสินค้าและการคิดเงินตามเกณฑ์ส่วนลด
# ---------------------------------------------------------
st.subheader("🛍️ ตะกร้าสินค้าและการคิดเงิน")

if len(st.session_state.cart) == 0:
    st.info("ยังไม่มีสินค้าในตะกร้า (เลือกสินค้าด้านบนได้เลยครับ)")
else:
    total_price = 0
    # แสดงสินค้าในตะกร้า
    for item in st.session_state.cart:
        st.write(f"- {item['name']} : {item['price']} บาท")
        total_price += item["price"]

    st.write(f"**ยอดซื้อรวม:** {total_price} บาท")

    # --- คำนวณส่วนลดอัตโนมัติตามเกณฑ์ ---
    discount_percent = 0

    if 500 <= total_price <= 700:
        discount_percent = 2
    elif 701 <= total_price <= 900:
        discount_percent = 4
    elif total_price >= 901:
        discount_percent = 5

    # คิดเป็นเงินส่วนลด
    discount_amount = total_price * (discount_percent / 100)
    final_price = total_price - discount_amount

    # แสดงผลส่วนลด
    if discount_percent > 0:
        st.success(
            f"🎉 ยอดซื้อเข้าเกณฑ์! ได้รับส่วนลด {discount_percent}% (ลดไป {discount_amount:.2f} บาท)"
        )
    else:
        st.caption("💡 ซื้อครบ 500 บาทขึ้นไป รับส่วนลดพิเศษสูงสุด 5%")

    st.markdown(f"### 💰 ยอดที่ต้องจ่ายจริง: {final_price:.2f} บาท")

    # ปุ่มจัดการตะกร้า
    col_a, col_b = st.columns(2)
    with col_a:
        if st.button("✅ ยืนยันการสั่งซื้อ"):
            st.balloons()
            st.success("สั่งซื้อสำเร็จ ขอบคุณมากๆเลยค่ะ!")
            st.session_state.cart = []
    with col_b:
        if st.button("🗑️ ล้างตะกร้า"):
            st.session_state.cart = []
            st.rerun()
