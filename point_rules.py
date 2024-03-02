from abc import ABC, abstractmethod
from models import Receipt
import math

class PointRule(ABC):
    """
    Abstract base class for all point calculation rules.
    """
    @abstractmethod
    def calculate(self, receipt: Receipt) -> int:
        """
        Calculates points for a receipt based on a specific rule.
        Args:
            receipt (Receipt): The receipt to calculate points for.
        Returns:
            int: The number of points calculated.
        """
        pass

class RetailerNamePointsRule(PointRule):
    """
    Calculates points based on the number of alphanumeric characters in the retailer name.
    """
    def calculate(self, receipt: Receipt) -> int:
        return len([c for c in receipt.retailer if c.isalnum()])

class TotalAmountPointsRule(PointRule):
    """
    Awards points if the total amount is a round number or a multiple of 0.25.
    """
    ROUND_TOTAL_POINTS = 50  # Points for round total amount
    MULTIPLE_OF_25_POINTS = 25  # Points for totals that are multiples of 0.25

    def calculate(self, receipt: Receipt) -> int:
        points = 0
        if float(receipt.total) % 1 == 0:
            points += self.ROUND_TOTAL_POINTS
        if float(receipt.total) % 0.25 == 0:
            points += self.MULTIPLE_OF_25_POINTS
        return points

class ItemsCountPointsRule(PointRule):
    """
    Awards points based on the number of items on the receipt.
    """
    POINTS_PER_TWO_ITEMS = 5  # Points awarded for every two items

    def calculate(self, receipt: Receipt) -> int:
        return self.POINTS_PER_TWO_ITEMS * (len(receipt.items) // 2)

class ItemDescriptionPointsRule(PointRule):
    """
    Awards points for each item whose description length is a multiple of 3.
    The points are calculated as 20% of the item's price, rounded up.
    """
    PRICE_MULTIPLIER = 0.2  # Multiplier for calculating item points

    def calculate(self, receipt: Receipt) -> int:
        points = 0
        for item in receipt.items:
            if len(item.shortDescription.strip()) % 3 == 0:
                points += math.ceil(float(item.price) * self.PRICE_MULTIPLIER)
        return points

class PurchaseDatePointsRule(PointRule):
    """
    Awards points if the purchase date is an odd day of the month.
    """
    ODD_DAY_POINTS = 6  # Points awarded for purchases made on an odd day

    def calculate(self, receipt: Receipt) -> int:
        return self.ODD_DAY_POINTS if receipt.purchaseDate.day % 2 != 0 else 0

class PurchaseTimePointsRule(PointRule):
    """
    Awards points if the purchase time is between 2:00 PM and 4:00 PM.
    """
    AFTERNOON_POINTS = 10  # Points for purchases made between 2:00 PM and 4:00 PM
    BONUS_POINT_HOUR_START = 14
    BONUS_POINT_HOUR_END = 16
    def calculate(self, receipt: Receipt) -> int:
        if self.BONUS_POINT_HOUR_START <= receipt.purchaseTime.hour < self.BONUS_POINT_HOUR_END:
            return self.AFTERNOON_POINTS
        return 0
