from tkinter import *
from tkinter import ttk
import requests


def get_data():
    city = city_name.get()
    try:
        response = requests.get(
            f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid=ec83f277edf7d5787f26944abeb739df"
        )
        data = response.json()

        if response.status_code == 200:
            weather_main = data.get("weather", [{}])[0].get("main", "N/A")
            weather_desc = data.get("weather", [{}])[0].get("description", "N/A")
            temp = data.get("main", {}).get("temp", 0) - 273.15
            pressure = data.get("main", {}).get("pressure", "N/A")

            w_label_1.config(text=weather_main)
            wb_label_1.config(text=weather_desc)
            temp_label_1.config(text=f"{temp:.2f}°C")
            p_label_1.config(text=pressure)
        else:
            w_label_1.config(text="Error")
            wb_label_1.config(text="Invalid city or API error")
            temp_label_1.config(text="N/A")
            p_label_1.config(text="N/A")

    except Exception as e:
        w_label_1.config(text="Error")
        wb_label_1.config(text=str(e))
        temp_label_1.config(text="N/A")
        p_label_1.config(text="N/A")


win = Tk()
win.title("Nava Weather Forecast")
win.config(bg="gray")
win.geometry("500x500")

name_label = Label(win, text="Nava Weather App", font=("Times New Roman", 30, "bold"))
name_label.place(x=25, y=50, height=50, width=450)

city_name = StringVar()

name_list = [
    "Andhra Pradesh",
    "Arunachal Pradesh",
    "Assam",
    "Bihar",
    "Chhattisgarh",
    "Goa",
    "Gujarat",
    "Haryana",
    "Himachal Pradesh",
    "Jammu and Kashmir",
    "Jharkhand",
    "Karnataka",
    "Kerala",
    "Madhya Pradesh",
    "Maharashtra",
    "Manipur",
    "Meghalaya",
    "Mizoram",
    "Nagaland",
    "Odisha",
    "Punjab",
    "Rajasthan",
    "Sikkim",
    "Tamil Nadu",
    "Telangana",
    "Tripura",
    "Uttar Pradesh",
    "Uttarakhand",
    "West Bengal",
    "Andaman and Nicobar Islands",
    "Chandigarh",
    "Dadra and Nagar Haveli",
    "Daman and Diu",
    "Lakshadweep",
    "National Capital Territory of Delhi",
    "Puducherry",
]

a = ttk.Combobox(
    win,
    values=name_list,
    font=("Times New Roman", 18, "bold"),
    textvariable=city_name,
)
a.place(x=25, y=120, height=30, width=450)


w_label = Label(win, text="Weather Condition", font=("Times New Roman", 10, "bold"))
w_label.place(x=25, y=280, height=30, width=150)

w_label_1 = Label(win, text="", font=("Times New Roman", 10, "bold"))
w_label_1.place(x=185, y=280, height=30, width=150)

wb_label = Label(win, text="Weather Description", font=("Times New Roman", 10, "bold"))
wb_label.place(x=25, y=320, height=30, width=150)

wb_label_1 = Label(win, text="", font=("Times New Roman", 10, "bold"))
wb_label_1.place(x=185, y=320, height=30, width=150)

temp_label = Label(win, text="Temperature", font=("Times New Roman", 10, "bold"))
temp_label.place(x=25, y=360, height=30, width=150)

temp_label_1 = Label(win, text="", font=("Times New Roman", 10, "bold"))
temp_label_1.place(x=185, y=360, height=30, width=150)

p_label = Label(win, text="Pressure", font=("Times New Roman", 10, "bold"))
p_label.place(x=25, y=400, height=30, width=150)

p_label_1 = Label(win, text="", font=("Times New Roman", 10, "bold"))
p_label_1.place(x=185, y=400, height=30, width=150)


done_button = Button(
    win, text="Show", font=("Times New Roman", 18, "bold"), command=get_data
)
done_button.place(x=200, y=190, height=50, width=100)


win.mainloop()
