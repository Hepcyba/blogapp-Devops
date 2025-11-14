from flask import Flask, request, jsonify
from flask_cors import CORS
from pymongo import MongoClient
from bson.objectid import ObjectId
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)
CORS(app)

# Load values from .env
MONGO_URI = os.getenv("MONGO_URI")
DB_NAME = os.getenv("DB_NAME")
COLLECTION_NAME = os.getenv("COLLECTION_NAME")

client = MongoClient(MONGO_URI)
db = client[DB_NAME]
posts = db[COLLECTION_NAME]

# ---------- POST (Create) ----------
@app.route("/posts", methods=["POST"])
def create_post():
    data = request.json
    result = posts.insert_one({
        "title": data["title"],
        "content": data["content"]
    })
    return jsonify({"msg": "Post Created", "id": str(result.inserted_id)}), 201

# ---------- GET (Read All) ----------
@app.route("/posts", methods=["GET"])
def get_posts():
    all_posts = []
    for p in posts.find():
        all_posts.append({
            "_id": str(p["_id"]),
            "title": p["title"],
            "content": p["content"]
        })
    return jsonify(all_posts), 200

# ---------- PATCH (Update) ----------
@app.route("/posts/<post_id>", methods=["PATCH"])
def update_post(post_id):
    data = request.json
    posts.update_one(
        {"_id": ObjectId(post_id)},
        {"$set": data}
    )
    return jsonify({"msg": "Post Updated"}), 200

# ---------- DELETE (Delete) ----------
@app.route("/posts/<post_id>", methods=["DELETE"])
def delete_post(post_id):
    posts.delete_one({"_id": ObjectId(post_id)})
    return jsonify({"msg": "Post Deleted"}), 200

@app.route("/", methods=["GET"])
def home():
    return jsonify({"message": "Blog API is running"}), 200


if __name__ == "__main__":
    app.run(debug=True)
