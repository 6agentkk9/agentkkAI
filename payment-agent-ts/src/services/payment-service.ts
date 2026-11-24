import type { Payment } from "../models/payment.js";
import type { PaymentGateway } from "../interfaces/payment-gateway.js";

class PaymentService {

    constructor(
        private readonly gateway: PaymentGateway
    ) {}

    async investigate(
        payment_id: string
    ): Promise<Payment> {

        return this.gateway.getPayment(payment_id);
    }
}

export default PaymentService;