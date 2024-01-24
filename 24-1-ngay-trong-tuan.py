nhap_thu = input("Nhập ngày trong tuần:")
if nhap_thu == "thứ 7":
    print("Đi chơi thể thao")
elif nhap_thu == "Chủ nhật":
    print("nghỉ ngơi")
elif (nhap_thu == "thứ 2" or nhap_thu == "thứ 3" or nhap_thu == "thứ 4" or nhap_thu == "thứ 5" or nhap_thu == "thứ 6" ):
    print("Ngày đi làm")
else:
    print("Sai cú pháp, nhập lại theo cú pháp bao gồm 'thứ x' với x là số hoặc chủ nhật")