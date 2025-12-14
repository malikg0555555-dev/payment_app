from flask import Flask, render_template, request, jsonify
from abc import ABC, abstractmethod

app = Flask(__name__)

# ===============================
# Polymorphism Interface
# ===============================
class PaymentMethod(ABC):

    @abstractmethod
    def pay(self, amount):
        pass


class CreditCard(PaymentMethod):
    def pay(self, amount):
        return f"💳 Credit Card payment of Rs.{amount} successful"


class PayPal(PaymentMethod):
    def pay(self, amount):
        return f"🅿️ PayPal payment of Rs.{amount} successful"


class GooglePay(PaymentMethod):
    def pay(self, amount):
        return f"📱 Google Pay payment of Rs.{amount} successful"


# ===============================
# API Route (Backend Logic)
# ===============================
@app.route("/pay", methods=["POST"])
def pay():
    data = request.json
    method = data.get("method")
    amount = data.get("amount")

    if not method or not amount:
        return jsonify({"error": "Invalid data"}), 400

    if method == "card":
        payment = CreditCard()
    elif method == "paypal":
        payment = PayPal()
    elif method == "gpay":
        payment = GooglePay()
    else:
        return jsonify({"error": "Invalid payment method"}), 400

    # 👉 POLYMORPHISM HERE
    result = payment.pay(amount)

    return jsonify({"message": result})


# ===============================
# Home Page
# ===============================
@app.route("/")
def home():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
