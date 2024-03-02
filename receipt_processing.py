from models import Receipt
from point_rules import (
    RetailerNamePointsRule,
    TotalAmountPointsRule,
    ItemsCountPointsRule,
    ItemDescriptionPointsRule,
    PurchaseDatePointsRule,
    PurchaseTimePointsRule
)

class ReceiptProcessor:
    """
    Orchestrates the calculation of points for a receipt using a set of defined rules.
    """
    def __init__(self):
        # Initializes the list of rules to be applied for point calculation.
        self.rules = [
            RetailerNamePointsRule(),
            TotalAmountPointsRule(),
            ItemsCountPointsRule(),
            ItemDescriptionPointsRule(),
            PurchaseDatePointsRule(),
            PurchaseTimePointsRule()
        ]

    def calculate_points(self, receipt: Receipt) -> int:
        """
        Calculates the total points for a receipt by applying all defined rules.
        Args:
            receipt (Receipt): The receipt to calculate points for.
        Returns:
            int: The total number of points awarded for the receipt.
        """
        # Applies each rule in the list and sums up the points awarded.
        return sum(rule.calculate(receipt) for rule in self.rules)
