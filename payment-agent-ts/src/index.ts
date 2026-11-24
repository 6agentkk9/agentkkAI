// npm.cmd --version

// node --env-file=src/.env --import tsx --watch src/index.ts

// $env:PAYMENT_API_URL = "http://localhost:8000"
// npm.cmd run dev
// npm.cmd start

// & "C:\Program Files\nodejs\npx.cmd" tsx src/index.ts
// npx tsx src/index.ts

// tsx lets us run TypeScript files directly during development without manually compiling each time.

// debugging with breakpoints in VS Code:
// npx tsx --inspect-brk src/index.ts debugging with breakpoints in VS Code. The --inspect-brk flag tells Node.js to wait for a debugger to attach before executing the script.

// node --env-file=src/.env --import tsx --watch src/index.ts

import PaymentService from "./services/payment-service.js";
import { MockPaymentGateway } from "./services/mock-payment-gateway.js";

import { settings } from "./config/settings.js";
import { logger } from "./config/logger.js";

const service = new PaymentService(
    new MockPaymentGateway()
);

import type { Incident } from "./models/incident.js";

const incident: Incident = {
    incidentId: "INC-10001",
    paymentId: "PAY-10001",
    errorCode: "GATEWAY_TIMEOUT",
    description: "Payment gateway did not respond",
    status: "OPEN"
};

logger.info({ incident }, "Incident recorded");


async function main(): Promise<void> {

    logger.info(
        {
            application: settings.appName,
            environment: settings.nodeEnv
        },
        "Application starting"
    );

    logger.info(
        {
            paymentApiUrl: settings.paymentApiUrl
        },
        "Payment API configuration loaded"
    );

    logger.info("Payment AI Agent is ready");

    // USe case 1: Investigate a payment using the PaymentService
    const gateway = new MockPaymentGateway();
    const service = new PaymentService(gateway);
    const payment = await service.investigate("PAY-10001");

    console.log(payment);

     // USe case 2: Investigate a payment using the PaymentApiClient
    // const { default: PaymentApiClient } = await import("./services/payment-api-client.js");


    // const client = new PaymentApiClient(
    //     "http://localhost:8000"
    // );



    // try {
    //     const payment = await client.getPayment("PAY-10001");
    //     console.log("Payment ID:", payment.payment_id);
    //     console.log("Status:", payment.gateway_status);


    //     // Example usage of the getPayment function calling multiple APIs concurrently
    //     const payments = await client.getPayments(["PAY-10001", "PAY-10002", "PAY-10003"]);

    //     // Sample Printing of the payments array to verify the results
    //     console.log("Sample Printing of the payments array to verify the results:");
    //     payments.forEach((payment) => {
    //         console.log("Payment ID:", payment.payment_id);
    //         console.log("Status:", payment.gateway_status);
    //     });

    //     // Sample 2 to print the payments array using a for...of loop
    //     console.log("Sample 2 to print the payments array using a for...of loop:");
    //     for (const payment of payments) {
    //         console.log(
    //         payment.payment_id,
    //         payment.gateway_status
    //     );
    // } catch (error) {
    //     if (error instanceof Error) {
    //         console.error(error.message);
    //     }
    // }

}

main().catch((error: unknown) => {

    if (error instanceof Error) {
        logger.error(
            { err: error },
            "Application startup failed"
        );
    } else {
        logger.error(
            { error },
            "Application startup failed"
        );
    }
});