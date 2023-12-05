from banker.data.category import PaymentType


def format_payment_type(payment_type: PaymentType) -> str:
    match payment_type:
        case PaymentType.Household:
            return "Opłaty domowe"
        case PaymentType.Recurring:
            return "Opłaty stałe"
        case PaymentType.Occasional:
            return "Opłaty okolicznościowe"
        case PaymentType.Optional:
            return "Opłaty opcjonalne"
    raise ValueError(f"Unknown payment type: {payment_type}")
