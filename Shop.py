<!DOCTYPE html>
<html lang="th">
<head>
    <meta charset="UTF-8">
    <title>ร้านเครื่องเขียนราคาถูก</title>
    <style>
        body {
            font-family: sans-serif;
            padding: 20px;
            background-color: #f4f6f9;
        }
        .box {
            background: white;
            padding: 15px;
            margin-bottom: 15px;
            border-radius: 8px;
        }
        .price {
            color: red;
            font-weight: bold;
        }
        button {
            background-color: green;
            color: white;
            border: none;
            padding: 5px 10px;
            border-radius: 4px;
        }
    </style>
</head>
<body>

    <h1>ร้านเครื่องเขียน พรลภัส</h1>
    <p>จัดทำโดย: นางสาว พรลภัส ต้องมีเกียรติกุล ม.4/13</p>

    <div class="box">
        <h3>เกณฑ์ส่วนลด</h3>
        <p>ยอดซื้อ 500 - 700 บาท ลด 2%</p>
        <p>ยอดซื้อ 701 - 900 บาท ลด 4%</p>
        <p>ยอดซื้อ 901 บาทขึ้นไป ลด 5%</p>
    </div>

    <h2>รายการสินค้า</h2>
    <div class="box">
        <p>สมุด - <span class="price">13 บาท</span> <button onclick="add(13)">ซื้อ</button></p>
        <p>ปากกา - <span class="price">10 บาท</span> <button onclick="add(10)">ซื้อ</button></p>
        <p>ดินสอ - <span class="price">7 บาท</span> <button onclick="add(7)">ซื้อ</button></p>
        <p>ยางลบ - <span class="price">5 บาท</span> <button onclick="add(5)">ซื้อ</button></p>
        <p>ลิควิดชี้น้ำ - <span class="price">15 บาท</span> <button onclick="add(15)">ซื้อ</button></p>
        <p>ลิควิดเทป - <span class="price">20 บาท</span> <button onclick="add(20)">ซื้อ</button></p>
        <p>ไม้บรรทัด - <span class="price">16 บาท</span> <button onclick="add(16)">ซื้อ</button></p>
        <p>สีไม้ 24 สี - <span class="price">239 บาท</span> <button onclick="add(239)">ซื้อ</button></p>
        <p>กระเป๋าดินสอ - <span class="price">39 บาท</span> <button onclick="add(39)">ซื้อ</button></p>
        <p>แฟ้ม - <span class="price">20 บาท</span> <button onclick="add(20)">ซื้อ</button></p>
        <p>กบเหลา - <span class="price">25 บาท</span> <button onclick="add(25)">ซื้อ</button></p>
    </div>

    <div class="box">
        <h2>สรุปรายการสั่งซื้อ</h2>
        <p>ราคารวม: <span id="total">0</span> บาท</p>
        <p>ส่วนลด: <span id="discount">0</span> บาท</p>
        <h3>ยอดที่ต้องจ่าย: <span id="net">0</span> บาท</h3>
        <button onclick="resetCart()" style="background-color: red;">ล้างข้อมูล</button>
    </div>

    <script>
        let sum = 0;

        function add(price) {
            sum = sum + price;
            cal();
        }

        function resetCart() {
            sum = 0;
            cal();
        }

        function cal() {
            let dc = 0;
            if (sum >= 500 && sum <= 700) {
                dc = 2;
            } else if (sum >= 701 && sum <= 900) {
                dc = 4;
            } else if (sum > 901) {
                dc = 5;
            }

            let dcBath = (sum * dc) / 100;
            let netTotal = sum - dcBath;

            document.getElementById('total').innerText = sum;
            document.getElementById('discount').innerText = dcBath;
            document.getElementById('net').innerText = netTotal;
        }
    </script>

</body>
</html>
