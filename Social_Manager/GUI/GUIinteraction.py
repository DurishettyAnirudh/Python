import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter import ttk
from tkcalendar import DateEntry
import mysql.connector
import os
from datetime import datetime
import subprocess

# Database Configuration
DB_CONFIG = {
    'host': 'localhost',
    'port': 3306,
    'user': 'root',
    'password': 'root',
    'database': 'client_upload'
}

class VideoManagerApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Video Manager")
        self.configure(bg="#f0f0f0")
        self.geometry(f"{self.winfo_screenwidth()}x{self.winfo_screenheight()-100}+0+0")

        # UI Variables
        self.serial_numbers = []
        self.title_entries = []
        self.category_entries = []
        self.video_paths = []
        self.privacy_statuses = []
        self.description_entries = []
        self.keyword_entries = []
        self.date_entries = []
        self.hour_selectors = []
        self.minute_selectors = []

        # Row Count
        self.row_count = 0

        # Create Main Frame and Canvas for Scrollable Content
        self.main_frame = tk.Frame(self, bg="#f0f0f0")
        self.main_frame.pack(fill=tk.BOTH, expand=True)

        self.canvas = tk.Canvas(self.main_frame, bg="#f0f0f0")
        self.scrollbar = tk.Scrollbar(self.main_frame, orient=tk.VERTICAL, command=self.canvas.yview)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        self.frame = tk.Frame(self.canvas, bg="#f0f0f0")
        self.canvas.create_window((0, 0), window=self.frame, anchor='nw')
        self.frame.bind("<Configure>", self.on_frame_configure)

        # Configure grid layout
        for col in range(11):
            self.frame.columnconfigure(col, weight=1)

        # Add Header Row
        self.add_row(is_label_row=True)

        # Load Existing Data
        self.load_data()

        # Add Buttons
        self.add_row_button = tk.Button(self, text="Add Row", command=self.add_row)
        self.add_row_button.pack(pady=10)

        self.save_button = tk.Button(self, text="Save", command=self.save_data)
        self.save_button.pack(pady=10)

    def on_frame_configure(self, event):
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))

    def add_row(self, is_label_row=False, data=None):
        if is_label_row:
            headers = ["Serial Number", "Title", "Category", "Video Upload", "Video Path", "Privacy Status",
                       "Description", "Keywords", "Date", "Time", "Actions"]
            for col, header in enumerate(headers):
                label = tk.Label(self.frame, text=header, bg="#d3d3d3", relief="solid", anchor='center')
                label.grid(row=self.row_count, column=col, padx=5, pady=10, sticky="nsew")
        else:
            if data:
                serial_number, title, category, video_path, privacy_status, description, keywords, date, time = data
                hour, minute, _ = time.split(':')
            else:
                serial_number = str(self.row_count)
                title = category = video_path = description = keywords = ""
                date = datetime.now().strftime('%Y-%m-%d')
                hour = datetime.now().strftime('%H')
                minute = datetime.now().strftime('%M')
                privacy_status = "Public"

            # Serial Number
            serial_number_label = tk.Label(self.frame, text=serial_number, anchor='center', relief="solid")
            serial_number_label.grid(row=self.row_count, column=0, padx=5, pady=10, sticky="nsew")
            self.serial_numbers.append(serial_number_label)

            # Title
            title_entry = tk.Entry(self.frame, justify='center')
            title_entry.insert(0, title)
            title_entry.grid(row=self.row_count, column=1, padx=5, pady=10, sticky="nsew")
            self.title_entries.append(title_entry)

            # Category
            category_entry = tk.Entry(self.frame, justify='center')
            category_entry.insert(0, category)
            category_entry.grid(row=self.row_count, column=2, padx=5, pady=10, sticky="nsew")
            self.category_entries.append(category_entry)

            # Video Upload
            video_path_var = tk.StringVar()
            video_path_var.set(video_path)
            self.video_paths.append(video_path_var)
            video_upload_button = tk.Button(self.frame, text="Upload Video",
                                            command=lambda row_index=self.row_count: self.upload_video(row_index))
            video_upload_button.grid(row=self.row_count, column=3, padx=5, pady=10, sticky="nsew")
            video_path_label = tk.Label(self.frame, textvariable=video_path_var, anchor='center', relief="solid")
            video_path_label.grid(row=self.row_count, column=4, padx=5, pady=10, sticky="nsew")

            # Privacy Status
            privacy_status = tk.StringVar()
            privacy_status.set(privacy_status)
            privacy_options = ttk.Combobox(self.frame, textvariable=privacy_status, values=["Public", "Private"],
                                           justify='center')
            privacy_options.grid(row=self.row_count, column=5, padx=5, pady=10, sticky="nsew")
            self.privacy_statuses.append(privacy_status)

            # Description
            description_entry = tk.Entry(self.frame, justify='center')
            description_entry.insert(0, description)
            description_entry.grid(row=self.row_count, column=6, padx=5, pady=10, sticky="nsew")
            self.description_entries.append(description_entry)

            # Keywords
            keywords_entry = tk.Entry(self.frame, justify='center')
            keywords_entry.insert(0, keywords)
            keywords_entry.grid(row=self.row_count, column=7, padx=5, pady=10, sticky="nsew")
            self.keyword_entries.append(keywords_entry)

            # Date
            date_picker = DateEntry(self.frame, date_pattern='yyyy-mm-dd')
            date_picker.set_date(date)
            date_picker.grid(row=self.row_count, column=8, padx=5, pady=10, sticky="nsew")
            self.date_entries.append(date_picker)

            # Time
            time_frame = tk.Frame(self.frame)
            time_frame.grid(row=self.row_count, column=9, padx=5, pady=10, sticky="nsew")
            hour_selector = ttk.Combobox(time_frame, values=[f"{i:02d}" for i in range(24)], width=2, justify='center')
            hour_selector.set(hour)
            hour_selector.pack(side=tk.LEFT, padx=(0, 2))
            self.hour_selectors.append(hour_selector)
            minute_selector = ttk.Combobox(time_frame, values=[f"{i:02d}" for i in range(60)], width=2,
                                           justify='center')
            minute_selector.set(minute)
            minute_selector.pack(side=tk.LEFT)
            self.minute_selectors.append(minute_selector)

            # Actions
            action_frame = tk.Frame(self.frame)
            action_frame.grid(row=self.row_count, column=10, padx=5, pady=10, sticky="nsew")
            delete_button = tk.Button(action_frame, text="Delete",command=lambda row_index=self.row_count: self.delete_row(row_index))
            delete_button.pack(side=tk.LEFT, padx=(0, 5))
            upload_button = tk.Button(action_frame, text="Upload", command=self.trigger_upload_app(self.row_count))
            upload_button.pack(side=tk.LEFT)

        self.row_count += 1

    def upload_video(self, row_index):
        file_path = filedialog.askopenfilename(filetypes=[("Video Files", "*.mp4;*.avi;*.mov")])
        if file_path:
            destination = os.path.join('app_directory', os.path.basename(file_path))
            print(destination)
            os.makedirs('app_directory', exist_ok=True)
            with open(file_path, 'rb') as fsrc:
                with open(destination, 'wb') as fdst:
                    fdst.write(fsrc.read())
            self.video_paths[row_index-1].set(destination)

    def trigger_upload_app(self, row_index):
        subprocess.Popen(["python", "../Youtube/another_application.py"])

    def delete_row(self, row_index):
        self.delete_from_db(row_index - 1)
        for widget in self.frame.grid_slaves(row=row_index):
            widget.grid_forget()
        self.update_ui_after_delete(row_index)

    def update_ui_after_delete(self, deleted_index):
        # Remove data from lists
        del self.serial_numbers[deleted_index - 1]
        del self.title_entries[deleted_index - 1]
        del self.category_entries[deleted_index - 1]
        del self.video_paths[deleted_index - 1]
        del self.privacy_statuses[deleted_index - 1]
        del self.description_entries[deleted_index - 1]
        del self.keyword_entries[deleted_index - 1]
        del self.date_entries[deleted_index - 1]
        del self.hour_selectors[deleted_index - 1]
        del self.minute_selectors[deleted_index - 1]

        # Shift rows up
        for i in range(deleted_index, self.row_count):
            for widget in self.frame.grid_slaves(row=i + 1):
                widget.grid_configure(row=i)

        self.row_count -= 1

    def delete_from_db(self, row_index):
        serial_number = self.serial_numbers[row_index].cget("text")
        try:
            conn = mysql.connector.connect(**DB_CONFIG)
            cursor = conn.cursor()
            cursor.execute('DELETE FROM videos WHERE serial_number = %s', (serial_number,))
            conn.commit()
            cursor.close()
            conn.close()
            messagebox.showinfo("Success", f"Row {row_index + 1} deleted successfully!")
        except mysql.connector.Error as err:
            messagebox.showerror("Error", f"Error: {err}")

    def save_data(self):
        for i in range(self.row_count - 1):
            date_time = f"{self.date_entries[i].get()} {self.hour_selectors[i].get()}:{self.minute_selectors[i].get()}:00"
            data = {
                'Serial Number': self.serial_numbers[i].cget("text"),
                'Title': self.title_entries[i].get(),
                'Category': self.category_entries[i].get(),
                'Video Path': self.video_paths[i].get(),
                'Privacy Status': self.privacy_statuses[i].get(),
                'Description': self.description_entries[i].get(),
                'Keywords': self.keyword_entries[i].get(),
                'Date and Time': date_time
            }

            try:
                conn = mysql.connector.connect(**DB_CONFIG)
                cursor = conn.cursor()

                cursor.execute('''
                    CREATE TABLE IF NOT EXISTS videos (
                        id INT AUTO_INCREMENT PRIMARY KEY,
                        serial_number VARCHAR(255),
                        title VARCHAR(255),
                        category VARCHAR(255),
                        video_path VARCHAR(255),
                        privacy_status VARCHAR(255),
                        description TEXT,
                        keywords VARCHAR(255),
                        date_time DATETIME
                    )
                ''')

                cursor.execute('SELECT COUNT(*) FROM videos WHERE serial_number = %s', (data['Serial Number'],))
                result = cursor.fetchone()
                if result[0] == 0:
                    cursor.execute('''
                        INSERT INTO videos (serial_number, title, category, video_path, privacy_status, description, keywords, date_time)
                        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
                    ''', (
                        data['Serial Number'],
                        data['Title'],
                        data['Category'],
                        data['Video Path'],
                        data['Privacy Status'],
                        data['Description'],
                        data['Keywords'],
                        data['Date and Time']
                    ))

                    conn.commit()

                cursor.close()
                conn.close()

                messagebox.showinfo("Success", "Data saved successfully!")

            except mysql.connector.Error as err:
                messagebox.showerror("Error", f"Error: {err}")

    def load_data(self):
        try:
            conn = mysql.connector.connect(**DB_CONFIG)
            cursor = conn.cursor()
            cursor.execute(
                'SELECT serial_number, title, category, video_path, privacy_status, description, keywords, date_time FROM videos')
            rows = cursor.fetchall()
            for row in rows:
                serial_number, title, category, video_path, privacy_status, description, keywords, date_time = row
                date_time_str = date_time.strftime('%Y-%m-%d %H:%M:%S')
                date, time = date_time_str.split()
                self.add_row(data=(serial_number, title, category, video_path, privacy_status, description, keywords, date, time))
            cursor.close()
            conn.close()
        except mysql.connector.Error as err:
            messagebox.showerror("Error", f"Error: {err}")


if __name__ == "__main__":
    app = VideoManagerApp()
    app.mainloop()
