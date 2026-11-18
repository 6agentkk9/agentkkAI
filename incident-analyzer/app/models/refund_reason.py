from enum import Enum


class RefundReason(str, Enum):
    DUPLICATE = "DUPLICATE"
    CUSTOMER_REQUEST = "CUSTOMER_REQUEST"
    PROCESSING_ERROR = "PROCESSING_ERROR"