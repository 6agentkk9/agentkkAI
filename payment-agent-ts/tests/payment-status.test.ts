import { describe, it } from "node:test";
import assert from "node:assert/strict";

import { isPaymentFailed } from "../src/services/payment-status.ts";

describe("Payment status", () => {

    it("should identify failed payments", () => {

        const result = isPaymentFailed("FAILED");

        assert.equal(result, true);
    });

    it("should identify successful payments", () => {

        const result = isPaymentFailed("SUCCESS");

        assert.equal(result, false);
    });
});