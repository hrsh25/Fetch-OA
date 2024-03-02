from models import Receipt, Item
from point_rules import (RetailerNamePointsRule, TotalAmountPointsRule, ItemsCountPointsRule, 
                         ItemDescriptionPointsRule, PurchaseDatePointsRule, PurchaseTimePointsRule)

# Helper function to create a receipt
def create_receipt(retailer, purchaseDate, purchaseTime, items, total):
    return Receipt(retailer=retailer, purchaseDate=purchaseDate, purchaseTime=purchaseTime, items=items, total=total)

# RetailerNamePointsRule Tests
def test_retailer_name_points():
    rule = RetailerNamePointsRule()
    receipt = create_receipt("TestStore", "2022-01-01", "13:01", [Item(shortDescription="Item1", price="1.00")], "1.00")
    assert rule.calculate(receipt) == 9

# TotalAmountPointsRule Tests for round total amount
def test_total_amount_points_round():
    rule = TotalAmountPointsRule()
    receipt = create_receipt("TestStore", "2022-01-01", "13:01", [Item(shortDescription="Item1", price="1.00")], "1.00")
    assert rule.calculate(receipt) == 75  # Round total amount + 25 for being divisible by 0.25

# TotalAmountPointsRule Test for total as a multiple of 0.25
def test_total_amount_points_multiple_of_25():
    rule = TotalAmountPointsRule()
    receipt = create_receipt("TestStore", "2022-01-01", "13:01", [Item(shortDescription="Item1", price="99.75")], "99.75")
    assert rule.calculate(receipt) == 25  # Total is a multiple of 0.25

# TotalAmountPointsRule Test for total that is neither round nor a multiple of 0.25
def test_total_amount_points_neither():
    rule = TotalAmountPointsRule()
    receipt = create_receipt("TestStore", "2022-01-01", "13:01", [Item(shortDescription="Item1", price="99.99")], "99.99")
    assert rule.calculate(receipt) == 0  # Neither round nor a multiple of 0.25

# ItemsCountPointsRule Tests
def test_items_count_points():
    rule = ItemsCountPointsRule()
    items = [Item(shortDescription="Item1", price="1.00"), Item(shortDescription="Item2", price="2.00")]
    receipt = create_receipt("TestStore", "2022-01-01", "13:01", items, "3.00")
    assert rule.calculate(receipt) == 5  # 2 items should yield 5 points

# ItemDescriptionPointsRule Tests
def test_item_description_points():
    rule = ItemDescriptionPointsRule()
    items = [Item(shortDescription="Item12", price="10.00")]  # 6 characters, divisible by 3
    receipt = create_receipt("TestStore", "2022-01-01", "13:01", items, "10.00")
    assert rule.calculate(receipt) == 2  # 20% of 10.00, rounded up

# PurchaseDatePointsRule Tests
def test_purchase_date_points():
    rule = PurchaseDatePointsRule()
    receipt = create_receipt("TestStore", "2022-01-01", "13:01", [Item(shortDescription="Item1", price="1.00")], "100.00")  # An odd day
    assert rule.calculate(receipt) == 6

# PurchaseTimePointsRule Test for purchase time within bonus points hours
def test_purchase_time_points_within_range():
    rule = PurchaseTimePointsRule()
    receipt = create_receipt("TestStore", "2022-01-01", "15:00", [Item(shortDescription="Item1", price="1.00")], "1.00")  # Within bonus hours
    assert rule.calculate(receipt) == 10

# PurchaseTimePointsRule Test for purchase time at the start of bonus points hours
def test_purchase_time_points_at_start():
    rule = PurchaseTimePointsRule()
    receipt = create_receipt("TestStore", "2022-01-01", "14:00", [Item(shortDescription="Item1", price="1.00")], "1.00")  # At the start of bonus hours
    assert rule.calculate(receipt) == 10

# PurchaseTimePointsRule Test for purchase time outside bonus points hours
def test_purchase_time_points_outside_range():
    rule = PurchaseTimePointsRule()
    receipt = create_receipt("TestStore", "2022-01-01", "16:00", [Item(shortDescription="Item1", price="1.00")], "1.00")  # Outside bonus hours
    assert rule.calculate(receipt) == 0