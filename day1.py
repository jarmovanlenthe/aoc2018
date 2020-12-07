current_frequency = 0
seen_freqs = {current_frequency}

part_one_done = False
part_two_done = False

with open('day1_input.txt', 'r') as f:
    lines = f.readlines()

    loop = 1
    while not part_two_done:
        for line in lines:
            loop += 1
            current_frequency += int(line)
            
            seen_freqs.add(current_frequency)
            if not part_two_done and len(seen_freqs) < loop:
                print("Day 1, part two: {}".format(current_frequency))
                part_two_done = True
        if not part_one_done:
            print("Day 1, part one: {}".format(current_frequency))
            part_one_done = True
