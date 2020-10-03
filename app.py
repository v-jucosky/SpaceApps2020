from flask import Flask


app = Flask(__name__)

html = """
<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <title>Nasa Hackathon</title>
</head>
<body>
    <div>
        <h1>hello, World!</h1>
        <p>Principalmente você, Marte</p>
    </div>
</body>
</html>
"""

@app.route('/')
def index():
    return html