def translate_list(text_list, language):
    if language == "English":
        return text_list

    # simple placeholder (LLM-ready layer)
    hindi_map = {
        "Eligible for business loan": "व्यवसाय ऋण के लिए पात्र",
        "Suitable for working capital loan": "कार्यशील पूंजी ऋण के लिए उपयुक्त",
        "Improve finances before borrowing": "ऋण लेने से पहले वित्तीय स्थिति सुधारें",
        "Reduce operating costs": "परिचालन लागत कम करें",
        "Consider refinancing loan": "ऋण पुनर्वित्त पर विचार करें"
    }

    translated = []

    for t in text_list:
        translated.append(hindi_map.get(t, t))

    return translated