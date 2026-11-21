interface Payment {
    paymentId: string;
    status: string;
    amount: number;
    currency: string;
}

async function getPayment(
    paymentId: string
): Promise<Payment> {

    const response = await fetch(
        `http://localhost:8000/payments/${paymentId}`
    );

    if (!response.ok) {
        throw new Error(
            `Payment API failed: ${response.status}`
        );
    }

    return await response.json() as Payment;
}

async function main() {
    try {
        // Sequential calls:
        const p1 = await getPayment("PAY-10001");
        console.log("Payment 1:", p1);
        const p2 = await getPayment("PAY-10002");
        console.log("Payment 2:", p2);
        const p3 = await getPayment("PAY-10003");
        console.log("Payment 3:", p3);

        // Example usage of the getPayment function call multiple APIs concurrently
        const payments = await Promise.all([
            getPayment("PAY-10001"),
            getPayment("PAY-10002"),
            getPayment("PAY-10003")
        ]);

        console.log("Payments:", payments);

    }

    catch (error) {
        if (error instanceof Error) {
            console.error(error.message);
        } else {
            console.error("Unexpected error", error);
        }
    }
}

main();