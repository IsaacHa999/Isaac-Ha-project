def remove_n_chars_from_lines(text, n):
    lines = text.split('\n')  # 개행 문자를 기준으로 텍스트를 줄 단위로 분리
    result = []
    
    for line in lines:
        if len(line) >= n:
            result.append(line[n:])  # n개의 문자를 삭제하고 남은 부분을 결과에 추가
        else:
            result.append("")  # 줄의 길이가 n보다 작으면 빈 문자열을 추가
    
    return '\n'.join(result)  # 줄 단위로 결과를 합쳐서 반환

# 예시 텍스트
text = """
안녕하세요,
파이썬을 배우고 있는
학습자입니다.
"""

# 각 줄에서 3개의 문자 삭제
new_text = remove_n_chars_from_lines(text, 3)
print(new_text)
# 출력:
# 세요,
# 썬을 배우고 있는
# 학습자입니다.
