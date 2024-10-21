# Darlene Lopez
# CIS 131
# This program uses an Employee class hierarchy that formats and prints all relevant employee information and read only.

from abc import ABC, abstractmethod

# Abstract class Employee
class Employee(ABC):
    def __init__(self, first_name, last_name, social_security_number):
        self._first_name = first_name
        self._last_name = last_name
        self._social_security_number = social_security_number

    # Read-only properties for first_name, last_name, and social_security_number
    @property
    def first_name(self):
        return self._first_name

    @property
    def last_name(self):
        return self._last_name

    @property
    def social_security_number(self):
        return self._social_security_number

    # Abstract method earnings, must be overridden in derived classes
    @abstractmethod
    def earnings(self):
        raise NotImplementedError("Subclasses must implement the earnings method.")

    # __repr__ method to return string containing employee details
    def __repr__(self):
        return (f"Employee: {self.first_name} {self.last_name}, "
                f"SSN: {self.social_security_number}")


# Subclass SalariedEmployee inheriting from Employee
class SalariedEmployee(Employee):
    def __init__(self, first_name, last_name, social_security_number, weekly_salary):
        super().__init__(first_name, last_name, social_security_number)
        self.weekly_salary = weekly_salary

    # Read-write property for weekly_salary with a non-negative constraint
    @property
    def weekly_salary(self):
        return self._weekly_salary

    @weekly_salary.setter
    def weekly_salary(self, salary):
        if salary < 0:
            raise ValueError("Weekly salary must be non-negative.")
        self._weekly_salary = salary

    # Override earnings method
    def earnings(self):
        return self.weekly_salary

    # Override __repr__ method
    def __repr__(self):
        return (f"SalariedEmployee: {self.first_name} {self.last_name}, "
                f"SSN: {self.social_security_number}, "
                f"Weekly Salary: ${self.weekly_salary:,.2f}")


# Subclass HourlyEmployee inheriting from Employee
class HourlyEmployee(Employee):
    def __init__(self, first_name, last_name, social_security_number, hourly_wage, hours_worked):
        super().__init__(first_name, last_name, social_security_number)
        self.hourly_wage = hourly_wage
        self.hours_worked = hours_worked

    # Read-write property for hourly_wage with a non-negative constraint
    @property
    def hourly_wage(self):
        return self._hourly_wage

    @hourly_wage.setter
    def hourly_wage(self, wage):
        if wage < 0:
            raise ValueError("Hourly wage must be non-negative.")
        self._hourly_wage = wage

    # Read-write property for hours_worked with a constraint (0-168 hours)
    @property
    def hours_worked(self):
        return self._hours_worked

    @hours_worked.setter
    def hours_worked(self, hours):
        if not (0 <= hours <= 168):
            raise ValueError("Hours worked must be between 0 and 168.")
        self._hours_worked = hours

    # Override earnings method
    def earnings(self):
        if self.hours_worked <= 50:
            return self.hourly_wage * self.hours_worked
        else:
            overtime_hours = self.hours_worked - 50
            overtime_pay = overtime_hours * (1.5 * self.hourly_wage)
            regular_pay = 50 * self.hourly_wage
            return regular_pay + overtime_pay

    # Override __repr__ method
    def __repr__(self):
        return (f"HourlyEmployee: {self.first_name} {self.last_name}, "
                f"SSN: {self.social_security_number}, "
                f"Hourly Wage: ${self.hourly_wage:,.2f}, "
                f"Hours Worked: {self.hours_worked}, "
                f"Earnings: ${self.earnings():,.2f}")


# Example usage
salaried_employee = SalariedEmployee("Bober", "Beaver", "555-55-5555", 1500)
hourly_employee = HourlyEmployee("Banana", "Pudding", "333-33-3333", 30, 36)

print(salaried_employee)
print(hourly_employee)
