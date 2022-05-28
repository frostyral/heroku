from django.core.exceptions import ValidationError

def validate_names(value):
    temp = value.strip().replace(" ", "")
    if not temp.replace(",", "").isalpha():
        raise ValidationError("Invalid Input")
    return value

def validate_name_format(value):
    if not ", " in value:
        raise ValidationError("Invalid Name Format")
    return value

def validate_exam_number(value):
    if not value.isdigit():
        raise ValidationError("Invalid Exam Number")
    return value