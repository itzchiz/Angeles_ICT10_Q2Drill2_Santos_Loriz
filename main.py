from js import document
import html

inte = {"Lex Basillio", "Brian Siongco", "Damien Francisco"}
comms = {"Vanya Garcia", "Juliana Reyes"}
advoc = {"Loriz Santos", "Rojiniah Tungul", "Guia Suarez", "Sean Lee"}
acad = {"Zia Sio", "Juan Cruz", "Kristen Gorospe", "Kate Sunga"}


def show_members():
    all_members = set(inte) | set(comms) | set(advoc) | set(acad)
    member_list = sorted(all_members)
    names = "<br>".join(html.escape(name) for name in member_list)

    document.getElementById("output").innerHTML = (
        "<h3>Updated Club Members</h3>" + names
    )


def add_member(event):
    global inte

    first = document.getElementById("fname").value.strip()
    last = document.getElementById("lname").value.strip()

    full_name = f"{first} {last}".strip()
    if not full_name:
        return

    inte = inte | {full_name}
    show_members()

    document.getElementById("fname").value = ""
    document.getElementById("lname").value = ""


show_members()
