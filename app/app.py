from flask import Flask, render_template
import pymysql

app = Flask(__name__)

# Database connection (MySQL)
db = pymysql.connect(
    host='47.129.22.75',
    user='admin117',
    password='angeline117!',
    database='ecom1db'
)

@app.route('/')
def index():
    cursor = db.cursor()
    cursor.execute("SELECT product_name, price, image_url FROM products")
    products = cursor.fetchall()
    return render_template('index.html', products=products)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)