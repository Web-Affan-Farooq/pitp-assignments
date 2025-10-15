## .read_csv()
## .read_json()
## .read_excel()
## .to_excel()
## .to_json()
## .to_csv()
## .describe()
## .info()
## .shape ---- shape[0] -> number of rows  shape[1] -> number of columns
## .isnull() returns the data frame with only True and False filled (False is null)
## .copy() copy entire dataset

# import pandas as pd

# data = {
#     "Names": [
#         "Affan",
#         "Amir",
#         "Khalid",
#         "Ali",
#         "Kasim",
#         "Rashid",
#         "Khalil",
#         "Ahmed",
#         "Mustafa",
#         "Habib",
#     ],
#     "Age": [16, 17, 29, 28, 50, 60, 10, 84, 34, 34],
#     "TotalMarks": [100, 90, 39, 40, 83, 56, 28, 40, 100, 34],
#     "RollNumbers": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
# }
# df = pd.DataFrame(data)
# result = df[df["TotalMarks"] == 100]["RollNumbers"]
# print(result)

import pandas as pd
import numpy as np

# data = {
#     "Names": [
#         "Affan",
#         "Amir",
#         "Khalid",
#         "Ali",
#         "Kasim",
#         "Rashid",
#         "Khalil",
#         "Ahmed",
#         "Mustafa",
#         "Habib",
#     ],
#     "Age": [16, 17, 29, 28, 50, 60, 10, 84, 34, 34],
#     "Maths": [1, 90, 30, 40, 28, 48, 29, 39, 39, 10],
#     "Chemistry": [1, 90, 30, 40, 28, 48, 29, 39, 39, 10],
#     "Physics": [1, 90, 30, 40, 28, 48, 29, 39, 39, 10],
#     "RollNumber": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
# }
# pd.DataFrame(data).to_excel("./data.xlsx")

total = 300
passing_marks = (70 / 100) * total

## ____ Create total marks columns ...
df = pd.read_excel("./data.xlsx")
arr = np.array([df["Maths"], df["Chemistry"], df["Physics"]])

total_marks = []
for i in range(len(df["Maths"])):
    marks_obtained = int(sum(arr[0:3, i]))
    total_marks.append(marks_obtained)

df["TotalMarks"] = total_marks

## calculate percentages ...

percentages = [(num * 100) / 300 for num in df["TotalMarks"]]
df["Percentages"] = percentages

## _____ Step_3 .. Create status column
status_array = []
for num in df["TotalMarks"]:
    if num >= passing_marks:
        status_array.append("Pass")
    else:
        status_array.append("Fail")

df["Status"] = status_array
df.to_excel("./final.xlsx")
