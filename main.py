import os
from dotenv import load_dotenv
import pymongo

#setting up MongoDB and collections
load_dotenv()

mongodb_uri = os.getenv("MONGO_URI")
client = pymongo.MongoClient(mongodb_uri)
db = client["chop-n-shop"]
users_collection = db["users"]
stores_collection = db["stores"]
items_collection = db["items"]
recipes_collection = db["recipes"]

try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

#creating user documents
def add_user():

    #getting user inputs
    first_name = input("Enter First Name: ")
    email = input("Enter Email: ")
    budget = float(input("Enter Budget: "))
    dietary_restrictions = input("Enter Dietary Restrictions (comma-separated): ").split(",")
    allergies = input("Enter Allergies (comma-separated): ").split(",")
    food_request = input("Enter Food Request (comma-separated): ").split(",")
    preferred_stores = input("Enter Preferred Stores (comma-separated): ").split(",")
    
    #inserting into user documents
    user_document = {,
        "First_name": first_name,
        "Email": email,
        "Budget": budget,
        "Dietary_restrictions": [d.strip() for d in dietary_restrictions],
        "Allergies": [a.strip() for a in allergies],
        "Food_request": [f.strip() for f in food_request],
        "Preferred_stores": [s.strip() for s in preferred_stores]
    }
    
    try:
        result = users_collection.insert_one(user_document)
        print(f"User {first_name} added with ID: {result.inserted_id}")
    except pymongo.errors.PyMongoError as e:
        print(f"An error occurred while adding the user: {e}")

add_user()

#creating store documents

#creating item documents

#creating recipe documents

client.close()
