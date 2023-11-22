#Create a class called Employee with members, name, id and pf_contributions_by_month, leaves_per_month. 
#Create a method to return his total pf contribution with interest.

class Employee:
    def __init__(self, name, emp_id, pf_contributions_by_month, leaves_per_month):
        self.name = name
        self.emp_id = emp_id
        self.pf_contributions_by_month = pf_contributions_by_month
        self.leaves_per_month = leaves_per_month

    def calculate_total_pf_with_interest(self, interest_rate=0.05):
        total_pf_contributions = sum(self.pf_contributions_by_month)
        total_interest = total_pf_contributions * interest_rate
        return total_pf_contributions + total_interest

# Example usage:
employee1 = Employee("John Doe", 123, [4000, 4500, 5000], 4)

# Calculate and print the total PF contribution with interest
total_pf_with_interest = employee1.calculate_total_pf_with_interest()
print(f"Total PF Contribution with Interest for {employee1.name} (ID: {employee1.emp_id}): ${total_pf_with_interest:.2f}")
