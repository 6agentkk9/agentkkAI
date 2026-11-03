import logging

logging.basicConfig(level=logging.INFO)

logging.debug("Debug message")
logging.info("Payment processing started")
logging.warning("Payment processing is taking longer than expected")
logging.error("Payment processing failed")
logging.critical("Payment service is unavailable")


# Write logs to a file
import logging
from pathlib import Path

# log_path = Path(__file__).with_name("payment.log")
log_path = Path.cwd() / "payment-reconciliation" / "payment.log"

logging.basicConfig(
    filename=log_path,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logger = logging.getLogger(__name__)

# case 1
logger.info("Payment processing started")
logger.info("Payment ID: 1001")
logger.error("Payment processing failed")

# case 2 
try:
    result = 100 / 0

except ZeroDivisionError:
    logger.exception("Payment calculation failed")


#  Full test case

import logging
from pathlib import Path

log_path = Path.cwd() / "payment-reconciliation" / "payment.log"
logging.basicConfig(
    filename=log_path,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logger = logging.getLogger(__name__)

def reconcile_payment(payment_id, amount):

    logger.info("Starting payment: %s", payment_id)

    try:
        if amount < 0:
            raise ValueError("Negative payment amount")

        logger.info(
           "Payment %s reconciled successfully for $%.2f",
            payment_id,
            amount
        )

    except ValueError:
        logger.exception(
            "Payment %s reconciliation failed for $%.2f",
            payment_id,
            amount
        )


logger.info("Reconciliation batch started")

reconcile_payment(1001, 250)
reconcile_payment(1002, -50)

logger.info("Reconciliation batch completed")