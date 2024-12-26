import json

from flask import Flask, jsonify, request
import psycopg2
import redis

app = Flask(__name__)

# Configure PostgreSQL connection
db_config = {
    "dbname": "mydatabase",
    "user": "user",
    "password": "password",
    "host": "postgres_service",  # Docker Compose service name for the database
    "port": 5432
}

redis_client = redis.Redis(host="redis_service", port=6379)

@app.route('/')
def home():
    return jsonify({"message": "Welcome to my Python Flask App!"})

@app.route('/data', methods=['POST'])
def insert_data():
    # Get data from request
    name = request.json.get('name')
    email = request.json.get('email')

    # Insert data into PostgreSQL
    try:
        conn = psycopg2.connect(**db_config)
        cursor = conn.cursor()
        cursor.execute("INSERT INTO users (name , email ) VALUES (%s , %s);", (name,email))
        conn.commit()
        cursor.close()
        conn.close()
    except Exception as e:
        return jsonify({"error": str(e)}), 500

    # Cache data in Redis
    redis_client.set('latest_data', json.dumps({'name': name , 'email': email}))

    return jsonify({"message": "Data saved successfully!"})

@app.route('/data', methods=['GET'])
def get_data():
    cached_data = redis_client.get('latest_data')
    if cached_data:
        cached_data = json.loads(cached_data)
        return jsonify({"source": "cache", "data": cached_data})
    try:
        conn = psycopg2.connect(**db_config)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users ORDER BY id Desc LIMIT 1;")
        row = cursor.fetchone()
        cursor.close()
        conn.close()
        data=[]
        if row:
            return jsonify({'name': row[1] , 'email': row[2]})
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

