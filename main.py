from flask import Flask, render_template
import json

app = Flask(__name__)


@app.route('/')
def render_sku_data():
    with open('data.json', 'r') as f:
        sku_data = json.load(f)
        return render_template('index.html', sku_data=sku_data)


if __name__ == "__main__":
    app.run(debug=True, port=8000)
