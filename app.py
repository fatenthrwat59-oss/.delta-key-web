from flask import Flask, render_template_string
app = Flask(__name__)
html = """
<!DOCTYPE html>
<html lang="ar">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Delta Key System</title>
    <style>
        body { background: radial-gradient(circle, #1a1a1a 0%, #000 100%); color: white; font-family: sans-serif; display: flex; align-items: center; justify-content: center; height: 100vh; margin: 0; }
        .container { background: rgba(25, 25, 25, 0.95); padding: 35px; border-radius: 30px; box-shadow: 0 0 30px rgba(0, 210, 255, 0.3); text-align: center; width: 85%; max-width: 380px; border: 1px solid #00d2ff; }
        h2 { color: #00d2ff; text-transform: uppercase; margin-bottom: 30px; }
        .btn { display: block; width: 100%; padding: 15px; margin: 12px 0; border: none; border-radius: 15px; font-weight: bold; cursor: pointer; transition: 0.5s; }
        .btn-task { background: transparent; color: #00d2ff; border: 2px solid #00d2ff; }
        #final-btn { background-color: #333; color: #666; cursor: not-allowed; margin-top: 25px; }
        #final-btn.active { background: linear-gradient(45deg, #00d2ff, #38ef7d); color: white; cursor: pointer; box-shadow: 0 0 20px rgba(56, 239, 125, 0.6); }
        .footer { margin-top: 30px; font-size: 12px; color: #444; }
    </style>
</head>
<body>
    <div class="container">
        <h2>Delta Key</h2>
        <button class="btn btn-task" onclick="complete(1)">Sub Channel</button>
        <button class="btn btn-task" onclick="complete(2)">Like Video</button>
        <button id="final-btn" class="btn">Copy Website Link</button>
        <div id="msg" style="display:none; color:#38ef7d; margin-top:10px;">✅ تم النسخ بنجاح!</div>
        <div class="footer">DEVELOPED BY: <b>MAALEK_1234</b></div>
    </div>
    <script>
        let t1=false, t2=false;
        function complete(n){
            if(n==1) t1=true; if(n==2) t2=true;
            if(t1 && t2){ 
                let b = document.getElementById('final-btn');
                b.classList.add('active');
                b.innerText = "نسخ الرابط";
                b.onclick = function() {
                    navigator.clipboard.writeText("https://get-key-delta.com");
                    document.getElementById('msg').style.display = 'block';
                };
            }
        }
    </script>
</body>
</html>
"""
@app.route('/')
def home(): return render_template_string(html)
if __name__ == '__main__': app.run(host='0.0.0.0', port=5000)
  
