import requests
import csv
from bs4 import BeautifulSoup as bs

url = "https://results.jntukucev.ac.in/helper.php?gamaOne=getResult"

sem_code = [1, 2, 12, 23, 41, 59, 75, 101]

hallticket = ['19VV1A1201', '19VV1A1202', '19VV1A1203', '19VV1A1204', '19VV1A1205', '19VV1A1206', '19VV1A1207', '19VV1A1208', '19VV1A1209', '19VV1A1210', '19VV1A1211', '19VV1A1212', '19VV1A1213', '19VV1A1214', '19VV1A1215', '19VV1A1216', '19VV1A1217', '19VV1A1218', '19VV1A1219', '19VV1A1220', '19VV1A1221', '19VV1A1222', '19VV1A1223', '19VV1A1224', '19VV1A1225', '19VV1A1226', '19VV1A1227', '19VV1A1228', '19VV1A1229', '19VV1A1230', '19VV1A1231',
              '19VV1A1232', '19VV1A1233', '19VV1A1234', '19VV1A1235', '19VV1A1236', '19VV1A1237', '19VV1A1238', '19VV1A1239', '19VV1A1240', '19VV1A1241', '19VV1A1242', '19VV1A1243', '19VV1A1244', '19VV1A1245', '19VV1A1246', '19VV1A1247', '19VV1A1248', '19VV1A1249', '19VV1A1250', '19VV1A1251', '19VV1A1252', '19VV1A1253', '19VV1A1254', '19VV1A1255', '19VV1A1256', '19VV1A1257', '19VV1A1258', '19VV1A1259', '19VV1A1260', '19VV1A1261', '19VV1A1262', '19VV1A1263']
complete_data = []
for roll in hallticket:
    sgpa_arr = []
    cgpa = 0
    sem_count = 0
    print("running rollnumber"+roll)
    for sem in sem_code:
        try:
            response = requests.post(
                url, data={"hallticket": roll, "result": sem})
            data = bs(response.text, "html.parser")
            sgpa = data.find("div", {"data-title": "SGPA"}).getText()
            try:
                sgpa_arr.append(float(sgpa))
            except:
                sgpa_arr.append("fail")
            try:
                cgpa += float(sgpa)
            except:
                cgpa = "backlog"
        except:
            sgpa_arr.append("-")
        sem_count = sem_count+1
    if (cgpa != "backlog"):
        cgpa = round(cgpa/sem_count, 3)
    complete_data.append({"HallTicket": roll, "sem1": sgpa_arr[0], "sem2": sgpa_arr[1], "sem3": sgpa_arr[2], "sem4": sgpa_arr[3],
                         "sem5": sgpa_arr[4], "sem6": sgpa_arr[5], "sem7": sgpa_arr[6], "sem8": sgpa_arr[7], "CGPA": cgpa})

    headers = ["HallTicket", "sem1", "sem2", "sem3",
               "sem4", "sem5", "sem6", "sem7", "sem8", "CGPA"]

    filename = "University Grades.csv"

    with open(filename, "w") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=headers)

        writer.writeheader()

        writer.writerows(complete_data)
