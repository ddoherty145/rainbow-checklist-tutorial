checklist = list()

# CRUD Operations

def create(item):  # create
    checklist.append({"item": item, "completed": False})

def read(index):  # read
    if index < len(checklist):
        return checklist[index]
    else:
        print(f"Index {index} is out of range.")
        return None

def update(index, item):  # update
    if index < len(checklist):
        checklist[index]["item"] = item
    else:
        print(f"Index {index} is out of range.")

def destroy(index):  # destroy
    if index < len(checklist):
        checklist.pop(index)
    else:
        print(f"Index {index} is out of range.")

def list_all_items():  # check list items loop
    for check, entry in enumerate(checklist):
        check_status = "√" if entry["completed"] else " "
        print(f"{check} [{check_status}] {entry['item']}")

def mark_completed(index):  # mark an item as complete
    if index < len(checklist):
        checklist[index]["completed"] = True
        print(f"Item '{checklist[index]['item']}' marked as completed.")
    else:
        print(f"Index {index} is out of range.")

# Function to select operations based on user input
def select(function_code):
    if function_code == "C":
        input_item = user_input("Input Item: ")
        create(input_item)
    elif function_code == "R":
        item_index = int(user_input("Index Number? "))
        item = read(item_index)
        if item:
            print(f"[{'√' if item['completed'] else ' '}] {item['item']}")
    elif function_code == "U":
        item_index = int(user_input("Index Number? "))
        new_item = user_input("Updated Item: ")
        update(item_index, new_item)
    elif function_code == "D":
        item_index = int(user_input("Index Number to Delete? "))
        destroy(item_index)
    elif function_code == "M":
        item_index = int(user_input("Index Number to Mark Completed? "))
        mark_completed(item_index)
    elif function_code == "P":
        list_all_items()
    elif function_code == "Q":
        return False
    else:
        print("Unknown Option")
    return True

# Function to capture user input
def user_input(prompt):
    return input(prompt)

# Test function to populate list and run basic CRUD operations
def test():
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

    user_value = user_input("Please Enter a Value: ")
    print(user_value)

# Running the application loop
running = True
while running:
    selection = user_input(
        "Press C to add to List, R to Read from list, U to Update, D to Delete, M to mark Complete, P to display list, and Q to quit: ")
    running = select(selection)
