from flask import Flask, render_template
import psycopg2

app = Flask(__name__)

# Database connection (PostgreSQL)
db = psycopg2.connect(
    host='ecom-db1.chm448q8s314.ap-southeast-1.rds.amazonaws.com',
    user='admin117',
    password='angeline117!',
    dbname='ecom-db1'
)

@app.route('/')
def index():
    cursor = db.cursor()
    cursor.execute("SELECT product_name, price, image_url FROM products")
    products = cursor.fetchall()
    return render_template('index.html', products=products)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
