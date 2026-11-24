export function isPaymentFailed(
    status: string
): boolean {
    return status === "FAILED";
}