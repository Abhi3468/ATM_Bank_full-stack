document.addEventListener("DOMContentLoaded", function() {
    const pinVerificationForm = document.getElementById("pinVerificationForm");
    const balanceBtn = document.getElementById("balanceBtn");
    const withdrawBtn = document.getElementById("withdrawBtn");
    const depositBtn = document.getElementById("depositBtn");
    const pinChangeBtn = document.getElementById("pinChangeBtn");
    const dynamicInputs = document.getElementById("dynamicInputs");
    const messageDiv = document.getElementById("message");
    let pinVerified = false;

    function getCSRFToken() {
        const cookieValue = document.cookie
            .split("; ")
            .find(cookie => cookie.startsWith("csrftoken="))
            .split("=")[1];
        return cookieValue;
    }

    function showMessage(message) {
        messageDiv.innerHTML = message;
    }

    function showError(error) {
        showMessage(`<span style="color: red;">Error: ${error}</span>`);
    }

    function showPopup(message) {
        const modal = document.getElementById("popupModal");
        const popupMessage = document.getElementById("popupMessage");
        popupMessage.textContent = message;
        modal.style.display = "block";

        const closeButton = document.querySelector(".close");
        closeButton.addEventListener("click", function() {
            modal.style.display = "none";
        });
    }

    pinVerificationForm.addEventListener("submit", function(event) {
        event.preventDefault();
        const cardPin = document.getElementById("card_pin").value;
        const csrftoken = getCSRFToken();
        fetch("/verify_pin/", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
                "X-CSRFToken": csrftoken
            },
            body: JSON.stringify({ card_pin: cardPin })
        })
        .then(response => response.json())
        .then(data => {
            if (data.message === "Verified") {
                showPopup("PIN Verified");
                pinVerified = true;
                localStorage.setItem('card_number', data.card_number);
               // console.log(data.card_number); // Store account number
            } else {
                showError("Invalid PIN");
            }
        })
        .catch(error => {
            showError("Unable to verify PIN");
            console.error("Error:", error);
        });
    });

    balanceBtn.addEventListener("click", function() {
        if (!pinVerified) return;
        const cardNumber = localStorage.getItem("card_number"); // Get account number from local storage
        if (!cardNumber) {
            showError("Account number is missing.");
            return;
        }
        fetch("/available_balance/", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
                "X-CSRFToken": getCSRFToken()
            },
            body: JSON.stringify({ card_number: cardNumber })
        })
        .then(response => response.json())
        .then(data => {
            if (data.balance !== undefined) {
                showPopup("Balance: INR " + data.balance);
            } else {
                showError("Balance is undefined");
            }
        })
        .catch(error => {
            showError("Unable to fetch balance");
            console.error("Error:", error);
        });
    });

    function performTransaction(url, messagePrefix) {
        const amount = prompt("Enter Amount:");
        if (amount !== null) {
            const csrftoken = getCSRFToken();
            const cardNumber = localStorage.getItem("card_number");
            fetch(url, {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                    "X-CSRFToken": csrftoken
                },
                body: JSON.stringify({ card_number: cardNumber, amount: amount })
            })
            .then(response => response.json())
            .then(data => {
                showPopup(messagePrefix + data.new_balance);
            })
            .catch(error => {
                showError("Unable to perform transaction");
                console.error("Error:", error);
            });
        }
    }

    withdrawBtn.addEventListener("click", function() {
        if (!pinVerified) return;
        performTransaction("/withdraw/", "Withdrawal successful. \n New Balance: INR ");
    });

    depositBtn.addEventListener("click", function() {
        if (!pinVerified) return;
        performTransaction("/deposit/", "Deposit successful. \n New Balance: INR ");
    });

    pinChangeBtn.addEventListener("click", function() {
        if (!pinVerified) return;
        const newPin = prompt("Enter New PIN:");
        if (newPin !== null) {
            const csrftoken = getCSRFToken();
            const cardNumber = localStorage.getItem("card_number");
            fetch("/pin_change/", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                    "X-CSRFToken": csrftoken
                },
                body: JSON.stringify({ card_number: cardNumber, new_pin: newPin })
            })
            .then(response => response.json())
            .then(data => {
                showPopup(data.message);
            })
            .catch(error => {
                showError("Unable to change PIN");
                console.error("Error:", error);
            });
        }
    });

});
