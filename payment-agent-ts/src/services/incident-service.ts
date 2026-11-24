import { logger } from "../config/logger.js";
import type { Incident } from "../models/incident.js";

export function logIncident(incident: Incident): void {
    logger.info(
        {
            incidentId: incident.incidentId,
            paymentId: incident.paymentId,
            errorCode: incident.errorCode,
            status: incident.status
        },
        "Payment incident received"
    );
}