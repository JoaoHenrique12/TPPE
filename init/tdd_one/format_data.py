def format_data_for_display(people):
    formated_data = []
    for p in people:
        txt = p["given_name"] + " " + p["family_name"] + ": " + p["title"]
        formated_data.append(txt)
    return formated_data


def format_data_for_excel(people):
    txt = "given,family,title\n"
    for p in people:
        txt += p["given_name"] + "," + p["family_name"] + "," + p["title"] + '\n'
    return txt
