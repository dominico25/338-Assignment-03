import sys

def main():
    mylist = []
    previous_size = sys.getsizeof(mylist)
    for i in range(64):
        mylist.append(i)
        print(i)
        if (sys.getsizeof(mylist) != previous_size):
            print("Capacity has changed")
        previous_size = sys.getsizeof(mylist)
    
    
if __name__ == "__main__":
    main()