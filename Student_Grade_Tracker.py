# ============================================
# STUDENT GRADE TRACKER
# Rhombix Technologies - Python Development
# ============================================

def student_grade_tracker():
    student_name = input("Enter student name: ")
    num_subjects = int(input("Enter number of subjects: "))

    grades = {}
    total_obtained = 0
    total_possible = 0

    for i in range(num_subjects):
        subject_name = input(f"\nEnter subject {i+1} name: ")
        
        obtained = float(input(f"Enter marks gained in {subject_name}: "))
        out_of = float(input(f"Enter total possible marks for {subject_name}: "))
        
        grades[subject_name] = {"gained": obtained, "total": out_of}
        
        total_obtained += obtained
        total_possible += out_of

    overall_percentage = (total_obtained / total_possible) * 100 if total_possible > 0 else 0

    if overall_percentage >= 85:
        grade = "A"
    elif overall_percentage >= 70:
        grade = "B"
    elif overall_percentage >= 50:
        grade = "C"
    else:
        grade = "Fail"

    print("\n" + "="*42)
    print(f"{'STUDENT GRADE REPORT':^42}")
    print("="*42)
    print(f"Student Name: {student_name}")
    print("-" * 42)
    
    print(f"{'Subject':<15} | {'Gained':<10} | {'Out Of':<10}")
    print("-" * 42)

    for subject, score in grades.items():
        print(f"{subject:<15} | {score['gained']:<10} | {score['total']:<10}")

    print("-" * 42)
    print(f"Aggregate Score: {total_obtained} / {total_possible}")
    print(f"Overall Percentage: {overall_percentage:.2f}%")
    print(f"Final Grade: {grade}")
    print("="*42)

if __name__ == "__main__":
    student_grade_tracker()