import {
    StateGraph,
    START,
    END
} from "@langchain/langgraph";

import { PaymentIncidentState } from "./state.js";

import {
    retrievePayment,
    checkGateway,
    analyzeIncident,
    generateReport
} from "./nodes.js";


export const paymentIncidentGraph =
    new StateGraph(PaymentIncidentState)

        .addNode("retrievePayment", retrievePayment)
        .addNode("checkGateway", checkGateway)
        .addNode("analyzeIncident", analyzeIncident)
        .addNode("generateReport", generateReport)

        .addEdge(START, "retrievePayment")
        .addEdge("retrievePayment", "checkGateway")
        .addEdge("checkGateway", "analyzeIncident")
        .addEdge("analyzeIncident", "generateReport")
        .addEdge("generateReport", END)

        .compile();