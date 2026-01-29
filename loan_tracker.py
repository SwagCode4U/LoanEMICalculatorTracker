"""
🏦 PROFESSIONAL LOAN EMI CALCULATOR & TRACKER by @mit
============================================
A financial tool to calculate Equal Monthly Installments (EMI),
track repayments, and visualize interest costs.

Formula: EMI = [P x R x (1+R)^N] / [(1+R)^N-1]
Where:
P = Principal Amount
R = Monthly Interest Rate (Annual Rate / 12 / 100)
N = Tenure in Months

Author: Coders Jaunt - @mit
Purpose: Teaching financial math and logic in Python

“Practice mein crash allowed
Project mein crash unacceptable”

"""

# Import datetime to simulate payment dates (optional but professional)
from datetime import datetime

# ============================================================================
# GLOBAL DATA STRUCTURES
# ============================================================================

# Loan Details Dictionary
# Stores all information about the current active loan
loan_data = {
    'active': False,          # Is a loan currently active?
    'principal': 0.0,         # Origial loan amount
    'rate_annual': 0.0,       # Annual interest rate in %
    'tenure_months': 0,       # Total duration
    'emi': 0.0,               # Calculated monthly payment
    'balance_remaining': 0.0, # Amount left to pay
    'payments_made': 0,       # Number of EMIs paid
    'total_paid': 0.0         # Total money paid so far
}

# ============================================================================
# FINANCIAL LOGIC FUNCTIONS
# ============================================================================

def calculate_emi(principal, rate_annual, tenure_years):
    """
    Core mathematical engine for EMI calculation.
    
    Logic:
    1. Convert Rate to Monthly (R = Annual / 12 / 100)
    2. Convert Tenure to Months (N = Years * 12)
    3. Apply Formula
    """
    # Defensive programming: Division by zero check
    if rate_annual == 0:
        return principal / (tenure_years * 12)
        
    monthly_rate = rate_annual / 12 / 100   # calculations for monthly roi
    num_months = tenure_years * 12          # input in years so converting monthly well
    
    # Formula broken down for clarity
    numerator = principal * monthly_rate * ((1 + monthly_rate) ** num_months)   # Calculation of numerator for formula using BODMAS
    denominator = ((1 + monthly_rate) ** num_months) - 1
    
    emi = numerator / denominator
    return emi

# ============================================================================
# LOAN SETUP FUNCTIONS
# ============================================================================
def setup_loan():
    """Input loan details and activate the loan."""
    print("\n--- 🏦 NEW LOAN SETUP ---")
    
    if loan_data['active']:
        print("⚠️  You already have an active loan!")
        choice = input("Overwrite current loan? (yes/no): ").lower()
        if choice != 'yes':
            return
# Input Loan Details also used try and except block to handle invalid inputs
    try:
        p = float(input("Enter Principal Amount (₹): "))
        r = float(input("Enter Annual Interest Rate (%): "))
        t = float(input("Enter Tenure (Years): "))
        
        if p <= 0 or r < 0 or t <= 0:
            print("❌ Invalid input! Values must be positive.")
            return

        # Perform Calculation of EMI
        emi = calculate_emi(p, r, t)
        
        # Save to Global State
        loan_data['active'] = True
        loan_data['principal'] = p
        loan_data['rate_annual'] = r
        loan_data['tenure_months'] = int(t * 12)
        loan_data['emi'] = emi
        loan_data['balance_remaining'] = p
        loan_data['payments_made'] = 0
        loan_data['total_paid'] = 0.0
        
        print("\n✅ LOAN ACTIVATED SUCCESSFULLY!")
        print(f"   Calculated EMI: ₹{emi:,.2f} / month")
        
    except ValueError:
        print("❌ Invalid input! Please enter numbers only.")

# ============================================================================
# TRACKING & DISPLAY FUNCTIONS
# ============================================================================

def view_summary():
    """Display comprehensive loan details with professional formatting."""
    print("\n" + "="*60)
    print(f"{'📊 LOAN PORTFOLIO SUMMARY':^60}")
    print("="*60)
    
    if not loan_data['active']:
        print("📭 No active loan found. Please setup a loan first.")
        return

    # Calculate Summaries
    total_payable = loan_data['emi'] * loan_data['tenure_months']
    total_interest = total_payable - loan_data['principal']
    
    # Progress Calculation of loan repayment in percentage
    progress_pct = (loan_data['payments_made'] / loan_data['tenure_months']) * 100  # Formula for progress in percentage so that 0.25 = 25%
    
    print(f"{'Principal Amount':<25} : ₹{loan_data['principal']:,.2f}")
    print(f"{'Interest Rate':<25} : {loan_data['rate_annual']}%")
    print(f"{'Tenure':<25} : {loan_data['tenure_months']} Months")
    print("-" * 60)
    print(f"{'MONTHLY EMI':<25} : ₹{loan_data['emi']:,.2f}")
    print("-" * 60)
    print(f"{'Total Interest Payable':<25} : ₹{total_interest:,.2f}")
    print(f"{'Total Cost of Loan':<25} : ₹{total_payable:,.2f}")
    print("=" * 60)
    
    # Current Status Display with progress bar
    print(f"\n--- 📅 CURRENT STATUS ---")
    print(f"Payments Made      : {loan_data['payments_made']} / {loan_data['tenure_months']}")
    print(f"Balance Remaining  : ₹{loan_data['balance_remaining']:,.2f}")
    
    # Visual Progress Bar
    bar_length = 20
    filled_length = int(bar_length * progress_pct // 100)
    bar = '█' * filled_length + '░' * (bar_length - filled_length)
    print(f"Progress           : |{bar}| {progress_pct:.1f}%")

# ============================================================================
# PAYMENT SIMULATION FUNCTIONS
# ============================================================================
def make_payment():
    """Simulate making a monthly EMI payment."""
    print("\n--- 💸 MAKE PAYMENT ---")
    
    if not loan_data['active']:
        print("❌ No active loan to pay for.")
        return
        
    if loan_data['balance_remaining'] <= 1: # Float precision buffer
        print("✅ Loan is already fully paid off! 🎉")
        return

    print(f"EMI Due: ₹{loan_data['emi']:,.2f}")
    confirm = input("Confirm payment? (yes/no): ").lower()
    
    if confirm == 'yes':
        # Logic: 
        # In a real loan, part of EMI goes to Interest, part to Principal.
        # Interest for this month = Balance * (AnnualRate / 1200)
        # Principal Component = EMI - Interest
        
        monthly_r = loan_data['rate_annual'] / 12 / 100
        interest_component = loan_data['balance_remaining'] * monthly_r
        principal_component = loan_data['emi'] - interest_component
        
        # Update Balances
        loan_data['balance_remaining'] -= principal_component
        loan_data['payments_made'] += 1
        loan_data['total_paid'] += loan_data['emi']
        
        # Ensure balance doesn't go below zero (due to rounding)
        if loan_data['balance_remaining'] < 0:
            loan_data['balance_remaining'] = 0
            
        print("\n✅ Payment Successful!")
        print(f"   Interest Paid  : ₹{interest_component:,.2f}")
        print(f"   Principal Paid : ₹{principal_component:,.2f}")
        print(f"   New Balance    : ₹{loan_data['balance_remaining']:,.2f}")
    else:
        print("❌ Payment cancelled.")

# ============================================================================
# AMORTIZATION PREVIEW FUNCTION
# ============================================================================
def view_amortization_preview():
    """
    Show first year amortization schedule.
    Demonstrates how interest is heavy in the beginning.
    """
    print("\n--- 📉 AMORTIZATION PREVIEW (First 5 Months) ---")
    if not loan_data['active']:     # No active loan check then return - No Loan
        print("❌ No active loan.")
        return
        
    balance = loan_data['principal']
    monthly_r = loan_data['rate_annual'] / 12 / 100
    
    print(f"{'Month':<6} {'EMI':<12} {'Interest':<12} {'Principal':<12} {'Balance'}")
    print("-" * 60)
    
    for i in range(1, 6):
        interest = balance * monthly_r  # Interest for the month
        principal = loan_data['emi'] - interest # Principal comp of EMI
        balance -= principal
        
        print(f"{i:<6} {int(loan_data['emi']):<12} {int(interest):<12} {int(principal):<12} {int(balance)}")
        
    print("-" * 60)
    print("NOTE: Notice how Interest decreases and Principal increases!")

# ============================================================================
# MAIN PROGRAM
# ============================================================================

def main():
    while True:
        print("\n" + "="*50)
        print("🏦  LOAN EMI CALCULATOR & TRACKER")
        print("="*50)
        print("1. 🆕 Setup New Loan")
        print("2. 📊 View Portfolio Summary")
        print("3. 💸 Make EMI Payment")
        print("4. 📉 Amortization Preview")    
        print("5. 🚪 Exit")
        print("="*50)
        
        choice = input("Enter Choice (1-5): ").strip()
        
        if choice == '1':
            setup_loan()
        elif choice == '2':
            view_summary()
        elif choice == '3':
            make_payment()
        elif choice == '4':
            view_amortization_preview()
        elif choice == '5':
            print("\n👋 Stay financially savvy! Exiting...")
            break
        else:
            print("❌ Invalid Choice!")


# Program Entry Point - with standard Python convention - Dunder Main
if __name__ == "__main__":
    main()
