# Write a function to split item codes into their individual components

def split_item_code(item_code):
    components = []
    current_component = ""

    for char in item_code:
        if char.isalnum():  
            if current_component:
                
                if char.isalpha() != current_component[-1].isalpha() or \
                   char.isdigit() != current_component[-1].isdigit():
                    components.append(current_component)
                    current_component = ""
            current_component += char
        else:
           
            if current_component:
                components.append(current_component)
                current_component = ""


    if current_component:
        components.append(current_component)

    return components

item_code = "ABC123-45X"
print(split_item_code(item_code))