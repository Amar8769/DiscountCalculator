from flask import Flask, request, jsonify, render_template


app = Flask(__name__)


@app.route('/')
def home():
    return "Welcome to the Discount Calculator API!"


@app.route('/calculate_discount', methods=['POST'])
def calculate_discount():
    data = request.get_json()
    original_price = data.get('original_price')
    discount_percentage = data.get('discount_percentage')

    if original_price is None or discount_percentage is None:
        return jsonify({'error': 'Invalid input'}), 400

    try:
        original_price = float(original_price)
        discount_percentage = float(discount_percentage)
        discount_amount = (original_price * discount_percentage) / 100
        final_price = original_price - discount_amount

        return jsonify({
            'original_price': original_price,
            'discount_percentage': discount_percentage,
            'discount_amount': discount_amount,
            'final_price': final_price
        })
    except ValueError:
        return jsonify({'error': 'Invalid input values'}), 400


@app.route('/frontend')
def frontend():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)