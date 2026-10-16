from pyscript import document

grade_7 = {"Joaquin Hizon", "Eron Almiron"}
grade_8 = {"Thomas Cruz", "Alexander Great"}
grade_9 = {"Coca Cola", "Jane Doe"}
grade_10 = {"Chloe Almiron", "Sebastian Stan"}

def add_member(e):
    members_set = grade_7 | grade_8 | grade_9 | grade_10

    #getting first and last name
    first_name = document.getElementById("firstname").value.strip()
    last_name = document.getElementById("lastname").value.strip()
    full_name = f"{first_name} {last_name}"

    #putting the new input inside a set
    new_member_set = {full_name}

    #combining grade sets and the new member set
    members_set = members_set | new_member_set

    members_list_html = "<br>".join(sorted(members_set))

    #calculating total members 
    total_count = len(members_set)

    document.getElementById("members_box").innerHTML = (
        f"Total Member: {total_count}",
        f"All Members:<br>{members_list_html}"
    )