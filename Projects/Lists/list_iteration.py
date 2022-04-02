available_parts = ["computer",
                   "monitor",
                   "keyboard",
                   "mouse",
                   "mouse-pad",
                   "hdmi-cable",
                   "dvd-drive"]
current_choice = "_"
computer_parts = []  # create an empty list

while current_choice != '0':
    if current_choice in "123456":
        print("Adding {}".format(current_choice))
        if current_choice == '1':
            computer_parts.append("computer")
        elif current_choice == '2':
            computer_parts.append("monitor")
        elif current_choice == '3':
            computer_parts.append("keyboard")
        elif current_choice == '4':
            computer_parts.append("mouse")
        elif current_choice == '5':
            computer_parts.append("mouse-pad")
        elif current_choice == '6':
            computer_parts.append("hdmi-cable")
    else:
        print("Please add options from the list below:")
        for part in available_parts:
            print("{0}: {1}".format(available_parts.index(part) + 1, part))
    current_choice = input()
print(computer_parts)
print(' '.join(computer_parts))
