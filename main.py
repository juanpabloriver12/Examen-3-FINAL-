from flask import Flask
 
app = Flask(__name__)
 
@app.route('/')
def index():
    return '''
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Caz, te voy a extrañar</title>
<style>
            body {
                background-color: #111;
                color: white;
                font-family: Arial, sans-serif;
                text-align: center;
                padding: 5%;
            }
            button {
                background-color: #222;
                border: none;
                color: white;
                margin: 10px;
                padding: 10px 20px;
                cursor: pointer;
                transition: all 0.3s ease;
                font-size: 1em;
                border-radius: 8px;
            }
            button:hover {
                background-color: #333;
                transform: scale(1.05);
            }
            #message {
                margin-top: 2em;
                font-style: italic;
                color: #aaa;
            }
</style>
<script>
            function showMessage(msg) {
                document.getElementById('message').innerText = msg;
            }
</script>
</head>
<body>
<h1>Caz, te voy a extrañar...</h1>
<p>Gracias por todo 🖤</p>
<!-- Imagen con link externo -->
<img src="https://www.shutterstock.com/image-photo/joyful-multiethnic-classmates-looking-camera-260nw-2016786968.jpg" /> 
        <div class="buttons">
<button onclick="showMessage('Siempre estarás en nuestros corazónes')">❤️</button>
<button onclick="showMessage('Hasta pronto, no adiós')">🌙</button>
</div>
 
        <div id="message"></div>
</body>
</html>
    '''
print(html)
return html 
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8005)
