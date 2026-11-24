import { settings } from "./settings.js";

type LogMethod = (...args: unknown[]) => void;

const levels = ["trace", "debug", "info", "warn", "error", "fatal"] as const;
type LogLevel = (typeof levels)[number];

const configuredLevel = settings.logLevel as LogLevel;
const configuredLevelIndex = levels.includes(configuredLevel)
    ? levels.indexOf(configuredLevel)
    : levels.indexOf("info");

const createLogMethod = (level: LogLevel): LogMethod => (...args: unknown[]) => {
    if (levels.indexOf(level) < configuredLevelIndex) {
        return;
    }

    const timestamp = new Date().toISOString();
    const consoleMethod = level === "fatal" || level === "error"
        ? console.error
        : level === "warn"
            ? console.warn
            : level === "debug" || level === "trace"
                ? console.debug
                : console.info;

    consoleMethod({ application: settings.appName, level, time: timestamp, args });
};

export const logger = {
    trace: createLogMethod("trace"),
    debug: createLogMethod("debug"),
    info: createLogMethod("info"),
    warn: createLogMethod("warn"),
    error: createLogMethod("error"),
    fatal: createLogMethod("fatal"),
    child: () => logger
};