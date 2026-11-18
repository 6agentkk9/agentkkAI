from enum import Enum


class PaymentStatus(str, Enum):
    NEW = "NEW"
    FAILED = "FAILED"
    SUCCESS = "SUCCESS"
    RESOLVED = "RESOLVED"