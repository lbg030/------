print("과연 내 콜레스테롤 수치는?")

fat = int(input("중성 지방량을 적어주세요"))
hdl = int(input("고밀도지단백을 적어주세요"))
ldl = int(input("저밀도 저단백을 적어주세요"))
result = hdl + ldl + (fat / 5)

if result <= 199 :
    print("혈관 상태가 아주 좋아요 이대로 유지하세요")
elif result <= 239 :
    print("혈관 상태가 부실해요 의사와 상담 하세요")
else :
    print("자칫 잘못하면 콜레스테롤 혈증에 걸릴수도 있어요 당장 병원으로 달려가 치료하세요")