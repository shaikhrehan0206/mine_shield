#mine shield dashboard implemented here
import tkinter as tk
from tkinter import ttk
import random
import time


# -----------------------------
# Mine Shield Dashboard
# Simulated Sensor Data
# -----------------------------

class MineShieldDashboard:

    def __init__(self, root):
        self.root = root
        self.root.title("MINE SHIELD - AI Mine Vehicle Safety Dashboard")
        self.root.geometry("1200x700")
        self.root.configure(bg="#101820")

        self.create_header()
        self.create_camera_panel()
        self.create_sensor_panel()
        self.create_data_panel()
        self.create_risk_panel()
        self.create_footer()

        self.update_data()

    # -----------------------------
    # Header
    # -----------------------------
    def create_header(self):

        header = tk.Frame(
            self.root,
            bg="#17232D",
            height=70
        )
        header.pack(fill="x")

        title = tk.Label(
            header,
            text="MINE SHIELD",
            font=("Arial", 26, "bold"),
            fg="white",
            bg="#17232D"
        )
        title.pack(pady=(10, 0))

        subtitle = tk.Label(
            header,
            text="AI-BASED MINE VEHICLE SAFETY SYSTEM",
            font=("Arial", 11),
            fg="#B8C7D1",
            bg="#17232D"
        )
        subtitle.pack()

    # -----------------------------
    # Camera / YOLO Panel
    # -----------------------------
    def create_camera_panel(self):

        frame = tk.LabelFrame(
            self.root,
            text=" CAMERA / YOLO DETECTION ",
            font=("Arial", 12, "bold"),
            fg="white",
            bg="#101820"
        )
        frame.place(x=20, y=90, width=560, height=300)

        self.camera_display = tk.Label(
            frame,
            text="LIVE CAMERA\n\nVEHICLE DETECTED\n\nYOLO Confidence: 94.2 %",
            font=("Arial", 18, "bold"),
            fg="white",
            bg="#263746",
            width=45,
            height=10
        )
        self.camera_display.pack(padx=15, pady=15)

    # -----------------------------
    # Sensor Status
    # -----------------------------
    def create_sensor_panel(self):

        frame = tk.LabelFrame(
            self.root,
            text=" SENSOR STATUS ",
            font=("Arial", 12, "bold"),
            fg="white",
            bg="#101820"
        )
        frame.place(x=600, y=90, width=570, height=300)

        self.status_labels = {}

        sensors = [
            "Camera / Vision",
            "LiDAR",
            "Radar",
            "GPS / GNSS"
        ]

        for sensor in sensors:

            row = tk.Frame(
                frame,
                bg="#101820"
            )
            row.pack(fill="x", padx=30, pady=12)

            name = tk.Label(
                row,
                text=sensor,
                font=("Arial", 13),
                fg="white",
                bg="#101820",
                width=20,
                anchor="w"
            )
            name.pack(side="left")

            status = tk.Label(
                row,
                text="● ACTIVE",
                font=("Arial", 13, "bold"),
                fg="#00FF88",
                bg="#101820"
            )
            status.pack(side="right")

            self.status_labels[sensor] = status

    # -----------------------------
    # Sensor Data
    # -----------------------------
    def create_data_panel(self):

        frame = tk.LabelFrame(
            self.root,
            text=" REAL-TIME SENSOR DATA ",
            font=("Arial", 12, "bold"),
            fg="white",
            bg="#101820"
        )
        frame.place(x=20, y=410, width=1150, height=120)

        self.lidar_value = self.create_value(frame, "LiDAR", "18.6 m", 20)
        self.radar_value = self.create_value(frame, "Radar", "19.1 m", 290)
        self.speed_value = self.create_value(frame, "Relative Speed", "-2.8 m/s", 560)
        self.ttc_value = self.create_value(frame, "TTC", "3.8 s", 850)

    def create_value(self, parent, title, value, x):

        box = tk.Frame(
            parent,
            bg="#263746",
            width=230,
            height=75
        )
        box.place(x=x, y=20)

        tk.Label(
            box,
            text=title,
            font=("Arial", 11),
            fg="#B8C7D1",
            bg="#263746"
        ).pack(pady=(8, 0))

        value_label = tk.Label(
            box,
            text=value,
            font=("Arial", 18, "bold"),
            fg="white",
            bg="#263746"
        )
        value_label.pack()

        return value_label

    # -----------------------------
    # Risk Assessment
    # -----------------------------
    def create_risk_panel(self):

        frame = tk.LabelFrame(
            self.root,
            text=" RISK ASSESSMENT ",
            font=("Arial", 12, "bold"),
            fg="white",
            bg="#101820"
        )
        frame.place(x=20, y=545, width=570, height=90)

        self.risk_label = tk.Label(
            frame,
            text="WARNING",
            font=("Arial", 22, "bold"),
            fg="orange",
            bg="#101820"
        )
        self.risk_label.pack(pady=15)

    # -----------------------------
    # Footer
    # -----------------------------
    def create_footer(self):

        frame = tk.Frame(
            self.root,
            bg="#17232D"
        )
        frame.place(x=610, y=545, width=560, height=90)

        self.gps_label = tk.Label(
            frame,
            text="GPS: 19.5847° N, 74.2967° E",
            font=("Arial", 11),
            fg="white",
            bg="#17232D"
        )
        self.gps_label.pack(pady=(12, 5))

        self.database_label = tk.Label(
            frame,
            text="DATABASE: RECORDING",
            font=("Arial", 11, "bold"),
            fg="#00FF88",
            bg="#17232D"
        )
        self.database_label.pack()

    # -----------------------------
    # Simulated Data Update
    # -----------------------------
    def update_data(self):

        lidar = round(random.uniform(15, 30), 1)
        radar = round(lidar + random.uniform(0.3, 1.5), 1)
        speed = round(random.uniform(-4, -1), 1)

        ttc = round(
            lidar / abs(speed),
            1
        )

        self.lidar_value.config(
            text=f"{lidar} m"
        )

        self.radar_value.config(
            text=f"{radar} m"
        )

        self.speed_value.config(
            text=f"{speed} m/s"
        )

        self.ttc_value.config(
            text=f"{ttc} s"
        )

        self.root.after(
            1000,
            self.update_data
        )


# -----------------------------
# Start Dashboard
# -----------------------------

if __name__ == "__main__":

    root = tk.Tk()

    dashboard = MineShieldDashboard(root)

    root.mainloop()
