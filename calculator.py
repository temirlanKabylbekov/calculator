import bisect
from collections import OrderedDict

REGION_TO_TAX_MAP = {"UT": 6.85, "NV": 8, "TX": 6.25, "AL": 4, "CA": 8.25}

MIN_PRICE_FOR_MIN_DISCOUNT = 1000
MIN_PRICE_FOR_MAX_DISCOUNT = 50000

PRICE_TO_DISCOUNT_MAP = OrderedDict(
    {
        MIN_PRICE_FOR_MIN_DISCOUNT: 3,
        5000: 5,
        7000: 7,
        10000: 10,
        MIN_PRICE_FOR_MAX_DISCOUNT: 15,
    }
)

REFERENCE_PRICES = list(PRICE_TO_DISCOUNT_MAP.keys())


class InvalidCalculatorParamsError(Exception):
    pass


def calculate(price: float, region: str) -> float:
    """Расчет цены товара с учетом прогрессивной скидки и налога на штат

    Сложность алгоритма - O(logN), Дополнительная память - O(1)

    """
    if price < 0 or REGION_TO_TAX_MAP.get(region) is None:
        raise InvalidCalculatorParamsError()

    if price < MIN_PRICE_FOR_MIN_DISCOUNT:
        discount = 0
    elif price >= MIN_PRICE_FOR_MAX_DISCOUNT:
        discount = PRICE_TO_DISCOUNT_MAP[MIN_PRICE_FOR_MAX_DISCOUNT]
    else:
        idx = bisect.bisect_right(REFERENCE_PRICES, price)
        discount = PRICE_TO_DISCOUNT_MAP[REFERENCE_PRICES[idx - 1]]

    price_with_discount = price * (100 - discount) / 100
    price_with_tax = price_with_discount * (100 + REGION_TO_TAX_MAP[region]) / 100

    return price_with_tax
