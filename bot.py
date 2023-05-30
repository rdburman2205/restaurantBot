import json
import random
import string

from flask import Flask, jsonify, make_response

app = Flask(__name__)

def generate_unique_id():
    characters = string.digits
    unique_id = ''.join(random.choice(characters) for _ in range(6))
    return unique_id

@app.route('/api/text', methods=['POST'])
def get_text():
    characters = string.digits
    unique_id = ''.join(random.choice(characters) for _ in range(6))
    result = {
        "fulfillmentMessages": [
            {
                "text": {
                    "text": [
                        "Your order is placed, order id is " + unique_id + ". Do you want to know more about us ?"
                    ]
                }
            }
        ]
    }
    return jsonify(result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
