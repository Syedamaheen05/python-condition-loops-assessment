# Python Fundamentals — Mini Projects

A collection of beginner-friendly Python projects developed while practicing core programming concepts.

## Projects

### 1. Student Scholarship Eligibility System

**Purpose:** Evaluate a student's scholarship eligibility using academic marks, attendance, and family income.

**Eligibility criteria**
- Academic marks must be **80% or above**.
- Attendance must be **85% or above**.
- Family income must be **Rs. 50,000 or less**.
- Students scoring **90% or above** receive a **Full Scholarship**.
- Students scoring **80%–89.99%** receive a **Partial Scholarship**.
- If any eligibility condition is not met, the program displays the relevant reason(s) for ineligibility.

**Inputs**
- Student name
- Academic marks (%)
- Attendance (%)
- Family income (Rs.)

**Output**
- Input validation messages, where applicable
- Eligibility result and scholarship category
- Scholarship evaluation report

**Concepts practiced**
- `input()` and `print()`
- Variables and data types
- Type conversion (`float`)
- `if`, `elif`, and `else`
- Logical operators (`and`, `or`)
- Input validation
- Nested conditions
- Report formatting

### 2. Pharmacy Inventory and Sales System

**Purpose:** Process medicine sales, calculate revenue, monitor remaining inventory, and identify medicines that need restocking.

**Features**
- Ask how many medicines should be processed.
- Use a `for` loop to process each medicine.
- Collect medicine name, available stock, price per unit, and quantity sold.
- Check whether the requested sales quantity is available.
- Calculate sales amount only when the sale can be completed.
- Calculate and display remaining stock after a successful sale.
- Display a low-stock warning when remaining stock is below **10 units**.
- Accumulate total pharmacy revenue.
- Count medicines requiring restocking.
- Display a final pharmacy report.

**Concepts practiced**
- `input()` and `print()`
- Variables and data types
- Type conversion (`int` and `float`)
- `for` loop and `range()`
- `if`, `elif`, and `else`
- Logical operators
- Input validation and `try/except`
- Accumulators
- Counters
- Arithmetic operations
- Formatted strings (f-strings)
- Report formatting

## Requirements

- Python 3
- A code editor or terminal (for example, Visual Studio Code)

## How to Run

1. Save each program in a separate Python file.
2. Open a terminal in the folder containing the file.
3. Run the required program:

   ```bash
   python scholarship_system.py
   ```

   or

   ```bash
   python pharmacy_system.py
   ```

   If your system uses the Python launcher, you can use `py` instead of `python`.

## Sample Run — Student Scholarship Eligibility System

```text
==== Student Scholarship System ====
Enter your name: Ayesha
Enter your academic marks (%): 85
Enter your attendance (%): 90
Enter your family income: 40000

=================================
      SCHOLARSHIP EVALUATION REPORT
=================================
Student Name: Ayesha
Academic Marks: 85.0%
Attendance: 90.0%
Family Income: Rs. 40000.0
Eligibility: Eligible
Scholarship: Partial Scholarship
```

*Sample values are illustrative. Exact output depends on the program's formatting and the entered values.*

## Sample Run — Pharmacy Inventory and Sales System

```text
===== Pharmacy Inventory System =====
How many medicines do you want to process? 2

--- Medicine 1 ---
Enter medicine name: Panadol
Enter available stock: 25
Enter price per unit: 20
Enter quantity sold: 18
Sales amount: Rs. 360.0
Remaining stock: 7
WARNING: Panadol is low in stock. Restocking is required.

--- Medicine 2 ---
Enter medicine name: Syrup
Enter available stock: 30
Enter price per unit: 100
Enter quantity sold: 10
Sales amount: Rs. 1000.0
Remaining stock: 20

=================================
       PHARMACY SALES REPORT
=================================
Total medicines processed: 2
Total pharmacy revenue: Rs. 1360.0
Medicines requiring restocking: 1
```

*Sample values are illustrative. Exact output depends on the program's formatting and the entered values.*

## Learning Note

These projects are intended for practice and assignment submission. The code uses straightforward beginner-level logic and familiar Python constructs. The next learning step is to review each program line by line, understand the reason for each condition and accumulator, and test different input cases.
