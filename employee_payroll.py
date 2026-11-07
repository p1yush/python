employees = [
    {"name": "Piyush", "salary": 60000, "active": True},
    {"name": "Rahul", "salary": 45000, "active": True},
    {"name": "Aman", "salary": 70000, "active": False},
    {"name": "Priya", "salary": 55000, "active": True},
    {"name": "Neha", "salary": 40000, "active": True}
]

total_payroll = 0
active_employees = 0

print("========== EMPLOYEE PAYROLL ==========")

for employee in employees:

    if not employee["active"]:
        continue

    name = employee["name"]
    salary = employee["salary"]

    annual_salary = salary * 12

    if salary > 50000:
        bonus = annual_salary * 0.10
    else:
        bonus = 0

    total_compensation = annual_salary + bonus

    total_payroll += salary
    active_employees += 1

    print(f"\nEmployee: {name}")
    print(f"Monthly Salary: ₹{salary}")
    print(f"Annual Salary: ₹{annual_salary}")
    print(f"Bonus: ₹{bonus:.2f}")
    print(f"Total Compensation: ₹{total_compensation:.2f}")

print("\n========== SUMMARY ==========")

print(f"Active Employees: {active_employees}")
print(f"Total Monthly Payroll: ₹{total_payroll}")

print("============================")