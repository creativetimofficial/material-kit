from flask import Flask, request, send_from_directory

app = Flask(__name__)

@app.route('/')
def main():
    return "main"

@app.route('/sections/input-areas/inputs.html')
def serve_inputs_html():
    return send_from_directory('static/sections/input-areas', 'inputs.html')

# Route to handle form submission
@app.route('/submit', methods=['POST'])
def submit():
    first_name = request.form.get('first_name')
    return f"Received First Name: {first_name}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
