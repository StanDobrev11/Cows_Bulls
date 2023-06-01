from random import choice

numbers_as_tupple = ("1", "2", "3", "4", "5", "6", "7", "8", "9")
# available_numbers_as_list = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
element_list = []
non_element_list = []
chosen_numbers_list = []


# choice_list = available_numbers_as_list


def random_initial_choice(available_numbers_as_list):
    chosen_number = ""
    for i in range(4):
        number = choice(available_numbers_as_list)
        available_numbers_as_list.remove(number)
        chosen_number += number

    return chosen_number, available_numbers_as_list


def play():
    final_number_list = ["*", "*", "*", "*"]
    chosen_number_dict = {}
    available_numbers_as_list = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    returned_fm_random = random_initial_choice(available_numbers_as_list)
    chosen_number = returned_fm_random[0]
    chosen_numbers_list.append(chosen_number)

    count = 1
    print(f"Attempt: {count}")
    print(f"Give me bulls & cows in: {chosen_number}")
    bulls_in_chosen_number = int(input("How many bulls: "))
    cows_in_chosen_number = int(input("How many cows: "))

    chosen_number_dict[chosen_number] = bulls_in_chosen_number, cows_in_chosen_number
    # print(chosen_number_dict)
    total_elements_in_chosen_number = bulls_in_chosen_number + cows_in_chosen_number
    if total_elements_in_chosen_number == 1:
        returned_fm_random = random_initial_choice(available_numbers_as_list)
        chosen_number = returned_fm_random[0]
        chosen_numbers_list.append(chosen_number)

        count = 2
        print(f"Attempt: {count}")
        print(f"Give me bulls & cows in: {chosen_number}")
        bulls_in_chosen_number = int(input("How many bulls: "))
        cows_in_chosen_number = int(input("How many cows: "))

        chosen_number_dict[chosen_number] = bulls_in_chosen_number, cows_in_chosen_number

        total_elements_in_chosen_number = bulls_in_chosen_number + cows_in_chosen_number

        if total_elements_in_chosen_number == 3:
            non_element_list.append(available_numbers_as_list[0])
        elif total_elements_in_chosen_number == 2:
            element_list.append(available_numbers_as_list[0])

        # print(element_list)
        # print(non_element_list)
        available_numbers_as_list = list(chosen_numbers_list[1])
        # spare number to be use as index 2 and index 2 goes at the end
        available_numbers_as_list.pop()
        available_numbers_as_list.insert(2, element_list[0] if len(element_list) > 0 else non_element_list[0])
        available_numbers_as_list = "".join(available_numbers_as_list)
        chosen_number = available_numbers_as_list
        count = 3
        print(f"Attempt: {count}")
        print(f"Give me bulls & cows in: {chosen_number}")
        bulls_in_chosen_number = int(input("How many bulls: "))
        cows_in_chosen_number = int(input("How many cows: "))
        chosen_numbers_list.append(chosen_number)
        chosen_number_dict[chosen_number] = bulls_in_chosen_number, cows_in_chosen_number
        total_elements_in_chosen_number = bulls_in_chosen_number + cows_in_chosen_number
        # print(chosen_number_dict)
        if total_elements_in_chosen_number == 3:
            non_element_list.append(chosen_numbers_list[1][-1])
            chosen_number = list(chosen_number)
            for element in non_element_list:
                if element in chosen_number:
                    chosen_number.remove(element)
            for element in chosen_number:
                element_list.append(element)
            chosen_number = list(chosen_numbers_list[0])
            chosen_number[0], chosen_number[1] = non_element_list[0], non_element_list[1]
            chosen_number = "".join(chosen_number)
            count = 4
            print(f"Attempt: {count}")
            print(f"Give me bulls & cows in: {chosen_number}")
            bulls_in_chosen_number = int(input("How many bulls: "))
            cows_in_chosen_number = int(input("How many cows: "))
            chosen_numbers_list.append(chosen_number)
            chosen_number_dict[chosen_number] = bulls_in_chosen_number, cows_in_chosen_number
            total_elements_in_chosen_number = bulls_in_chosen_number + cows_in_chosen_number


        elif total_elements_in_chosen_number == 2:
            element_list.append(chosen_numbers_list[1][-1])
            chosen_number = chosen_numbers_list[-1]
            chosen_number = list(chosen_number)
            chosen_number[-1], chosen_number[-2] = non_element_list[0], element_list[0]
            chosen_number[0], chosen_number[1] = chosen_number[1], chosen_number[0]
            chosen_number = "".join(chosen_number)
            count = 4
            print(f"Attempt: {count}")
            print(f"Give me bulls & cows in: {chosen_number}")
            bulls_in_chosen_number = int(input("How many bulls: "))
            cows_in_chosen_number = int(input("How many cows: "))
            chosen_numbers_list.append(chosen_number)
            chosen_number_dict[chosen_number] = bulls_in_chosen_number, cows_in_chosen_number
            total_elements_in_chosen_number = bulls_in_chosen_number + cows_in_chosen_number
            if total_elements_in_chosen_number == 2:
                element_list.append(chosen_numbers_list[-2][-1])
                if cows_in_chosen_number == 0:
                    chosen_number = list(chosen_number)
                    final_number_list.insert(-2, chosen_number[-2])
                    final_number_list.pop()
                    chosen_number = chosen_numbers_list[-1]
                    chosen_number = list(chosen_number)
                    chosen_number[0] = element_list[1]
                    chosen_number = "".join(chosen_number)
                    count = 5
                    print(f"Attempt: {count}")
                    print(f"Give me bulls & cows in: {chosen_number}")
                    bulls_in_chosen_number = int(input("How many bulls: "))
                    cows_in_chosen_number = int(input("How many cows: "))
                    chosen_numbers_list.append(chosen_number)
                    chosen_number_dict[chosen_number] = bulls_in_chosen_number, cows_in_chosen_number
                    total_elements_in_chosen_number = bulls_in_chosen_number + cows_in_chosen_number
                    if total_elements_in_chosen_number == 2:
                        if cows_in_chosen_number == 1:
                            element_list.append(chosen_numbers_list[-2][0])
                            final_number_list[0] = chosen_numbers_list[-2][0]
                            final_number_list[1] = chosen_numbers_list[-1][0]
                            final_number_list[3] = chosen_numbers_list[0][0]
                            chosen_number = "".join(final_number_list)
                            count = 6
                            print(f"Attempt: {count}")
                            print(f"Give me bulls & cows in: {chosen_number}")
                            bulls_in_chosen_number = int(input("How many bulls: "))
                            cows_in_chosen_number = int(input("How many cows: "))
                            chosen_numbers_list.append(chosen_number)
                            chosen_number_dict[chosen_number] = bulls_in_chosen_number, cows_in_chosen_number
                            total_elements_in_chosen_number = bulls_in_chosen_number + cows_in_chosen_number
                            if total_elements_in_chosen_number == 3:
                                final_number_list[3] = chosen_numbers_list[0][1]
                                chosen_number = "".join(final_number_list)
                                count = 7
                                print(f"Attempt: {count}")
                                print(f"Give me bulls & cows in: {chosen_number}")
                                bulls_in_chosen_number = int(input("How many bulls: "))
                                cows_in_chosen_number = int(input("How many cows: "))
                                chosen_numbers_list.append(chosen_number)
                                chosen_number_dict[chosen_number] = bulls_in_chosen_number, cows_in_chosen_number
                            else:
                                print("You win")

                        # elif cows_in_chosen_number == 0:
                        #     element_list.append(chosen_numbers_list[-1][1])
                        #     non_element_list.append(chosen_numbers_list[-2][0])
                        #     non_element_list.append(chosen_numbers_list[0][-1])
                        #     final_number_list[1] = element_list[1]
                        #     chosen_number = final_number_list
                        #     # chosen_number[-1] = chosen_numbers_list[0][0]
                        #     chosen_number = "".join(chosen_number)
                        #     count = 6
                        #     print(f"Attempt: {count}")
                        #     print(f"Give me bulls & cows in: {chosen_number}")
                        #     bulls_in_chosen_number = int(input("How many bulls: "))
                        #     cows_in_chosen_number = int(input("How many cows: "))
                        #     chosen_numbers_list.append(chosen_number)
                        #     chosen_number_dict[chosen_number] = bulls_in_chosen_number, cows_in_chosen_number
                        #     total_elements_in_chosen_number = bulls_in_chosen_number + cows_in_chosen_number
                        #     if total_elements_in_chosen_number == 3:
                        #         chosen_number = final_number_list
                        #         chosen_number[-1] = chosen_numbers_list[0][1]
                        #         chosen_number = "".join(chosen_number)
                        #         count = 7
                        #         print(f"Attempt: {count}")
                        #         print(f"Give me bulls & cows in: {chosen_number}")
                        #         bulls_in_chosen_number = int(input("How many bulls: "))
                        #         cows_in_chosen_number = int(input("How many cows: "))
                        #         chosen_numbers_list.append(chosen_number)
                        #         chosen_number_dict[chosen_number] = bulls_in_chosen_number, cows_in_chosen_number
                        #         total_elements_in_chosen_number = bulls_in_chosen_number + cows_in_chosen_number
                        #     else:
                        #         print("Game Over")
                elif cows_in_chosen_number == 1:
                    pass




            elif total_elements_in_chosen_number == 3:
                non_element_list.append(chosen_numbers_list[-2][-1])

        print(chosen_numbers_list)
        print(chosen_number_dict)
        print()
        print("Element: ", element_list)
        print("Not element: ", non_element_list)
        print(final_number_list)

        #


play()
# print(chosen_number, chosen_numbers_list)
