from banker.data.category import PaymentType


def parse_payment_type(payment_type: str) -> PaymentType | None:
    match payment_type:
        case 'household':
            return PaymentType.Household
        case 'recurring':
            return PaymentType.Recurring
        case 'occasional':
            return PaymentType.Occasional
        case 'optional':
            return PaymentType.Optional
    return None
