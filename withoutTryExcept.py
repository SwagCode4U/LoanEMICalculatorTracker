"""
🏦 BASIC LOAN EMI CALCULATOR & TRACKER by @mit
=====================================
Learning Version (Crash Allowed)

Purpose:
- Practice variables, input, conditions, functions, dictionaries
- Understand financial logic
- Build confidence before Advanced Python

NOTE:
This version may crash on wrong input.
We will improve it later using try/except and __main__.
"""

# Import datetime (used later when we learn files / logs)
from datetime import datetime

# ============================================================================
# GLOBAL DATA STRUCTURE
# ============================================================================

loan_data = {
    'active': False,
    'principal': 0.0,
    'rate_annual': 0.0,
    'tenure_months': 0,
    'emi': 0.0,
    'balance_remaining': 0.0,
    'payments_made': 0,
    'total_paid': 0.0
}

# ============================================================================
# FINANCIAL LOGIC FUNCTIONS
# ============================================================================

def calculate_emi(principal, rate_annual, tenure_years):
    """
    EMI Formula Logic:
    EMI = [P x R x (1+R)^N] / [(1+R)^N - 1]
    """
    if rate_annual == 0:
        return principal / (tenure_years * 12)

    monthly_rate = rate_annual / 12 / 100       # simple math to get the ROI monthly
    months = tenure_years * 12          # converting years to month

    numerator = principal * monthly_rate * ((1 + monthly_rate) ** months)
    denominator = ((1 + monthly_rate) ** months) - 1

    return numerator / denominator

# Setup the input of user to show clear structure
def setup_loan():
    print("\n--- 🏦 NEW LOAN SETUP ---")

    if loan_data['active']:
        choice = input("Loan already exists. Overwrite? (yes/no): ")
        if choice != 'yes':
            return

    p = float(input("Enter Principal Amount (₹): "))
    r = float(input("Enter Annual Interest Rate (%): "))
    t = float(input("Enter Tenure (Years): "))

    if p <= 0 or r < 0 or t <= 0:
        print("❌ Invalid values! Loan not created.")
        return

    emi = calculate_emi(p, r, t)
        # Adding the loan_data details
    loan_data['active'] = True
    loan_data['principal'] = p
    loan_data['rate_annual'] = r
    loan_data['tenure_months'] = int(t * 12)
    loan_data['emi'] = emi
    loan_data['balance_remaining'] = p
    loan_data['payments_made'] = 0
    loan_data['total_paid'] = 0.0       # Must keep in float

    print("\n✅ Loan Created Successfully!")
    print(f"Monthly EMI: ₹{emi:,.2f}")
    # :,.2f keeps the figure in 2 digits and also keeps the number look better with the (,)

# ============================================================================
# DISPLAY & TRACKING FUNCTIONS
# ============================================================================

def view_summary():
    print("\n" + "=" * 60)
    print("📊 LOAN SUMMARY".center(60))
    print("=" * 60)

    if not loan_data['active']:
        print("No active loan found.")
        return

    total_payable = loan_data['emi'] * loan_data['tenure_months']
    total_interest = total_payable - loan_data['principal']
    progress = (loan_data['payments_made'] / loan_data['tenure_months']) * 100

    print(f"Principal        : ₹{loan_data['principal']:,.2f}")
    print(f"Interest Rate    : {loan_data['rate_annual']}%")
    print(f"Tenure           : {loan_data['tenure_months']} months")
    print("-" * 60)
    print(f"Monthly EMI      : ₹{loan_data['emi']:,.2f}")
    print(f"Total Interest   : ₹{total_interest:,.2f}")
    print(f"Total Payable    : ₹{total_payable:,.2f}")
    print("-" * 60)
    print(f"Paid EMIs        : {loan_data['payments_made']}")
    print(f"Balance Left     : ₹{loan_data['balance_remaining']:,.2f}")
    print(f"Progress         : {progress:.1f}%")

# make_payment - Structure input and also with conditions
def make_payment():
    print("\n--- 💸 EMI PAYMENT ---")

    if not loan_data['active']:
        print("No active loan.")
        return

    if loan_data['balance_remaining'] <= 0:
        print("Loan already cleared 🎉")
        return

    print(f"EMI Amount: ₹{loan_data['emi']:,.2f}")
    confirm = input("Pay EMI? (yes/no): ")

    if confirm != 'yes':            # if not yes then: cancel
        print("Payment cancelled.")
        return

    monthly_rate = loan_data['rate_annual'] / 12 / 100
    interest = loan_data['balance_remaining'] * monthly_rate
    principal = loan_data['emi'] - interest

    loan_data['balance_remaining'] -= principal
    loan_data['payments_made'] += 1
    loan_data['total_paid'] += loan_data['emi']

    if loan_data['balance_remaining'] < 0:
        loan_data['balance_remaining'] = 0

    print("✅ Payment Done!")
    print(f"Interest Paid  : ₹{interest:,.2f}")
    print(f"Principal Paid : ₹{principal:,.2f}")
    print(f"Balance Left   : ₹{loan_data['balance_remaining']:,.2f}")

# Amortization preview function

def view_amortization_preview():
    print("\n--- 📉 AMORTIZATION PREVIEW (First 5 Months) ---")

    if not loan_data['active']:
        print("No active loan.")
        return

    balance = loan_data['principal']
    monthly_rate = loan_data['rate_annual'] / 12 / 100

    print("Month | EMI | Interest | Principal | Balance")
    print("-" * 55)
    # for loop to get the range and also the int principal and balance due
    for month in range(1, 6):
        interest = balance * monthly_rate
        principal = loan_data['emi'] - interest
        balance -= principal        # balance due

        print(month, "|",
              int(loan_data['emi']), "|",
              int(interest), "|",
              int(principal), "|",
              int(balance))

# ============================================================================
# MAIN PROGRAM (DIRECT EXECUTION)
# ============================================================================

def main():
    while True:
        print("\n" + "=" * 50)
        print("🏦 LOAN EMI CALCULATOR")
        print("=" * 50)
        print("1. Setup Loan")
        print("2. View Summary")
        print("3. Pay EMI")
        print("4. Amortization Preview")
        print("5. Exit")

        choice = input("Enter choice (1-5): ")

        if choice == '1':
            setup_loan()
        elif choice == '2':
            view_summary()
        elif choice == '3':
            make_payment()
        elif choice == '4':
            view_amortization_preview()
        elif choice == '5':
            print("Goodbye 👋")
            break
        else:
            print("Invalid choice!")

# Direct call (no __main__ yet)
main()

# this do not have the dandur and even the try except which leads user bad input halts the Program with error and stops.
# See the outher version which will work far better and also learn the need of try and except early to use...

# Thanks 🙏 @mit
