import tkinter as tk
import requests

API_KEY = "API_KEYINGIZNI_BU_YERGA_QO'YING"

def get_weather():
    city = entry.get()
    if not city:
        result_label.config(text="Shahar nomini kiriting!")
        return

    url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric",
        "lang": "uz"
    }

    try:
        response = requests.get(url, params=params)
        data = response.json()

        if response.status_code == 200:
            temp = data["main"]["temp"]
            weather = data["weather"][0]["description"]
            humidity = data["main"]["humidity"]

            result = (
                f"Shahar: {city}\n"
                f"Harorat: {temp}°C\n"
                f"Holat: {weather}\n"
                f"Namlik: {humidity}%"
            )
            result_label.config(text=result)
        else:
            result_label.config(text="Shahar topilmadi ❌")

    except Exception as e:
        result_label.config(text="Internet xatosi!")

# ----- GUI -----
root = tk.Tk()
root.title("Ob-havo dasturi")
root.geometry("300x250")
root.resizable(False, False)

tk.Label(root, text="Shahar nomini kiriting:", font=("Arial", 11)).pack(pady=10)

entry = tk.Entry(root, font=("Arial", 12), justify="center")
entry.pack()

tk.Button(root, text="Tekshirish", font=("Arial", 11),
          command=get_weather).pack(pady=10)

result_label = tk.Label(root, text="", font=("Arial", 10), justify="left")
result_label.pack(pady=10)

root.mainloop()
