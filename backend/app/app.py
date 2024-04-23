import traceback

from flask import Flask, request, jsonify
from pymongo import MongoClient

app = Flask(__name__)

# Connect to MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['lead_in_water']
collection = db['grand_rapids']


# Define route to handle the address search
@app.route('/api/getPropertyByAddress', methods=['GET'])
def get_property_by_address():
    try:
        address = request.args.get('address')

        # Query MongoDB for the document with the given address
        property_data = collection.find_one({'abbreviatedAddress': address})

        if property_data:
            # Convert ObjectId to a serializable format
            property_data['_id'] = str(property_data['_id'])

            # If document found, return it as JSON response
            return jsonify(property_data), 200
        else:
            # If document not found, return 404 error
            return jsonify({'error': 'Property not found'}), 404
    except Exception as e:
        traceback.print_exc()  # Print the traceback to the console
        return jsonify({'error': 'An internal server error occurred'}), 500


if __name__ == '__main__':
    app.run(debug=True)