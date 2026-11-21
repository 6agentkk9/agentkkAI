// npx tsx src/index.ts
// tsx lets us run TypeScript files directly during development without manually compiling each time.

// debugging with breakpoints in VS Code:
// npx tsx --inspect-brk src/index.ts debugging with breakpoints in VS Code. The --inspect-brk flag tells Node.js to wait for a debugger to attach before executing the script.

async function main() {

    const { default: PaymentApiClient } = await import("./services/payment-api-client.js");

    const client = new PaymentApiClient(
        "http://localhost:8000"
    );



    try {
        const payment = await client.getPayment("PAY-10001");
        console.log("Payment ID:", payment.payment_id);
        console.log("Status:", payment.gateway_status);


        // Example usage of the getPayment function calling multiple APIs concurrently
        const payments = await client.getPayments(["PAY-10001", "PAY-10002", "PAY-10003"]);

        // Sample Printing of the payments array to verify the results
        console.log("Sample Printing of the payments array to verify the results:");
        payments.forEach((payment) => {
            console.log("Payment ID:", payment.payment_id);
            console.log("Status:", payment.gateway_status);
        });

        // Sample 2 to print the payments array using a for...of loop
        console.log("Sample 2 to print the payments array using a for...of loop:");
        for (const payment of payments) {
            console.log(
            payment.payment_id,
            payment.gateway_status
        );
}

    } catch (error) {
        if (error instanceof Error) {
            console.error(error.message);
        }
    }
}

main();