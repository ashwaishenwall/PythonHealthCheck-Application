from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/ashwani/shenwall/working')
def health_check():
    status = {"status": "OK", "message": "Ashwani everything is fine!"}
    return jsonify(status)

if __name__ == '__main__':
    # Important: listen on all interfaces inside container
    app.run(host='0.0.0.0', port=5000)
#..
