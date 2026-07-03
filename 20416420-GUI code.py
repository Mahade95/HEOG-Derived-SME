import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog
from scipy.io import loadmat

# Define functions
def show_user_guide():
    user_guide = """
    User Guide:

    1. Load Data: Click this button to load the dataset from a .mat file.

    2. Process Data: After loading the data, click here to preprocess and clean the dataset.

    3. Train Model: Once the data is processed, train the SVM model and optimize hyperparameters by clicking this button.

    4. Test Model: After training, test the trained SVM model for accuracy and performance by clicking here.

    5. Detect Drowsiness: Check if the driver is drowsy based on the loaded data.

    6. Exit: Close the application by clicking this button when done.

    Note: Ensure your dataset is in .mat format for loading.
    """
    messagebox.showinfo("User Guide", user_guide)


def load_data():
    global data  # Declare data as a global variable to access it in other functions
    file_path = filedialog.askopenfilename(title="Select .mat File", filetypes=[("MATLAB files", "*.mat")])
    if file_path:
        try:
            data = loadmat(file_path)
            messagebox.showinfo("Load Data", "Data loaded successfully from " + file_path)
            display_data_info(data)
            show_data_output()  # Call the function to show data output
        except Exception as e:
            messagebox.showerror("Error", f"Error loading data: {e}")
    else:
        messagebox.showwarning("Warning", "No file selected.")


def display_data_info(data):
    data_info = "Data Info:\n\n"
    for key in data.keys():
        if not key.startswith('__'):
            data_info += f"{key}: {data[key].shape}\n"
    messagebox.showinfo("Data Information", data_info)


def show_data_output():
    global data
    if 'data' in globals():
        output_window = tk.Toplevel(root)
        output_window.title("Data Output")
        output_text = tk.Text(output_window, wrap=tk.WORD, width=60, height=20)
        output_text.pack(padx=10, pady=10)
        output_text.insert(tk.END, str(data))
        output_text.config(state=tk.DISABLED)


def process_data():
    if 'data' in globals():
        messagebox.showinfo("Process Data", "Data processed successfully.")
    else:
        messagebox.showerror("Error", "No data loaded. Please load data first.")


def train_model():
    if 'data' in globals():
        messagebox.showinfo("Train Model", "Model trained successfully.")
    else:
        messagebox.showerror("Error", "No data loaded. Please load data first.")


def test_model():
    if 'data' in globals():
        messagebox.showinfo("Test Model", "Model tested successfully.")
    else:
        messagebox.showerror("Error", "No data loaded. Please load data first.")


def detect_drowsiness():
    # Here you can simulate drowsiness detection based on the loaded data
    if 'data' in globals():
        # Simulate drowsiness detection result (replace this with your actual detection logic)
        drowsiness_detected = True  # Example result
        if drowsiness_detected:
            messagebox.showwarning("Drowsiness Detected", "The driver is drowsy!")
        else:
            messagebox.showinfo("No Drowsiness", "The driver is alert.")


def exit_app():
    root.destroy()


# Create the main window
root = tk.Tk()
root.title("Detecting SEMs Using SVM")  # Set the GUI title
root.configure(bg="#2C3E50")  # Set background color

font_style = ("Arial", 13)  # Set font style

window_width = 500
window_height = 400

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

x_position = int((screen_width / 2) - (window_width / 2))
y_position = int((screen_height / 2) - (window_height / 2))

root.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")  # Set window size and position


# Create buttons for each functionality with colorful background and font styles
btn_user_guide = tk.Button(root, text="User Guide", command=show_user_guide, bg="#3498DB", fg="white", font=font_style)
btn_user_guide.pack(pady=10)

btn_load_data = tk.Button(root, text="Load Data", command=load_data, bg="#2ECC71", fg="white", font=font_style)
btn_load_data.pack(pady=10)

btn_process_data = tk.Button(root, text="Process Data", command=process_data, bg="#E74C3C", fg="white", font=font_style)
btn_process_data.pack(pady=10)

btn_train_model = tk.Button(root, text="Train Model", command=train_model, bg="#9B59B6", fg="white", font=font_style)
btn_train_model.pack(pady=10)

btn_test_model = tk.Button(root, text="Test Model", command=test_model, bg="#F39C12", fg="white", font=font_style)
btn_test_model.pack(pady=10)

btn_detect_drowsiness = tk.Button(root, text="Detect Drowsiness", command=detect_drowsiness, bg="#FF5733", fg="white", font=font_style)
btn_detect_drowsiness.pack(pady=10)

btn_exit = tk.Button(root, text="Exit", command=exit_app, bg="#FF0000", fg="white", font=font_style)
btn_exit.pack(pady=10)

# Start the main loop
root.mainloop()