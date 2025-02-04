# Write a function to check if a student passed, failed, or if the entered marks are invalid

def check_result(marks):
    
    if marks < 0 or marks > 100:
        return "Invalid score"
    
    return 'Pass' if marks >= 40 else 'Fail'

print(check_result(45))
