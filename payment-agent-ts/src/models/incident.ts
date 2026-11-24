export interface Incident {
    incidentId: string;
    paymentId: string;
    errorCode: string;
    description: string;
    status: "OPEN" | "INVESTIGATING" | "RESOLVED";
}