# 🏦 Loan EMI Calculator & Tracker by @mit

A professional financial tool to demystify loans. Calculate your monthly EMI and track your repayment journey with banking-grade logic.

## 🎯 What It Does

1. **Calculates EMI**: Uses the standard banking formula `[P x R x (1+R)^N]/[(1+R)^N-1]`.
2. **Tracks Payments**: Record monthly payments and watch your principal balance decrease.
3. **Amortization Preview**: See exactly how much money goes to Interest vs Principal in the early months.
4. **Portfolio Summary**: Shows the "Total Interest Payable" (the hidden cost of borrowing).

## 🚀 How to Run

```bash
# Navigate to the project directory
cd /home/john/Documents/learn/Learn_Dec_PYTHON/Basic-Projects/LoanEMICalculatorTracker

# Run the tracker
python loan_tracker.py
python3 loan_tracker.py
or
Run on VSCODE or PYCHARM
```

## ✨ Why This is "Adult-Level"

- **Financial Reality**: It reveals that for long-term loans, you often pay more in interest than the loan amount itself.
- **Precision**: Handles currency formatting (₹) and decimal precision like real banking apps.
- **Logic**: Implements the actual math used by banks, not just a simple estimate.

## 💡 Sample Usage

```
🏦  LOAN EMI CALCULATOR & TRACKER
==================================================
1. 🆕 Setup New Loan
2. 📊 View Portfolio Summary
3. 💸 Make EMI Payment
...
==================================================

Enter Principal Amount (₹): 500000
Enter Annual Interest Rate (%): 10
Enter Tenure (Years): 5

✅ LOAN ACTIVATED SUCCESSFULLY!
   Calculated EMI: ₹10,623.52 / month
```

## 📉 Amortization Example

```
Month  EMI          Interest     Principal    Balance
------------------------------------------------------------
1      10623        4166         6456         493543
2      10623        4112         6510         487032
3      10623        4058         6564         480467
------------------------------------------------------------
NOTE: Notice how Interest decreases and Principal increases!
```

## 🔧 Technical Details

- **Math**: Uses power operator `**` for compound interest calculations.
- **Logic**: Separates Interest and Principal components for every payment.
- **State Management**: Keeps track of running balance using a dictionary.

---
**Perfect for**: Learning how money works while learning Python code!

**Examples :**
**Used Try Except :** 
==================================================
🏦  LOAN EMI CALCULATOR & TRACKER
==================================================
1. 🆕 Setup New Loan
2. 📊 View Portfolio Summary
3. 💸 Make EMI Payment
4. 📉 Amortization Preview
5. 🚪 Exit
==================================================
Enter Choice (1-5): 1

--- 🏦 NEW LOAN SETUP ---
**#Entered strings and see How it works**
Enter Principal Amount (₹): dsds 
❌ Invalid input! Please enter numbers only.


==================================================
🏦  LOAN EMI CALCULATOR & TRACKER
==================================================
1. 🆕 Setup New Loan
2. 📊 View Portfolio Summary
3. 💸 Make EMI Payment
4. 📉 Amortization Preview
5. 🚪 Exit
==================================================
Enter Choice (1-5): 

**Learn Code wid @mit for**: Simplicity and depth!