import customtkinter as ctk
from tkinter import filedialog, messagebox
import re


# =========================
# APP SETTINGS
# =========================

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")


# =========================
# STRING FUNCTIONS
# =========================

def find_text(text, keyword):
    if not keyword:
        return "กรุณาใส่คำที่ต้องการค้นหา"

    matches = list(
        re.finditer(re.escape(keyword), text, re.IGNORECASE)
    )

    if not matches:
        return f'ไม่พบคำว่า "{keyword}"'

    positions = [match.start() for match in matches]

    return (
        f'พบคำว่า "{keyword}" จำนวน {len(matches)} ครั้ง\n\n'
        f'ตำแหน่งที่พบ: {positions}'
    )


def count_text(text, keyword):
    if not keyword:
        return "กรุณาใส่คำที่ต้องการนับ"

    matches = re.findall(
        re.escape(keyword),
        text,
        re.IGNORECASE
    )

    return f'พบคำว่า "{keyword}" จำนวน {len(matches)} ครั้ง'


def replace_text(text, keyword, replacement):
    if not keyword:
        return "กรุณาใส่คำที่ต้องการแทนที่"

    return re.sub(
        re.escape(keyword),
        replacement,
        text,
        flags=re.IGNORECASE
    )


def uppercase_text(text):
    return text.upper()


def lowercase_text(text):
    return text.lower()


def title_case_text(text):
    return text.title()


def remove_extra_spaces(text):
    return re.sub(r'\s+', ' ', text).strip()


def extract_numbers(text):
    numbers = re.findall(r'\d+(?:\.\d+)?', text)

    if not numbers:
        return "ไม่พบตัวเลข"

    result = "ตัวเลขที่พบ\n\n"

    for index, number in enumerate(numbers, start=1):
        result += f"{index}. {number}\n"

    return result


def extract_emails(text):
    emails = re.findall(
        r'[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}',
        text
    )

    if not emails:
        return "ไม่พบ Email"

    result = "Email ที่พบ\n\n"

    for index, email in enumerate(emails, start=1):
        result += f"{index}. {email}\n"

    return result


def split_words(text):
    words = re.findall(r'\b\w+\b', text)

    if not words:
        return "ไม่พบคำ"

    result = f"พบทั้งหมด {len(words)} คำ\n\n"

    for index, word in enumerate(words, start=1):
        result += f"{index}. {word}\n"

    return result


# =========================
# MAIN APPLICATION
# =========================

class StringToolApp(ctk.CTk):

    def __init__(self):
        super().__init__()

        self.title("String Tools")
        self.geometry("1150x750")
        self.minsize(950, 650)

        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.create_sidebar()
        self.create_main_area()

    # =========================
    # SIDEBAR
    # =========================

    def create_sidebar(self):

        self.sidebar = ctk.CTkFrame(
            self,
            width=250,
            corner_radius=0
        )

        self.sidebar.grid(
            row=0,
            column=0,
            sticky="nsew"
        )

        self.sidebar.grid_propagate(False)

        title = ctk.CTkLabel(
            self.sidebar,
            text="STRING\nTOOLS",
            font=ctk.CTkFont(
                size=28,
                weight="bold"
            )
        )

        title.pack(
            pady=(35, 10)
        )

        subtitle = ctk.CTkLabel(
            self.sidebar,
            text="Search & Formatter",
            text_color="gray70",
            font=ctk.CTkFont(size=14)
        )

        subtitle.pack(
            pady=(0, 30)
        )

        # LOAD FILE

        load_button = ctk.CTkButton(
            self.sidebar,
            text="📂  Load TXT",
            height=45,
            command=self.load_file
        )

        load_button.pack(
            fill="x",
            padx=20,
            pady=8
        )

        # SAVE FILE

        save_button = ctk.CTkButton(
            self.sidebar,
            text="💾  Save Result",
            height=45,
            command=self.save_file
        )

        save_button.pack(
            fill="x",
            padx=20,
            pady=8
        )

        # CLEAR

        clear_button = ctk.CTkButton(
            self.sidebar,
            text="🗑  Clear All",
            height=45,
            fg_color="#444444",
            hover_color="#555555",
            command=self.clear_all
        )

        clear_button.pack(
            fill="x",
            padx=20,
            pady=8
        )

        # THEME

        appearance_label = ctk.CTkLabel(
            self.sidebar,
            text="Appearance",
            font=ctk.CTkFont(
                size=14,
                weight="bold"
            )
        )

        appearance_label.pack(
            pady=(50, 8)
        )

        self.appearance_menu = ctk.CTkOptionMenu(
            self.sidebar,
            values=[
                "Dark",
                "Light",
                "System"
            ],
            command=self.change_appearance
        )

        self.appearance_menu.set("Dark")

        self.appearance_menu.pack(
            fill="x",
            padx=20
        )

        footer = ctk.CTkLabel(
            self.sidebar,
            text="Python String Processor\n10 Functions",
            text_color="gray60",
            font=ctk.CTkFont(size=12)
        )

        footer.pack(
            side="bottom",
            pady=25
        )

    # =========================
    # MAIN AREA
    # =========================

    def create_main_area(self):

        self.main_frame = ctk.CTkFrame(
            self,
            corner_radius=0,
            fg_color="transparent"
        )

        self.main_frame.grid(
            row=0,
            column=1,
            padx=25,
            pady=20,
            sticky="nsew"
        )

        self.main_frame.grid_columnconfigure(
            0,
            weight=1
        )

        self.main_frame.grid_rowconfigure(
            1,
            weight=1
        )

        self.main_frame.grid_rowconfigure(
            4,
            weight=1
        )

        # HEADER

        header = ctk.CTkLabel(
            self.main_frame,
            text="String Search & Formatter",
            font=ctk.CTkFont(
                size=26,
                weight="bold"
            )
        )

        header.grid(
            row=0,
            column=0,
            sticky="w",
            pady=(0, 10)
        )

        # INPUT TEXT

        input_frame = ctk.CTkFrame(
            self.main_frame
        )

        input_frame.grid(
            row=1,
            column=0,
            sticky="nsew",
            pady=(0, 15)
        )

        input_label = ctk.CTkLabel(
            input_frame,
            text="Input Text",
            font=ctk.CTkFont(
                size=16,
                weight="bold"
            )
        )

        input_label.pack(
            anchor="w",
            padx=15,
            pady=(12, 5)
        )

        self.input_text = ctk.CTkTextbox(
            input_frame,
            font=ctk.CTkFont(size=14),
            corner_radius=8
        )

        self.input_text.pack(
            fill="both",
            expand=True,
            padx=15,
            pady=(0, 15)
        )

        # CONTROLS

        control_frame = ctk.CTkFrame(
            self.main_frame
        )

        control_frame.grid(
            row=2,
            column=0,
            sticky="ew",
            pady=(0, 15)
        )

        control_frame.grid_columnconfigure(
            1,
            weight=1
        )

        control_frame.grid_columnconfigure(
            3,
            weight=1
        )

        # FUNCTION

        function_label = ctk.CTkLabel(
            control_frame,
            text="Function"
        )

        function_label.grid(
            row=0,
            column=0,
            padx=(15, 5),
            pady=15
        )

        self.function_menu = ctk.CTkOptionMenu(
            control_frame,
            values=[
                "1. Find Text",
                "2. Count Text",
                "3. Replace Text",
                "4. Uppercase",
                "5. Lowercase",
                "6. Title Case",
                "7. Remove Extra Spaces",
                "8. Extract Numbers",
                "9. Extract Emails",
                "10. Split Words"
            ],
            command=self.function_changed
        )

        self.function_menu.grid(
            row=0,
            column=1,
            padx=5,
            pady=15,
            sticky="ew"
        )

        # SEARCH

        search_label = ctk.CTkLabel(
            control_frame,
            text="Search"
        )

        search_label.grid(
            row=0,
            column=2,
            padx=(15, 5)
        )

        self.search_entry = ctk.CTkEntry(
            control_frame,
            placeholder_text="Enter keyword..."
        )

        self.search_entry.grid(
            row=0,
            column=3,
            padx=5,
            sticky="ew"
        )

        # REPLACE

        replace_label = ctk.CTkLabel(
            control_frame,
            text="Replace"
        )

        replace_label.grid(
            row=1,
            column=0,
            padx=(15, 5),
            pady=(0, 15)
        )

        self.replace_entry = ctk.CTkEntry(
            control_frame,
            placeholder_text="Replacement text..."
        )

        self.replace_entry.grid(
            row=1,
            column=1,
            padx=5,
            pady=(0, 15),
            sticky="ew"
        )

        # PROCESS BUTTON

        self.process_button = ctk.CTkButton(
            control_frame,
            text="▶  Process Text",
            height=40,
            font=ctk.CTkFont(
                size=15,
                weight="bold"
            ),
            command=self.process_text
        )

        self.process_button.grid(
            row=1,
            column=2,
            columnspan=2,
            padx=(15, 15),
            pady=(0, 15),
            sticky="ew"
        )

        # RESULT HEADER

        result_header = ctk.CTkFrame(
            self.main_frame,
            fg_color="transparent"
        )

        result_header.grid(
            row=3,
            column=0,
            sticky="ew"
        )

        result_label = ctk.CTkLabel(
            result_header,
            text="Result",
            font=ctk.CTkFont(
                size=16,
                weight="bold"
            )
        )

        result_label.pack(
            side="left"
        )

        self.status_label = ctk.CTkLabel(
            result_header,
            text="Ready",
            text_color="gray60"
        )

        self.status_label.pack(
            side="right"
        )

        # OUTPUT

        output_frame = ctk.CTkFrame(
            self.main_frame
        )

        output_frame.grid(
            row=4,
            column=0,
            sticky="nsew",
            pady=(5, 0)
        )

        self.output_text = ctk.CTkTextbox(
            output_frame,
            font=ctk.CTkFont(size=14)
        )

        self.output_text.pack(
            fill="both",
            expand=True,
            padx=15,
            pady=15
        )

        self.function_changed(
            self.function_menu.get()
        )

    # =========================
    # PROCESS
    # =========================

    def process_text(self):

        try:

            text = self.input_text.get(
                "1.0",
                "end"
            ).strip()

            if not text:

                messagebox.showwarning(
                    "Warning",
                    "กรุณาใส่ข้อความก่อน"
                )

                return

            selected = self.function_menu.get()

            keyword = self.search_entry.get()

            replacement = self.replace_entry.get()

            if selected == "1. Find Text":

                result = find_text(
                    text,
                    keyword
                )

            elif selected == "2. Count Text":

                result = count_text(
                    text,
                    keyword
                )

            elif selected == "3. Replace Text":

                result = replace_text(
                    text,
                    keyword,
                    replacement
                )

            elif selected == "4. Uppercase":

                result = uppercase_text(text)

            elif selected == "5. Lowercase":

                result = lowercase_text(text)

            elif selected == "6. Title Case":

                result = title_case_text(text)

            elif selected == "7. Remove Extra Spaces":

                result = remove_extra_spaces(text)

            elif selected == "8. Extract Numbers":

                result = extract_numbers(text)

            elif selected == "9. Extract Emails":

                result = extract_emails(text)

            elif selected == "10. Split Words":

                result = split_words(text)

            else:

                result = "กรุณาเลือก Function"

            self.output_text.delete(
                "1.0",
                "end"
            )

            self.output_text.insert(
                "1.0",
                result
            )

            self.status_label.configure(
                text="✓ Process completed"
            )

        except Exception as error:

            messagebox.showerror(
                "Error",
                f"เกิดข้อผิดพลาด\n\n{error}"
            )

    # =========================
    # FUNCTION CHANGE
    # =========================

    def function_changed(
        self,
        selected
    ):

        if selected in [
            "1. Find Text",
            "2. Count Text"
        ]:

            self.search_entry.configure(
                state="normal"
            )

            self.replace_entry.configure(
                state="disabled"
            )

        elif selected == "3. Replace Text":

            self.search_entry.configure(
                state="normal"
            )

            self.replace_entry.configure(
                state="normal"
            )

        else:

            self.search_entry.configure(
                state="disabled"
            )

            self.replace_entry.configure(
                state="disabled"
            )

    # =========================
    # LOAD FILE
    # =========================

    def load_file(self):

        try:

            file_path = filedialog.askopenfilename(
                title="Open Text File",
                filetypes=[
                    ("Text Files", "*.txt"),
                    ("All Files", "*.*")
                ]
            )

            if not file_path:
                return

            with open(
                file_path,
                "r",
                encoding="utf-8"
            ) as file:

                content = file.read()

            self.input_text.delete(
                "1.0",
                "end"
            )

            self.input_text.insert(
                "1.0",
                content
            )

            self.status_label.configure(
                text="✓ File loaded"
            )

        except Exception as error:

            messagebox.showerror(
                "Error",
                f"ไม่สามารถเปิดไฟล์ได้\n\n{error}"
            )

    # =========================
    # SAVE FILE
    # =========================

    def save_file(self):

        try:

            result = self.output_text.get(
                "1.0",
                "end"
            ).strip()

            if not result:

                messagebox.showwarning(
                    "Warning",
                    "ยังไม่มีผลลัพธ์ให้บันทึก"
                )

                return

            file_path = filedialog.asksaveasfilename(
                title="Save Result",
                defaultextension=".txt",
                filetypes=[
                    ("Text Files", "*.txt")
                ]
            )

            if not file_path:
                return

            with open(
                file_path,
                "w",
                encoding="utf-8"
            ) as file:

                file.write(result)

            self.status_label.configure(
                text="✓ File saved"
            )

            messagebox.showinfo(
                "Success",
                "บันทึกไฟล์เรียบร้อย"
            )

        except Exception as error:

            messagebox.showerror(
                "Error",
                f"ไม่สามารถบันทึกไฟล์ได้\n\n{error}"
            )

    # =========================
    # CLEAR
    # =========================

    def clear_all(self):

        self.input_text.delete(
            "1.0",
            "end"
        )

        self.output_text.delete(
            "1.0",
            "end"
        )

        self.search_entry.configure(
            state="normal"
        )

        self.replace_entry.configure(
            state="normal"
        )

        self.search_entry.delete(
            0,
            "end"
        )

        self.replace_entry.delete(
            0,
            "end"
        )

        self.function_changed(
            self.function_menu.get()
        )

        self.status_label.configure(
            text="Ready"
        )

    # =========================
    # APPEARANCE
    # =========================

    def change_appearance(
        self,
        mode
    ):

        ctk.set_appearance_mode(mode)


# =========================
# RUN PROGRAM
# =========================

if __name__ == "__main__":

    app = StringToolApp()

    app.mainloop()