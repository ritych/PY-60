def main(original_list):
    for item in original_list:
        if item.isalpha():
            l_list.append(item)
        elif item.isdigit():
            n_list.append(item)


orig_list = ["a", "s", "1", "a", "32", "23"]
l_list = []
n_list = []
main(orig_list)

del (l_list[-1])

print("Список букв:", l_list[::-1])
