from pyscript import document

club_info = {
    "Marching Band": {
        "Name": "Marching Band",
        "Moderator": "Mr. Alumno",
        "Meeting Schedule": "Monday, Tuesday, and Wednesday at 3:00 PM - 4:30 PM",
        "Description": "The Marching Band is a group of talented musicians.",
        "Location": "Marching Band Room",
        "No. Of Members": "42"
    },

    "Dance Club": {
        "Name": "Dance Club",
        "Moderator": "Mr. Cases",
        "Meeting Schedule": "Tuesday 3:00 PM - 5:00 PM",
        "Description": "The Dance Club is a vibrant group that explores various dance styles.",
        "Location": "Teatro Preciosza",
        "No. Of Members": "30"
    },

    "Math Club": {
        "Name": "Math Club",
        "Moderator": "Mr. Gabuya",
        "Meeting Schedule": "Monday 2:30 PM - 4:30 PM",
        "Description": "The Math Club enhances students' mathematical skills.",
        "Location": "Room 404",
        "No. Of Members": "16"
    },

    "Science Club": {
        "Name": "Science Club",
        "Moderator": "Ms. Maramag",
        "Meeting Schedule": "Tue 3-5 PM | Fri 2-3 PM",
        "Description": "The Science Club explores scientific concepts.",
        "Location": "Room 404",
        "No. Of Members": "18"
    },

    "Cocc Club": {
        "Name": "Cadet Officer Candidate Course (COCC)",
        "Moderator": "Ms. David",
        "Meeting Schedule": "Wednesday 2:30 PM - 4:30 PM",
        "Description": "A leadership training program for cadet corps roles.",
        "Location": "Quadrangle / Teatro / 4th Floor",
        "No. Of Members": "24"
    },

    "Glee Club": {
        "Name": "Glee Club",
        "Moderator": "Mr. Martin",
        "Meeting Schedule": "Mon & Fri 3:00 PM - 4:30 PM",
        "Description": "A vocal ensemble that performs music.",
        "Location": "HS Music Room",
        "No. Of Members": "28"
    },

    "CommArts": {
        "Name": "Communication Arts Club",
        "Moderator": "Ms. Fernandez",
        "Meeting Schedule": "Wed & Fri 3:00 PM - 4:00 PM",
        "Description": "Focuses on media, journalism, and public speaking.",
        "Location": "Room 406",
        "No. Of Members": "23"
    }
}


def Show_Club(event):
    selected = document.getElementById("Club_Selection").value
    info = club_info.get(selected)

    output = document.getElementById("output-box")

    if info:
        text = (
            f"Name: {info['Name']}\n"
            f"Moderator: {info['Moderator']}\n"
            f"Meeting Schedule: {info['Meeting Schedule']}\n"
            f"Description: {info['Description']}\n"
            f"Location: {info['Location']}\n"
            f"No. Of Members: {info['No. Of Members']}"
        )
    else:
        text = "No information found." #Incase the selected club does not exist in the dictionary.

    output.innerText = text #Would set the inner text of the output HTML element to the club information or a not found message.
