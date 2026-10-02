
from model import train_model

_, accuracy = train_model()

html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Machine Learning CI/CD Pipeline</title>
<style>
    body {{
        font-family: Arial, sans-serif;
        background: #f4f7fb;
        margin: 0;
        min-height: 100vh;
        display: flex;
        justify-content: center;
        align-items: center;
        text-align: center;
    }}
    .container {{
        background: white;
        padding: 40px;
        border-radius: 15px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.1);
        max-width: 700px;
        width: 85%;
        box-sizing: border-box;
    }}
    h1 {{ color: #1d3557; }}
    h2 {{ color: #457b9d; }}
    p {{ font-size: 18px; margin: 18px 0; }}
    .status {{ color: #16803c; font-weight: bold; }}
</style>
</head>
<body>
<div class="container">
    <h1>Machine Learning CI/CD Pipeline</h1>
    <h2>Model: Random Forest Classifier</h2>
    <p>Dataset: Iris</p>
    <p>Accuracy: {accuracy:.2%}</p>
    <p class="status">CI Tests: Passed</p>
    <p class="status">Deployment: Successful</p>
</div>
</body>
</html>
"""

with open("index.html", "w", encoding="utf-8") as file:
    file.write(html)

print(f"Webpage generated. Model accuracy: {accuracy:.2%}")
