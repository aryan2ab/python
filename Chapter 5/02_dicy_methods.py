marks = {
    "Aryan": 100,
    "Yash":78,
    0: "Arnav"

}
print(marks.items())
print(marks.keys())
print(marks.values())
marks.update({"Aryan":99})
print(marks)
print(marks.get("Aryan"))