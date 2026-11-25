import type { GraphNode } from "@langchain/langgraph";
import { PaymentIncidentState } from "./state.js";

interface PaymentRetrieval {
    paymentStatus: "FAILED" | "SUCCESS";
    investigationSteps: string[];
}

interface GatewayCheck {
    gatewayResponse: "51 - Insufficient funds" | "00 - Approved";
    retryCount: number;
    investigationSteps: string[];
}

interface IncidentAnalysis {
    aiAnalysis: "Payment failed due to insufficient funds." | "Payment completed successfully.";
    investigationSteps: string[];
}

interface IncidentReport {
    finalReport: string;
}

export const retrievePayment: GraphNode<
    typeof PaymentIncidentState
> = (state): PaymentRetrieval => {
    console.log("Retrieving payment:", state.paymentId);

    // Temporary mock data
    const paymentStatus: "FAILED" | "SUCCESS" =
        state.paymentId === "PAY-10001"
            ? "FAILED"
            : "SUCCESS";

    return {
        paymentStatus,
        investigationSteps: ["Payment retrieved"]
        // gatewayResponse: paymentStatus === "FAILED"
        // ? "51 - Insufficient funds"
        // : "00 - Approved"
    };
};

export const checkGateway: GraphNode<typeof PaymentIncidentState> =
    (state): GatewayCheck => {
        console.log("Checking gateway response...");

        const gatewayResponse: "51 - Insufficient funds" | "00 - Approved" =
            state.paymentStatus === "FAILED"
                ? "51 - Insufficient funds"
                : "00 - Approved";

        const retryRequired = state.paymentStatus === "FAILED";
        const retryCount = retryRequired
            ? state.retryCount + 1
            : state.retryCount;
        const investigationSteps = retryRequired
            ? ["Gateway retry required", "Gateway Checked"]
            : ["Gateway Checked"];

        return {
            gatewayResponse,
            retryCount,
            investigationSteps
        };
    };

export const analyzeIncident: GraphNode<typeof PaymentIncidentState> =
    (state): IncidentAnalysis => {

    console.log("Analyzing payment incident...");

    const aiAnalysis: "Payment failed due to insufficient funds." | "Payment completed successfully." =
            state.paymentStatus === "FAILED"
                ? "Payment failed due to insufficient funds."
                : "Payment completed successfully.";

    return {
        aiAnalysis,
        investigationSteps: ["Incident analyzed"]
        };
    };


export const generateReport: GraphNode<typeof PaymentIncidentState> =
    (state): IncidentReport => {
        console.log("Generating incident report...");

    const finalReport: string = `
        Incident ID: ${state.incidentId}
        Payment ID: ${state.paymentId}
        Payment Status: ${state.paymentStatus}
        Analysis: ${state.aiAnalysis}
        Gateway Response: ${state.gatewayResponse}
        Gateway Retry Count: ${state.retryCount}
        Analysis: ${state.aiAnalysis}
        Investigation Steps:${state.investigationSteps.map((step: string) => `- ${step}`).join("\n")}
        `;

        return {finalReport};
    };