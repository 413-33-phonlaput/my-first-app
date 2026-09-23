import streamlit as st

# สร้างระบบตะกร้าสินค้าสำหรับจำค่า
if "cart" not in st.session_state:
    st.session_state.cart = []

# 1. ตั้งค่าหัวข้อหน้าเว็บ
st.title("ร้านเครื่องเขียนราคากู้ก")
st.write("จัดทำโดย: กลุ่มที่ 5")

st.divider()  # เส้นคั่นหน้าจอ

# 2. แสดงรายการสินค้าชิ้นที่ 1
st.subheader("1. สมุดโน้ต")
st.write("ราคา: 20 บาท")
if st.button("สั่งซื้อสมุดโน้ต"):
    st.session_state.cart.append({"name": "สมุดโน้ต", "price": 20})
    st.success("บันทึกการสั่งซื้อสมุดโน้ตเรียบร้อย!")

st.divider()

# 3. แสดงรายการสินค้าชิ้นที่ 2
st.subheader("2. ปากกาเจล")
st.write("ราคา: 15 บาท")
if st.button("สั่งซื้อปากกาเจล"):
    st.session_state.cart.append({"name": "ปากกาเจล", "price": 15})
    st.success("บันทึกการสั่งซื้อปากกาเจลเรียบร้อย!")

st.divider()

# 4. โซนตะกร้าสินค้า คำนวณเงิน และระบบส่วนลด
st.subheader("🛒 ตะกร้าสินค้าและการชำระเงิน")

if len(st.session_state.cart) == 0:
    st.info("ยังไม่มีสินค้าในตะกร้า")
else:
    total_price = 0
    # แสดงรายการที่กดซื้อไป
    for item in st.session_state.cart:
        st.write(f"- {item['name']} : {item['price']} บาท")
        total_price += item['price']
    
    st.write(f"**ราคารวมปกติ:** {total_price} บาท")
    
    # --- ระบบส่วนลด (Discount System) ---
    st.markdown("### 🎁 ส่วนลด")
    
    # ช่องกรอกโค้ดส่วนลด
    user_code = st.text_input("กรอกโค้ดส่วนลด (ลองใส่: SALE10 หรือ FREE5):")
    
    discount = 0
    
    # เงื่อนไขส่วนลด
    if user_code == "SALE10":
        discount = 10
        st.success("🎉 ใช้โค้ด SALE10 สำเร็จ! ได้รับส่วนลด 10 บาท")
    elif user_code == "FREE5":
        discount = 5
        st.success("🎉 ใช้โค้ด FREE5 สำเร็จ! ได้รับส่วนลด 5 บาท")
    elif user_code != "":
        st.error("❌ โค้ดส่วนลดไม่ถูกต้อง")
    
    # คำนวณยอดเงินสุทธิหลังหักส่วนลด
    final_price = max(0, total_price - discount)
    
    st.markdown(f"### 💰 ยอดที่ต้องจ่ายจริง: {final_price} บาท")
    st.caption(f"(ประหยัดไปได้ {discount} บาท)")
    
    # ปุ่มยืนยันสั่งซื้อ และปุ่มล้างตะกร้า
    col1, col2 = st.columns(2)
    with col1:
        if st.button("✅ ยืนยันการสั่งซื้อ"):
            st.balloons()
            st.success("สั่งซื้อสำเร็จ ขอบคุณครับ!")
            st.session_state.cart = []
    with col2:
        if st.button("🗑️ ล้างตะกร้า"):
            st.session_state.cart = []
            st.rerun()
