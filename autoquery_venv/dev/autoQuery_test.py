import pandas as pd


# 엑셀 파일 불러오가
req_var_excel = pd.read_excel('/Users/shin-eunjae/Desktop/test.xlsx', # 입력받는 엑셀파일 불러오게 바꿔야 함
            header = 0,
            skipfooter = 0,
            usecols = 'A:C')

print(req_var_excel)

# 필요 변수 체크
# check_requitred_variable = 0 #설정필요

#if check_requitred_variable == 0:
    #제외
#else:
    #냅두고 쿼리 만들기



# 테이블 명 비교

# 쿼리 작성

# 출력