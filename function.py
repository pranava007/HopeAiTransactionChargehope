def calculate_fee_and_check_equality(hope_fee_amount, transaction_percentage):
    """
    This function calculates:
    - The total request amount
    - The transaction charge amount
    - The final amount after transaction deduction
    - Validates if the final amount matches the expected fee amount.
    """
    
    # Calculate the total request amount before transaction deduction
    request_Amount = round((hope_fee_amount * 100) / (100 - transaction_percentage))
    
    # Calculate the transaction charge
    trans_Amount = round(request_Amount * (transaction_percentage / 100))
    
    # Calculate the final amount after the transaction charge is deducted
    original_fee_Amount = request_Amount - trans_Amount

    # Validate if the computed fee matches the expected value
    if hope_fee_amount == original_fee_Amount:
        return request_Amount, trans_Amount, original_fee_Amount, "Equal"
    else:
        return request_Amount, trans_Amount, original_fee_Amount, "Not Equal"
