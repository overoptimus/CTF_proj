a = '8842101220480224404014224202480122'
a_list = a.split('0')
flag = ''
for i_str in a_list:
    # print(i_str)
    add_num = 0
    for i in i_str:
        add_num += int(i)

    add_num = add_num + 64
    # print(add_num)
    flag += chr(add_num)

print(flag)
