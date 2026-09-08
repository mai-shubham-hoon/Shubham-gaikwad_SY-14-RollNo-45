# Decorator for Report Header and Footer
def report_formatter(func):
    def wrapper(*args, **kwargs):
        print("=" * 50)
        print(" DYNAMIC REPORT GENERATOR")
        print("=" * 50)

        func(*args, **kwargs)

        print("=" * 50)
        print("           END OF REPORT")
        print("=" * 50)
    return wrapper


# Report Class
class Report:
    template = "Default Report"

    # Constructor
    def __init__(self, title):
        self.title = title
        self.contents = []

    # Class Method to Set Report Template
    @classmethod
    def set_template(cls, template_name):
        cls.template = template_name

    # Add Content
    def add_content(self, heading, data):
        self.contents.append((heading, data))

    # Magic Method (__len__)
    def __len__(self):
        return len(self.contents)

    # Magic Method (__str__)
    def __str__(self):
        report = f"\nTemplate : {Report.template}\n"
        report += f"Report Title : {self.title}\n"
        report += "-" * 40 + "\n"

        for heading, data in self.contents:
            report += f"{heading} : {data}\n"

        report += "-" * 40
        return report


# Report Generator Class
class ReportGenerator:

    @report_formatter
    def generate(self, report):
        print(report)
        print(f"\nTotal Sections: {len(report)}")


# Main Program
# Set Template
Report.set_template("Student Performance Report")

# Create Report Object
report1 = Report("Semester End Examination")

# Add Report Sections
report1.add_content("Student Name", "Rahul Sharma")
report1.add_content("Roll Number", "101")
report1.add_content("Department", "Computer Engineering")
report1.add_content("Percentage", "88.5%")
report1.add_content("Grade", "A")

# Generate Report
generator = ReportGenerator()
generator.generate(report1)
