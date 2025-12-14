function makePayment() {
    const method = document.getElementById("method").value;
    const amount = document.getElementById("amount").value;
    const result = document.getElementById("result");

    if (!method || !amount) {
        result.innerHTML = "❌ Please select method and enter amount";
        return;
    }

    result.innerHTML = "⏳ Processing payment...";

    fetch("/pay", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            method: method,
            amount: amount
        })
    })
    .then(res => res.json())
    .then(data => {
        result.innerHTML = data.message || data.error;
    })
    .catch(() => {
        result.innerHTML = "❌ Server error. Try again.";
    });
}
