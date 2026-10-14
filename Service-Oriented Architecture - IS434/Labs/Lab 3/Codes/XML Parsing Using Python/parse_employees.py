import xml.etree.ElementTree as ET


def parse_employees(filename):
    tree = ET.parse(filename)
    root = tree.getroot()
    employees = []
    for emp in root.findall("Employee"):
        employee = {
            "ID": emp.get("ID"),
            "Firstname": emp.find("Firstname").text,
            "Lastname": emp.find("Lastname").text,
            "Age": int(emp.find("Age").text),
            "Salary": float(emp.find("Salary").text),
        }
        employees.append(employee)
    return employees


def print_employees(employees):
    for emp in employees:
        print(f"ID: {emp['ID']}")
        print(f"Name: {emp['Firstname']} {emp['Lastname']}")
        print(f"Age: {emp['Age']}")
        print(f"Salary: {emp['Salary']}")
        print("-" * 20)


if __name__ == "__main__":
    employees = parse_employees("employees.xml")
    print_employees(employees)
