from flask import Flask, render_template
import pymysql

app = Flask(__name__)

# Database connection (PostgreSQL)
db = pymysql.connect(
    host='ecom1-db.chm448q8s314.ap-southeast-1.rds.amazonaws.com',
    user='admin117',
    password='angeline117!',
    database='ecom1-db'
)

@app.route('/')
def index():
    cursor = db.cursor()
    cursor.execute("SELECT product_name, price, image_url FROM products")
    products = cursor.fetchall()
    return render_template('index.html', products=products)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
