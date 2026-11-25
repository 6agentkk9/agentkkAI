import { StateSchema, ReducedValue } from "@langchain/langgraph";
import { z } from "zod/v4";

export const PaymentIncidentState = new StateSchema({
    incidentId: z.string(),
    paymentId: z.string(),

    paymentStatus: z.string().default("UNKNOWN"),
    gatewayResponse: z.string().default(""),

    aiAnalysis: z.string().default(""),
    finalReport: z.string().default(""),

    retryCount : z.number().default(0),
    investigationSteps: new ReducedValue(
        z.array(z.string()).default([]), { reducer: (left, right) => [...left, ...right] }
    )
});