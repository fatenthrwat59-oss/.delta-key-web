from flask import Flask, render_template_string

app = Flask(__name__)

html_code = """
<!DOCTYPE html>
<html lang="ar">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>AURA EXECUTOR | PRO</title>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
    <style>
        :root { --primary: #bc13fe; --secondary: #7a18ff; --bg: #050505; }
        body { background: var(--bg); color: white; font-family: 'Poppins', sans-serif; display: flex; align-items: center; justify-content: center; height: 100vh; margin: 0; }
        .card { background: #111; padding: 40px; border-radius: 30px; border: 1px solid #333; text-align: center; width: 350px; box-shadow: 0 0 30px rgba(188, 19, 254, 0.2); }
        .logo { font-size: 60px; color: var(--primary); margin-bottom: 10px; text-shadow: 0 0 20px var(--primary); }
        h1 { letter-spacing: 5px; font-size: 24px; margin-bottom: 30px; background: linear-gradient(to right, #bc13fe, #7a18ff); -webkit-background-clip: text; -webkit-text-fill-color: transparent; }
        .btn { display: block; width: 100%; padding: 15px; margin: 15px 0; border-radius: 15px; border: none; font-weight: bold; cursor: pointer; transition: 0.3s; text-decoration: none; font-size: 14px; }
        .btn-yt { background: #ff0000; color: white; }
        .btn-wait { background: #222; color: #bc13fe; border: 1px solid #bc13fe; }
        .btn-final { background: #333; color: #555; cursor: not-allowed; }
        .btn-final.active { background: linear-gradient(45deg, var(--primary), var(--secondary)); color: white; cursor: pointer; box-shadow: 0 0 20px var(--primary); }
        .loader { width: 15px; height: 15px; border: 2px solid #333; border-top: 2px solid var(--primary); border-radius: 50%; animation: spin 1s linear infinite; display: inline-block; margin-right: 10px; vertical-align: middle; }
        @keyframes spin { 0% { transform: rotate(0deg); } 100% { transform: rotate(360deg); } }
    </style>
</head>
<body>
    <div class="card">
        <div class="logo"><i class="fas fa-atom"></i></div>
        <h1>AURA SYSTEM</h1>
        <a href="https://youtube.com/@husseintharwat810?si=rLtuHlbthv-DAoO6" target="_blank" class="btn btn-yt" onclick="s1()">SUBSCRIBE TO UNLOCK</a>
        <button id="wb" class="btn btn-wait" onclick="s2()" disabled>WAITING...</button>
        <button id="fb" class="btn btn-final">GET EXECUTOR LINK</button>
    </div>
    <script>
        let step = 0;
        function s1() { step = 1; document.getElementById('wb').disabled = false; document.getElementById('wb').innerText = 'START PROCESS'; }
        function s2() {
            if(step<1) return;
            let b = document.getElementById('wb');
            b.disabled = true;
            let t = 5;
            let i = setInterval(() => {
                b.innerHTML = `<div class="loader"></div> PROCESSING ${t}s`;
                t--;
                if(t < 0) {
                    clearInterval(i);
                    b.innerText = 'VERIFIED ✅';
                    let f = document.getElementById('fb');
                    f.classList.add('active');
                    f.onclick = () => {
                        navigator.clipboard.writeText('https://get-key-delta.com');
                        alert('Link Copied, Master!');
                    };
                }
            }, 1000);
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
    
