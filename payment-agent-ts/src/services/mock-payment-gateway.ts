import type { Payment } from "../models/payment.js";
import type { PaymentGateway } from "../interfaces/payment-gateway.js";

class MockPaymentGateway implements PaymentGateway {

    async getPayment(
        payment_id: string
    ): Promise<Payment> {


        return {
            payment_id,
            gateway_status: "FAILED fronm MockPaymentGateway",
            amount: 150.50,
            currency: "USD"
        };
    }
}

export { MockPaymentGateway };