from flask import Flask, render_template_string

app = Flask(__name__)

html_code = """
<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Delta Key System | Pro</title>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
    <style>
        :root {
            --primary: #00d2ff;
            --secondary: #38ef7d;
            --bg: #0f0f0f;
            --card-bg: #1a1a1a;
        }
        body { 
            background: radial-gradient(circle at center, #1a1a1a 0%, #000 100%); 
            color: white; 
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; 
            display: flex; 
            align-items: center; 
            justify-content: center; 
            height: 100vh; 
            margin: 0;
            overflow: hidden;
        }
        .container { 
            background: var(--card-bg); 
            padding: 40px; 
            border-radius: 25px; 
            box-shadow: 0 15px 35px rgba(0,0,0,0.5), 0 0 20px rgba(0, 210, 255, 0.2); 
            text-align: center; 
            width: 90%; 
            max-width: 400px; 
            border: 1px solid rgba(0, 210, 255, 0.3);
        }
        .logo-area { font-size: 50px; color: var(--primary); margin-bottom: 10px; text-shadow: 0 0 15px var(--primary); }
        h2 { font-size: 24px; margin-bottom: 30px; letter-spacing: 2px; color: #fff; }
        
        .btn { 
            display: flex; 
            align-items: center; 
            justify-content: center; 
            gap: 12px;
            width: 100%; 
            padding: 16px; 
            margin: 15px 0; 
            border: none; 
            border-radius: 12px; 
            font-weight: bold; 
            cursor: pointer; 
            transition: all 0.3s ease; 
            font-size: 16px;
            text-decoration: none;
            position: relative;
            overflow: hidden;
        }
        
        /* زر الاشتراك */
        .btn-sub { background: #ff0000; color: white; }
        .btn-sub:hover { transform: translateY(-2px); background: #cc0000; }
        
        /* زر الانتظار مع تأثير التحميل */
        .btn-wait { background: #222; color: var(--primary); border: 2px solid var(--primary); }
        .btn-wait:disabled { border-color: #444; color: #666; cursor: not-allowed; }
        
        .loader {
            width: 20px;
            height: 20px;
            border: 3px solid rgba(0, 210, 255, 0.3);
            border-radius: 50%;
            border-top-color: var(--primary);
            animation: spin 1s ease-in-out infinite;
            display: none; /* يظهر فقط عند البدء */
        }

        @keyframes spin { to { transform: rotate(360deg); } }

        /* الزر النهائي */
        #final-btn { background: #333; color: #555; cursor: not-allowed; }
        #final-btn.active { 
            background: linear-gradient(45deg, var(--primary), var(--secondary)); 
            color: white; 
            cursor: pointer; 
            box-shadow: 0 5px 15px rgba(56, 239, 125, 0.4);
            animation: pulse 1.5s infinite;
        }

        @keyframes pulse {
            0% { transform: scale(1); }
            50% { transform: scale(1.02); }
            100% { transform: scale(1); }
        }

        #msg { display: none; color: var(--secondary); margin-top: 15px; font-weight: bold; animation: fadeIn 0.5s; }
    </style>
</head>
<body>
    <div class="container">
        <div class="logo-area"><i class="fas fa-shield-alt"></i></div>
        <h2>DELTA SYSTEM</h2>
        
        <a href="https://youtube.com/@husseintharwat810?si=rLtuHlbthv-DAoO6" target="_blank" class="btn btn-sub" onclick="step1()">
            <i class="fab fa-youtube"></i> SUBSCRIBE TO START
        </a>

        <button id="wait-btn" class="btn btn-wait" onclick="step2()" disabled>
            <i class="fas fa-lock"></i> WAIT FOR VERIFY
        </button>

        <button id="final-btn" class="btn">
            <i class="fas fa-key"></i> GET KEY LINK
        </button>

        <p id="msg"><i class="fas fa-check-double"></i> Done! Link Copied Master.</p>
        
        <div style="margin-top:20px; font-size:10px; color:#444;">DEV BY MAALEK_1234</div>
    </div>

    <script>
        let s1 = false;

        function step1() {
            s1 = true;
            let wb = document.getElementById('wait-btn');
            wb.disabled = false;
            wb.innerHTML = '<i class="fas fa-unlock"></i> CLICK TO PROCESS';
            wb.style.borderColor = "#38ef7d";
            wb.style.color = "#38ef7d";
        }

        function step2() {
            if(!s1) return;
            let btn = document.getElementById('wait-btn');
            btn.disabled = true;
            // إضافة أيقونة التحميل المتحركة
            btn.innerHTML = '<div class="loader" id="ld" style="display:block"></div> <span id="txt">WAITING... 5s</span>';
            
            let timeLeft = 4; // نبدأ بـ 5 ثوانٍ
            let timer = setInterval(function() {
                document.getElementById('txt').innerText = "WAITING... " + timeLeft + "s";
                timeLeft -= 1;
                
                if(timeLeft < 0) {
                    clearInterval(timer);
                    btn.innerHTML = '<i class="fas fa-check-circle" style="color:#38ef7d"></i> VERIFIED';
                    activateFinal();
                }
            }, 1000);
        }

        function activateFinal() {
            let f = document.getElementById('final-btn');
            f.classList.add('active');
            f.innerHTML = '<i class="fas fa-external-link-alt"></i> COPY LINK NOW';
            f.onclick = function() {
                const el = document.createElement('textarea');
                el.value = "https://get-key-delta.com";
                document.body.appendChild(el);
                el.select();
                document.execCommand('copy');
                document.body.removeChild(el);
                document.getElementById('msg').style.display = 'block';
            };
        }
    </script>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(html_code)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
    
