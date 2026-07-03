from src.database import client

try:
    client.admin.command("ping")
    print("✅ Successfully connected to MongoDB!")
except Exception as e:
    print("❌ Connection failed!")
    print(e)