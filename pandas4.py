import pandas as pd

students = {
    "StudentId": [1, 2, 3, 4],
    "Name": ["Ahmet", "Ayşe", "Ali", "Elif"]
}
students_df = pd.DataFrame(students)


notlar = {
    "StudentId": [1, 3, 5],
    "Grade": [80, 95, 60]
}
notlar_df = pd.DataFrame(notlar)
birleştireme = pd.merge(students_df, notlar_df, on='StudentId', how="left",)

print(birleştireme)