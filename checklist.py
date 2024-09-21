checklist = list()


#Understanding CRUD

def create(item): #create
    checklist.append({"item": item, "completed": False})

def read(index): #read
    return checklist[index]

def update(index, item): #update
    checklist[index]["item"] = item

def destroy(index): #destroy
    checklist.pop(index)

def list_all_items(): #check list items loop
    for check, entry in enumerate(checklist):
        check_status = "√" if entry["completed"] else " "
        print(f"{check} [{check_status}] {entry['item']}")

def mark_completed(index):
    if index < len(checklist):
        checklist[index]["completed"] = True
        print(f"Item '{checklist[index]['item']}' marked as completed.")
    else:
        print(f"Index {index} is out of range.")

def select(function_code):
    if function_code == "C":
        input_item = user_input("Input Item:")
        create(input_item)
    elif function_code == "R":
        item_index = user_input("Index Number?")
        read(int(item_index))
    elif function_code == "P":
        list_all_items()
    else:
        print("Unknown Option")

def user_input(prompt):
    user_input = input(prompt)
    return user_input
    

def test(): #tester
    create('Purple Sox')
    create("Red Cloak")

    print(read(0))
    print(read(1))

    update(0, "purple socks")

    destroy(1)

    print(read(0))
    
    list_all_items()

    select("C")

    list_all_items()

    select("R")

    list_all_items()

    user_value = user_input("Please Enter a Value:")
    print(user_value)

test()


