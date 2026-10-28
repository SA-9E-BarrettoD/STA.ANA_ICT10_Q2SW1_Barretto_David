from pyscript import document

club_members = [
    "Josua Ortiz",
    "David Barretto",
    "Sianna Santiago",
    "Nyle Gutierrez",
    "Sophia Pedro"
]

def result_checker(e):
    first_name = document.querySelector("#first_name").value.strip()
    last_name = document.querySelector("#last_name").value.strip()
    full_name = first_name + " " + last_name

    result = full_name in club_members

    messages = {
        True: f"Congratulations {full_name}! You are now part of the ICT club.",
        False: f"Sorry {full_name}, your name is not on the list."
    }

    output = document.querySelector("#output")
    output.innerText = messages[result]
    output.className = "alert mt-3 mx-auto"