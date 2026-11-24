import type { Payment } from "../models/payment.js";

class PaymentApiClient {

    constructor(
        private readonly baseUrl: string
    ) {}

    async getPayment(
        paymentId: string
    ): Promise<Payment> {

        const response = await fetch(
            `${this.baseUrl}/payments/${encodeURIComponent(paymentId)}`
        );

        if (!response.ok) {
            throw new Error(
                `Payment API error: ${response.status}`
            );
        }

        return await response.json() as Payment;
    }

    async getPayments(
        paymentIds: string[]
    ): Promise<Payment[]> {
        return await Promise.all(
            paymentIds.map(paymentId => this.getPayment(paymentId))
        );
    }
}

export default PaymentApiClient;