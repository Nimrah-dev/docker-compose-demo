from flask import Flask
import psycopg2
import redis
import os

app = Flask(__name__)

@app.route('/')
def home():
    return "App is running!"

@app.route('/db-check')
def db_check():
    try:
        conn = psycopg2.connect(
            host=os.environ.get('DB_HOST', 'db'),
            user='postgres',
            password='pass123',
            dbname='postgres'
        )
        conn.close()
        return "Database connection: SUCCESS"
    except Exception as e:
        return f"Database connection: FAILED - {e}"

@app.route('/cache-check')
def cache_check():
    try:
        r = redis.Redis(host=os.environ.get('REDIS_HOST', 'cache'), port=6379)
        r.set('test', 'hello')
        value = r.get('test')
        return f"Cache check: SUCCESS - {value}"
    except Exception as e:
        return f"Cache check: FAILED - {e}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
