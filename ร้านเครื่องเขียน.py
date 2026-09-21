<!DOCTYPE html>
<html lang="th">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>ร้านเครื่องเขียนราคาถูก (Stationery Shop)</title>
    <style>
        {
            box-sizing: border-box;
            margin: 0;
            padding: 0;
            font-family: 'Tahoma', sans-serif;
        }
        body {
            background-color: #f4f6f8;
            color: #333;
        }
        header {
            background-color: #4A90E2;
            color: white;
            text-align: center;
            padding: 2rem 1rem;
        }
        header h1 {
            font-size: 2rem;
            margin-bottom: 0.5rem;
        }
        .container {
            max-width: 1000px;
            margin: 2rem auto;
            padding: 0 1rem;
        }
        .product-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
            gap: 1.5rem;
        }
        .product-card {
            background: white;
            border-radius: 8px;
            box-shadow: 0 2px 8px rgba(0,0,0,0.1);
            padding: 1rem;
            text-align: center;
            display: flex;
            flex-direction: column;
            justify-content: space-between;
        }
        .product-card img {
            width: 100%;
            height: 150px;
            object-fit: cover;
            border-radius: 6px;
            margin-bottom: 1rem;
        }
        .product-title {
            font-size: 1.1rem;
            margin-bottom: 0.5rem;
        }
        .price {
            color: #e74c3c;
            font-size: 1.2rem;
            font-weight: bold;
            margin-bottom: 1rem;
        }
        .btn-buy {
            display: inline-block;
            background-color: #27ae60;
            color: white;
            text-decoration: none;
            padding: 0.6rem 1rem;
            border-radius: 4px;
            font-weight: bold;
            transition: background 0.2s;
        }
        .btn-buy:hover {
            background-color: #219150;
        }
        footer {
            text-align: center;
            padding: 1.5rem;
            background: #e9ecef;
            margin-top: 3rem;
            font-size: 0.9rem;
        }
    </style>
</head>
<body>

    <header>
        <h1>✏️ ร้านเครื่องเขียนราคา67</h1>
        <p>อุปกรณ์การเรียน สำนักงาน คุณภาพดี ราคาเป็นกันเอง</p>
    </header>

    <div class="container">
        <div class="product-grid">
            
            <!-- สินค้าชิ้นที่ 1 -->
            <div class="product-card">
                <img src="https://images.unsplash.com/photo-1585336261026-8f5786372969?w=300" alt="ปากกาลูกลื่น">
                <div class="product-title">ปากกาลูกลื่น 0.5 มม. (แพ็ค 5 ด้าม)</div>
                <div class="price">฿25</div>
                <!-- เปลี่ยน ลิงก์ Line ID หรือเพจ Facebook ได้ตรงนี้ -->
                <a href="https://line.me/ti/p/~YOUR_LINE_ID" class="btn-buy" target="_blank">สั่งซื้อทาง LINE</a>
            </div>

            <!-- สินค้าชิ้นที่ 2 -->
            <div class="product-card">
                <img src="https://images.unsplash.com/photo-1544816155-12df9643f363?w=300" alt="สมุดโน้ต">
                <div class="product-title">สมุดโน้ตมีเส้น A5 (80 แผ่น)</div>
                <div class="price">฿35</div>
                <a href="https://line.me/ti/p/~YOUR_LINE_ID" class="btn-buy" target="_blank">สั่งซื้อทาง LINE</a>
            </div>

            <!-- สินค้าชิ้นที่ 3 -->
            <div class="product-card">
                <img src="https://images.unsplash.com/photo-1513542789411-b6a5d4f31634?w=300" alt="ชุดดินสอไม้">
                <div class="product-title">ดินสอไม้ 2B (กล่อง 12 ด้าม)</div>
                <div class="price">฿40</div>
                <a href="https://line.me/ti/p/~YOUR_LINE_ID" class="btn-buy" target="_blank">สั่งซื้อทาง LINE</a>
            </div>

            <!-- สินค้าชิ้นที่ 4 -->
            <div class="product-card">
                <img src="https://images.unsplash.com/photo-1583485088034-697b5bc54ccd?w=300" alt="โพสต์อิท">
                <div class="product-title">กระดาษโน้ตดักกี้ (Post-it) คละสี</div>
                <div class="price">฿15</div>
                <a href="https://line.me/ti/p/~YOUR_LINE_ID" class="btn-buy" target="_blank">สั่งซื้อทาง LINE</a>
            </div>

        </div>
    </div>

    <footer>
        <p>สนใจสั่งซื้อจำนวนมาก หรือสอบถามเพิ่มเติม ติดต่อ Line: @YOUR_LINE_ID | โทร: 08X-XXX-XXXX</p>
    </footer>

</body>
</html>
