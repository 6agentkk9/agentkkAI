// TypeScript model for a refund investigation agent.

// A. Define RefundStatus Union type 	Restrict allowed values
type  RefundStatus =
    | "REQUESTED"
    | "VALIDATING"
    | "APPROVED"
    | "REJECTED";

// B. Define interfacev RefundRequest
interface RefundRequest {
    refundId: string;
    paymentId: string;
    amount: number;
    currency: string;
    status: RefundStatus;
}

// C. Define RefundDecision discriminated unions Represent different agent decisions
type RefundDecision =
    | { type: "APPROVE"; reason: string }
    | { type: "REJECT"; reason: string }
    | { type: "REVIEW"; reviewer: string };

// D. Implement processRefundDecision
function processRefundDecision(decision: RefundDecision): string {
    switch (decision.type) {
        case "APPROVE":
           return `Approved: ${decision.reason}`;
        case "REJECT":
            return `Rejected: ${decision.reason}`;
        case "REVIEW":
            return `Under review by ${decision.reviewer}`;
    }
}

// Test your function with an APPROVE decision.
const result = processRefundDecision({
    type: "APPROVE",
    reason: "Refund is within policy"
});

console.log(result);
