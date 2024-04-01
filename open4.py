def input_student_info():
    student_info = {}
    print("학번:")
    student_info['학번'] = input()
    print("이름:")
    student_info['이름'] = input()
    print("영어:")
    student_info['영어'] = int(input())
    print("C-언어:")
    student_info['C-언어'] = int(input())
    print("파이썬:")
    student_info['파이썬'] = int(input())
    return student_info

def calculate_total_average(student_info):
    total = student_info['영어'] + student_info['C-언어'] + student_info['파이썬']
    average = total // 3  # 정수 나눗셈으로 변경하여 소수점 이하를 버림
    student_info['총점'] = total
    student_info['평균'] = average
    return student_info


def calculate_grade(student_info):
    score = student_info['평균']
    if score >= 90:
        grade = 'A'
    elif score >= 80:
        grade = 'B+'
    elif score >= 70:
        grade = 'B'
    elif score >= 60:
        grade = 'C+'
    elif score >= 50:
        grade = 'C'
    else:
        grade = 'F'
    student_info['학점'] = grade
    return student_info

def calculate_rank(student_list):
    ranked_student_list = sorted(student_list, key=lambda x: x['총점'], reverse=True)
    for i, student in enumerate(ranked_student_list):
        student['등수'] = i + 1
    return ranked_student_list

def print_student_info_table(student_list):
    print("=" * 90)
    print("{:<15}{:<15}{:<10}{:<10}{:<12}{:<10}{:<10}{:<12}{:<10}".format(
        '학번', '이름', '영어', 'C-언어', '파이썬', '총점', '평균', '학점', '등수'))
    print("=" * 90)
    for student in student_list:
        print("{:<15}{:<15}{:<10}{:<10}{:<12}{:<10.2f}{:<10}{:<12}{:<10}".format(
            student['학번'], student['이름'], student['영어'], student['C-언어'], student['파이썬'],
            student['총점'], student['평균'], student['학점'], student['등수']))
    print("=" * 90)

def main():
    student_list = []
    num_students = 5

    print("성적관리 프로그램\n")
    for i in range(num_students):
        print("=" * 90)
        print(f"학생 정보 입력 - {i + 1}번째 학생")
        student_info = input_student_info()
        student_info = calculate_total_average(student_info)
        student_info = calculate_grade(student_info)
        student_list.append(student_info)

    ranked_student_list = calculate_rank(student_list)
    print_student_info_table(ranked_student_list)

if __name__ == "__main__":
    main()


