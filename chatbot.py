from college_data import colleges


def get_bot_response(college_name, message):

    message = message.lower().strip()

    college = colleges[college_name]

    # -------- HISTORY --------

    if any(word in message for word in [
        "history",
        "about college",
        "about the college",
        "established",
        "started",
        "founded"
    ]):
        return college["history"]

    # -------- VISION --------

    elif any(word in message for word in [
        "vision",
        "goal",
        "future"
    ]):
        return college["vision"]

    # -------- MISSION --------

    elif any(word in message for word in [
        "mission",
        "objective",
        "purpose"
    ]):
        return college["mission"]

    # -------- COURSES --------

    elif any(word in message for word in [
        "course",
        "courses",
        "branch",
        "branches",
        "program",
        "programs",
        "department"
    ]):

        text = "The following courses are offered:\n\n"

        for course in college["courses"]:
            text += "• " + course + "\n"

        return text

    # -------- FEES --------

    elif any(word in message for word in [
        "fee",
        "fees",
        "tuition",
        "cost",
        "payment"
    ]):
        return college["fees"]

    # -------- ELIGIBILITY --------

    elif any(word in message for word in [
        "eligibility",
        "eligible",
        "qualification",
        "qualify"
    ]):
        return college["eligibility"]

    # -------- ADMISSION --------

    elif any(word in message for word in [
        "admission",
        "admissions",
        "join",
        "apply",
        "seat"
    ]):
        return college["admission"]

    # -------- CUTOFF --------

    elif any(word in message for word in [
        "cutoff",
        "cut off",
        "rank",
        "eamcet",
        "jee"
    ]):
        return college["cutoff"]

    # -------- PLACEMENTS --------

    elif any(word in message for word in [
        "placement",
        "placements",
        "job",
        "jobs",
        "company",
        "companies",
        "package"
    ]):
        return college["placements"]

    # -------- HOSTEL --------

    elif any(word in message for word in [
        "hostel",
        "hostels",
        "mess",
        "room",
        "accommodation"
    ]):
        return college["hostel"]

    # -------- TRANSPORT --------

    elif any(word in message for word in [
        "transport",
        "bus",
        "buses",
        "college bus"
    ]):
        return college["transport"]

    # -------- FACILITIES --------

    elif any(word in message for word in [
        "facility",
        "facilities",
        "library",
        "lab",
        "labs",
        "wifi",
        "sports"
    ]):
        return college["facilities"]

    # -------- EXAMS --------

    elif any(word in message for word in [
        "exam",
        "exams",
        "semester",
        "internal",
        "assessment"
    ]):
        return college["exams"]

    # -------- CONTACT --------

    elif any(word in message for word in [
        "contact",
        "phone",
        "email",
        "website",
        "address"
    ]):
        return college["contact"]

    # -------- LOCATION --------

    elif any(word in message for word in [
        "location",
        "where",
        "place",
        "address"
    ]):
        return "The college is located at " + college["location"] + "."

    # -------- NAAC --------

    elif "naac" in message:
        return "The NAAC Accreditation of this college is " + college["naac"] + "."

    # -------- NBA --------

    elif "nba" in message:
        return "NBA Accreditation : " + college["nba"]

    # -------- GREETING --------

    elif any(word in message for word in [
        "hi",
        "hello",
        "hey"
    ]):
        return "Hello! 👋 How can I help you today?"

    # -------- THANK YOU --------

    elif any(word in message for word in [
        "thanks",
        "thank you"
    ]):
        return "You're welcome! 😊 Feel free to ask if you have more questions."

    # -------- DEFAULT --------

    else:
        return (
            "Sorry, I couldn't understand your question.\n\n"
            "You can ask me about:\n"
            "• Courses\n"
            "• Fees\n"
            "• Admission\n"
            "• Eligibility\n"
            "• Cutoff\n"
            "• Placements\n"
            "• Hostel\n"
            "• Facilities\n"
            "• Transport\n"
            "• History\n"
            "• Vision\n"
            "• Mission\n"
            "• Exams\n"
            "• Contact\n"
            "• Location\n"
            "• NAAC\n"
            "• NBA"
        )