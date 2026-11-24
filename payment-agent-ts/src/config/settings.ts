const env = (globalThis as typeof globalThis & {
    process?: { env?: Record<string, string | undefined> };
}).process?.env ?? {};

function requiredEnv(name: string): string {
    const value = env[name];

    if (!value) {
        throw new Error(
            `Missing required environment variable: ${name}`
        );
    }

    return value;
}

export const settings = {
    appName: env.APP_NAME ?? "PaymentIncidentAgent",

    nodeEnv: env.NODE_ENV ?? "development",

    paymentApiUrl: requiredEnv("PAYMENT_API_URL"),

    logLevel: env.LOG_LEVEL ?? "info"
};