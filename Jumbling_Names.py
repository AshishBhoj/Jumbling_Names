def jumbled_names(name_list):
    import random
    first_name = [x[0] for x in name_list]
    last_name_list = [x[1:] for x in name_list]
    last_name = [" ".join(last_name_list) for last_name_list in last_name_list]
    random.shuffle(last_name)
    jumble_names = [" ".join(name) for name in list(map(list, list(zip(first_name, last_name))))]
    return jumble_names

if __name__ == '__main__':
    restart = 'y'
    name_list = []

    while restart == 'y':
        number = int(input("Enter the Number of Students : "))
        for i in range(0,number):
            name_list.append(input(f"\nEnter {i+1} Student Full Name : ").split(" "))

        funny_names = jumbled_names(name_list)
        print(f"\nFunny Names are {funny_names}")

        restart = input("\nPress y to restart : ").lower()
        if restart != 'y':
            print("Thank you")
            break

