from datetime import datetime

def check_rrn(rrn):
    rrn = rrn.replace("-", "").strip()

    if len(rrn) != 13:
        return "오류: 주민번호는 숫자 13자리여야 합니다."

    if not rrn.isdigit():
        return "오류: 숫자만 입력해야 합니다."

    gender_code = rrn[6]

    if gender_code in ["1", "3", "5", "7"]:
        gender = "남성"
    else:
        gender = "여성"

    if gender_code in ["1", "2", "5", "6"]:
        year = "19" + rrn[0:2]
    elif gender_code in ["3", "4", "7", "8"]:
        year = "20" + rrn[0:2]
    else:
        return "오류: 주민번호 뒷자리 첫 숫자가 올바르지 않습니다."

    month = rrn[2:4]
    day = rrn[4:6]

    birth_date = year + month + day
    birth_text = f"{year}-{month}-{day}"

    try:
        datetime.strptime(birth_date, "%Y%m%d")
    except ValueError:
        return "오류: 존재하지 않는 생년월일입니다."

    weights = [2, 3, 4, 5, 6, 7, 8, 9, 2, 3, 4, 5]

    total = 0

    for i in range(12):
        total += int(rrn[i]) * weights[i]

    check_number = (11 - (total % 11)) % 10

    if check_number == int(rrn[12]):
        return f"""출생일: {birth_text}
성별: {gender}

형식상 정상입니다. 단, 실제 존재 여부를 확인한 것은 아닙니다."""
    else:
        return f"""출생일: {birth_text}
성별: {gender}

오류 가능성이 있습니다. 숫자를 잘못 적었을 수 있습니다."""
