from flask import Flask, jsonify, request

from . import core

app = Flask(__name__)


@app.get("/ping")
def ping():
    return jsonify({"ok": True})


@app.get("/total")
def total():
    try:
        subtotal = float(request.args.get("subtotal", "100"))
        tax_rate = float(request.args.get("tax", "0.08"))
    except ValueError:
        return jsonify({"error": "invalid params"}), 400

    total_value = core.calc_total(subtotal, tax_rate)
    return jsonify({"total": total_value})


if __name__ == "__main__":
    app.run(debug=True)
