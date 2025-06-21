from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/sheet-update', methods=['POST'])
def sheet_update():
    data = request.json
    print("📥 收到通知:", data)
    return jsonify({"status": "ok"}), 200

if __name__ == '__main__':
    app.run()