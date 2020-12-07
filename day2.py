amount_two = 0
amount_three = 0

with open('day2_input.txt', 'r') as f:
    box_ids = f.readlines()

    for box_id in box_ids:
        two = False
        three = False
        for current_char in range(97, 97+26):
            if not two and box_id.count(chr(current_char)) == 2:
                amount_two += 1
                two = True
            if not three and box_id.count(chr(current_char)) == 3:
                amount_three += 1
                three = True
            if two and three:
                break

    print("Amount two: {}".format(amount_two))
    print("Amount three: {}".format(amount_three))
    print("Result: {}".format(amount_two * amount_three))

    for box_id in box_ids:
        for box_id2 in box_ids:
            check_list = [abs(ord(x)-ord(y)) for x,y in zip(box_id, box_id2)]
            check_list = list(filter(lambda a: a != 0, check_list))
            if len(check_list) == 1:
                print(box_id, box_id2)
                print("Result: {}".format(''.join([x for x,y in zip(box_id, box_id2) if x==y])))
                break
