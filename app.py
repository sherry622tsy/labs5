from flask import Flask, request, jsonify
import psycopg2
from config import DB_CONFIG

app = Flask(__name__)

# Create DB connection
def get_db_connection():
    conn = psycopg2.connect(**DB_CONFIG)
    return conn

# -------- Create new User ----------
@app.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    name = data.get('name')
    email = data.get('email')
    height = data.get('height_cm')
    weight = data.get('weight_kg')

    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO users (name, email, height_cm, weight_kg) VALUES (%s, %s, %s, %s) RETURNING id;",
        (name, email, height, weight)
    )
    user_id = cur.fetchone()[0]
    conn.commit()
    cur.close()
    conn.close()
    return jsonify({"success": True, "user_id": user_id}), 201

# ---------- Read All Users ----------
@app.route('/users', methods=['GET'])
def get_users():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT id, name, email, height_cm, weight_kg FROM users;")
    rows = cur.fetchall()
    cur.close()
    conn.close()
    users = []
    for row in rows:
        users.append({
            "id": row[0],
            "name": row[1],
            "email": row[2],
            "height_cm": row[3],
            "weight_kg": float(row[4])
        })
    return jsonify({"success": True, "users": users})

# ---------- Read Single User ----------
@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT id, name, email, height_cm, weight_kg FROM users WHERE id = %s;", (user_id,))
    row = cur.fetchone()
    cur.close()
    conn.close()
    if row:
        return jsonify({
            "id": row[0],
            "name": row[1],
            "email": row[2],
            "height_cm": row[3],
            "weight_kg": float(row[4])
        })
    else:
        return jsonify({"error": "User not found"}), 404

# ---------- Update User ----------
@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    data = request.get_json()
    name = data.get('name')
    email = data.get('email')
    height = data.get('height_cm')
    weight = data.get('weight_kg')

    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("""
        UPDATE users 
        SET name = %s, email = %s, height_cm = %s, weight_kg = %s
        WHERE id = %s;
    """, (name, email, height, weight, user_id))
    conn.commit()
    cur.close()
    conn.close()
    return jsonify({"success": True, "message": "User updated"})

# ---------- Delete User ----------
@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("DELETE FROM users WHERE id = %s;", (user_id,))
    conn.commit()
    cur.close()
    conn.close()
    return jsonify({"success": True, "message": f"User {user_id} deleted"})

# ---------- Run ----------
if __name__ == '__main__':
    app.run(debug=True)
