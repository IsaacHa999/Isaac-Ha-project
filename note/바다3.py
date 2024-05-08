# 사과 개수
total_apples = 1200

# 사과상자에
apples_per_box = 36

# 사과상자의 개수 
full_boxes = total_apples // apples_per_box
print("완성된 사과상자의 개수:", full_boxes, "개")

# 완성되지 않은 사과
remaining_apples = total_apples % apples_per_box
print("완성되지 않은 사과의 개수:", remaining_apples, "개")
