import pdb

num_list = [500, 600, 700]
alpha_list = ['x', 'y', 'z']


def nested_loop():
    for number in num_list:
        print(number)

        # Trigger debugger at this line
        #pdb.set_trace()
        for letter in alpha_list:
            print(letter)
def main():
    #pdb.set_trace()
    nested_loop()
    print("main over!!!")

if __name__ == '__main__':
    pdb.set_trace()
    main()