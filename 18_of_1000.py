inventory = ["knife", "apple", "battery", "apple", "apple", "water"]

def count_items(items_list, target_item):
    count =0
    for i in range(len(items_list)):
        if target_item==items_list[i]:
            count+=1
    return count


def clean_inventory(items_list, trash_item):
    clean_list = []
    for i in items_list:
        if i!=trash_item:
            clean_list.append(i)
    return clean_list


apples_count = count_items(inventory, "apple")
print(clean_inventory(inventory, "battery"))
print(f"У тебе в рюкзаку {apples_count} яблук.")