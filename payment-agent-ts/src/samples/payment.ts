interface Payment {
    paymentId: string;
    amount: number;
    status: string;
    currency: string;
}

function isPaymentFailed(payment: Payment): boolean {
    return payment.status === "FAILED";
}

const payment: Payment = {
    paymentId: "PAY-10001",
    amount: 150.50,
    status: "FAILED",
    currency: "USD"
};

console.log("Payment ID:", payment.paymentId);
console.log("Failed:", isPaymentFailed(payment));