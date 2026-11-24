import type { Payment } from "../models/payment.js";

export interface PaymentGateway {
    getPayment(paymentId: string): Promise<Payment>;
}