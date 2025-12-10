from pyscript import document, display

def calculate_gwa(e):
    first = document.getElementById("firstname").value
    last = document.getElementById("lastname").value

    science = float(document.getElementById("science").value)
    math = float(document.getElementById("math").value)
    english = float(document.getElementById("english").value)
    filipino = float(document.getElementById("filipino").value)
    ict = float(document.getElementById("ict").value)
    ss = float(document.getElementById("socialstudies").value)

    # Subject Names
    subjects = {
        "Science": science,
        "Math": math,
        "English": english,
        "Filipino": filipino,
        "ICT": ict,
        "Social Studies": ss
    }

    # Weighted Units
    weights = {
        "Science": 5,
        "Math": 5,
        "English": 5,
        "Filipino": 3,
        "ICT": 2,
        "Social Studies": 3
    }

    weighted_sum = sum(subjects[sub] * weights[sub] for sub in subjects) #Formula for gwa such that it would multiply the subject grade to its weight.
    total_units = sum(weights.values())
    gwa = weighted_sum / total_units

    summary = "Grade Summary:" #Would summarize the grades of each subject and its corresponding grade for each.
    for sub, grade in subjects.items():
        summary += f"{sub}: {grade:.0f}\n"

    # Output to HTML
    display(summary, target="output")
    display(f"Your GWA: {gwa:.2f}", target="highlight") #The target in both of these display functions would make it so that the output would be shown in the specified HTML element with the corresponding ID.