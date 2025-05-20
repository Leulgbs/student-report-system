#!/usr/bin/env python3

class Student:
    def __init__(self, name, student_id, advanced_prog, web_design, ui_design, systems_eng, azure_integration):
        self.name = name
        self.student_id = student_id
        self.advanced_prog = advanced_prog
        self.web_design = web_design
        self.ui_design = ui_design
        self.systems_eng = systems_eng
        self.azure_integration = azure_integration
        self.average = self._calculate_average()
        self.grade, self.grade_points = self._calculate_grade()
        self.status = self._calculate_status()
        self.performance_trend = self._calculate_performance_trend()
        self.category = self._determine_category()

    def _calculate_average(self):
        marks = [
            self.advanced_prog,
            self.web_design,
            self.ui_design,
            self.systems_eng,
            self.azure_integration
        ]
        return sum(marks) / len(marks)

    def _calculate_grade(self):
        if self.average >= 91:
            return 'A', 5.0
        elif self.average >= 81:
            return 'B+', 4.5
        elif self.average >= 71:
            return 'B', 4.0
        elif self.average >= 61:
            return 'C+', 3.5
        elif self.average >= 51:
            return 'C', 3.0
        else:
            return 'F', 2.0

    def _calculate_status(self):
        if self.average >= 51:  # Updated to match new passing grade
            return "Passing"
        else:
            return "At Risk"

    def _calculate_performance_trend(self):
        marks = [
            self.advanced_prog,
            self.web_design,
            self.ui_design,
            self.systems_eng,
            self.azure_integration
        ]
        if all(mark >= 91 for mark in marks):
            return "Excellent"
        elif all(mark >= 81 for mark in marks):
            return "Very Good"
        elif all(mark >= 71 for mark in marks):
            return "Good"
        elif all(mark >= 51 for mark in marks):
            return "Average"
        else:
            return "Needs Improvement"

    def _determine_category(self):
        if self.average >= 85 and all(mark >= 80 for mark in [self.advanced_prog, self.web_design, 
                                                             self.ui_design, self.systems_eng, 
                                                             self.azure_integration]):
            return "High Achiever"
        elif self.average >= 70 and all(mark >= 60 for mark in [self.advanced_prog, self.web_design, 
                                                               self.ui_design, self.systems_eng, 
                                                               self.azure_integration]):
            return "Consistent Performer"
        elif self.average >= 60 and all(mark >= 50 for mark in [self.advanced_prog, self.web_design, 
                                                               self.ui_design, self.systems_eng, 
                                                               self.azure_integration]):
            return "Average"
        elif self.average < 60 or any(mark < 50 for mark in [self.advanced_prog, self.web_design, 
                                                            self.ui_design, self.systems_eng, 
                                                            self.azure_integration]):
            return "Needs Support"
        else:
            return "Under Review"

    def get_subject_performance(self):
        return {
            "Advanced Programming": self.advanced_prog,
            "Web Applications Design": self.web_design,
            "UI Design": self.ui_design,
            "Systems Engineering": self.systems_eng,
            "Azure Integration": self.azure_integration
        }

    def to_dict(self):
        return {
            'ID': self.student_id,
            'Name': self.name,
            'Advanced Programming': self.advanced_prog,
            'Web Design': self.web_design,
            'UI Design': self.ui_design,
            'Systems Engineering': self.systems_eng,
            'Azure Integration': self.azure_integration,
            'Average': round(self.average, 1),
            'Grade': self.grade,
            'Grade Points': self.grade_points,
            'Status': self.status,
            'Performance': self.performance_trend,
            'Category': self.category
        }

class StudentReportSystem:
    def __init__(self):
        self.students = {}
        self.categories = {
            "High Achiever": {
                "description": "Students with excellent performance across all subjects",
                "criteria": "Average ≥ 85% and all subjects ≥ 80%",
                "color": "#27ae60"  # Green
            },
            "Consistent Performer": {
                "description": "Students with good performance across all subjects",
                "criteria": "Average ≥ 70% and all subjects ≥ 60%",
                "color": "#2980b9"  # Blue
            },
            "Average": {
                "description": "Students with satisfactory performance",
                "criteria": "Average ≥ 60% and all subjects ≥ 50%",
                "color": "#f39c12"  # Orange
            },
            "Needs Support": {
                "description": "Students requiring additional support",
                "criteria": "Average < 60% or any subject < 50%",
                "color": "#e74c3c"  # Red
            },
            "Under Review": {
                "description": "Students with mixed performance",
                "criteria": "Does not meet other category criteria",
                "color": "#95a5a6"  # Gray
            }
        }

    def add_student(self, name, student_id, advanced_prog, web_design, ui_design, systems_eng, azure_integration):
        if student_id in self.students:
            raise ValueError("Student ID already exists!")
        
        student = Student(name, student_id, advanced_prog, web_design, ui_design, systems_eng, azure_integration)
        self.students[student_id] = student
        return student

    def get_student(self, student_id):
        return self.students.get(student_id)

    def get_all_students(self):
        return list(self.students.values())

    def get_top_students(self, n):
        return sorted(
            self.students.values(),
            key=lambda x: x.average,
            reverse=True
        )[:n]

    def get_students_by_status(self, status):
        return [s for s in self.students.values() if s.status == status]

    def get_students_by_performance(self, performance):
        return [s for s in self.students.values() if s.performance_trend == performance]

    def get_subject_statistics(self):
        stats = {
            'Advanced Programming': {'avg': 0, 'max': 0, 'min': 100, 'passing': 0},
            'Web Applications Design': {'avg': 0, 'max': 0, 'min': 100, 'passing': 0},
            'UI Design': {'avg': 0, 'max': 0, 'min': 100, 'passing': 0},
            'Systems Engineering': {'avg': 0, 'max': 0, 'min': 100, 'passing': 0},
            'Azure Integration': {'avg': 0, 'max': 0, 'min': 100, 'passing': 0}
        }
        
        if not self.students:
            return stats

        for student in self.students.values():
            for subject, mark in student.get_subject_performance().items():
                stats[subject]['avg'] += mark
                stats[subject]['max'] = max(stats[subject]['max'], mark)
                stats[subject]['min'] = min(stats[subject]['min'], mark)
                if mark >= 60:
                    stats[subject]['passing'] += 1

        # Calculate averages
        total_students = len(self.students)
        for subject in stats:
            stats[subject]['avg'] = round(stats[subject]['avg'] / total_students, 1)
            stats[subject]['passing_rate'] = round((stats[subject]['passing'] / total_students) * 100, 1)

        return stats

    def get_overall_statistics(self):
        if not self.students:
            return {
                'total_students': 0,
                'average_grade': 0,
                'passing_rate': 0,
                'grade_distribution': {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'F': 0},
                'performance_distribution': {
                    'Excellent': 0,
                    'Good': 0,
                    'Average': 0,
                    'Needs Improvement': 0
                }
            }

        total_students = len(self.students)
        total_average = sum(s.average for s in self.students.values()) / total_students
        passing_students = sum(1 for s in self.students.values() if s.average >= 60)
        
        grade_dist = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'F': 0}
        perf_dist = {'Excellent': 0, 'Good': 0, 'Average': 0, 'Needs Improvement': 0}
        
        for student in self.students.values():
            grade_dist[student.grade] += 1
            perf_dist[student.performance_trend] += 1

        return {
            'total_students': total_students,
            'average_grade': round(total_average, 1),
            'passing_rate': round((passing_students / total_students) * 100, 1),
            'grade_distribution': grade_dist,
            'performance_distribution': perf_dist
        }

    def get_students_by_category(self, category):
        return [s for s in self.students.values() if s.category == category]

    def get_category_statistics(self):
        stats = {category: 0 for category in self.categories}
        for student in self.students.values():
            stats[student.category] += 1
        return stats

    def get_category_performance(self, category):
        students = self.get_students_by_category(category)
        if not students:
            return None
        
        return {
            'count': len(students),
            'average_score': sum(s.average for s in students) / len(students),
            'subject_averages': {
                'Advanced Programming': sum(s.advanced_prog for s in students) / len(students),
                'Web Design': sum(s.web_design for s in students) / len(students),
                'UI Design': sum(s.ui_design for s in students) / len(students),
                'Systems Engineering': sum(s.systems_eng for s in students) / len(students),
                'Azure Integration': sum(s.azure_integration for s in students) / len(students)
            }
        }

    def get_category_recommendations(self, category):
        recommendations = {
            "High Achiever": [
                "Consider advanced placement opportunities",
                "Encourage participation in competitions",
                "Assign leadership roles in group projects"
            ],
            "Consistent Performer": [
                "Focus on maintaining current performance",
                "Identify areas for potential improvement",
                "Encourage participation in additional activities"
            ],
            "Average": [
                "Provide additional study resources",
                "Schedule regular progress reviews",
                "Consider peer tutoring opportunities"
            ],
            "Needs Support": [
                "Implement personalized study plans",
                "Schedule regular one-on-one sessions",
                "Provide additional learning resources",
                "Consider remedial classes for weak subjects"
            ],
            "Under Review": [
                "Conduct detailed performance analysis",
                "Schedule meeting with student",
                "Create targeted improvement plan"
            ]
        }
        return recommendations.get(category, [])

def main():
    system = StudentReportSystem()
    
    while True:
        print("\n=== Student Report Menu ===")
        print("1. Add Student")
        print("2. View All Students")
        print("3. Search by ID")
        print("4. Show Top Students")
        print("5. Exit")

        choice = input("\n> ").strip()

        if choice == '1':
            system.add_student()
        elif choice == '2':
            system.view_all_students()
        elif choice == '3':
            system.search_by_id()
        elif choice == '4':
            system.show_top_students()
        elif choice == '5':
            print("\nThanks for using the system!")
            break
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main() 