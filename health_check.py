from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/ashwani/shenwall/working')
def health_check():
    # Check the health of your application here
    # You can add more sophisticated checks based on your application's requirements

    # For demonstration purposes, let's assume the application is always healthy
    status = {"status": "OK", "message": "Ashwani everything is fine!"}

    return jsonify(status)

if __name__ == '__main__':
    app.run()

