print("Checklist Maker Initiated!")
print('.\n.\n.')

title = input("Title: ")
checklist_file = open(title +".txt", "w")
checklist_file.write("\t\t" + title)
item = []

def if_item_is_carrot(x):
    if x == "^":
        return ''
    else:
        return x

while item != "<":
    item = (input("[ ]"))
    if item == "^":
        tab = input("\t->")
        checklist_file.write("\n\t->" + tab)
    else:
        item = if_item_is_carrot(item)
        if item != "<":
            checklist_file.write("\n[ ]" + item)
        else:
            checklist_file.close()

else:
	print('.\n.\n.')
	print("Checklist Maker Terminated!")

