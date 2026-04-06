import tkinter as tk
from tkinter import ttk
import matplotlib
matplotlib.use("TkAgg")  # Use Tkinter backend for Matplotlib
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class DataVisualizer:
    def __init__(self):
        # Initialize main Tkinter window
        self.data = []
        self.root = tk.Tk()
        self.root.title("Product Review Sentiment Analyzer")
        self.entry = tk.Entry(self.root, width=100, )
        self.entry.pack()
        self.product = ""


    def save(self):
        """Saves user input from entry and closes input window"""
        self.product = self.entry.get()
        self.root.quit()

    def get_user_input(self):
        """Prompts user to enter the name of an Apple product to analyze"""
        prompt_label = tk.Label(self.root, text="Enter the product Name: ")
        prompt_label.pack()

        submit_button = tk.Button(self.root, text="Submit", command=self.save)
        submit_button.pack()

        end_button = tk.Button(self.root, text="Exit", command=self.root.destroy)
        end_button.pack()

        self.root.mainloop()
        return self.product

    def show_results(self, summary):
        """Displays sentiment analysis results in a new window with text and bar chart"""
        parent = self.root
        results_win = tk.Toplevel(parent)
        results_win.title(f"Review Summary - {summary.product_name}")
        results_win.geometry("1280x720")

        # Configure grid layout on the results window
        results_win.columnconfigure(0, weight=1)
        results_win.columnconfigure(1, weight=2)
        results_win.rowconfigure(0, weight=1)

        # ----- LEFT SIDE: Textual Analysis -----
        left_frame = ttk.Frame(results_win, padding=10)
        left_frame.grid(row=0, column=0, sticky="nsew")
        left_frame.rowconfigure(1, weight=1)

        title_label = ttk.Label(
            left_frame,
            text=summary.product_name,
            font=("Segoe UI", 16, "bold")
        )
        title_label.grid(row=0, column=0, sticky="w", pady=(0, 10))

        # General analysis text
        general_frame = ttk.LabelFrame(left_frame, text="General Analysis")
        general_frame.grid(row=1, column=0, sticky="nsew")
        general_frame.rowconfigure(0, weight=1)
        general_frame.columnconfigure(0, weight=1)

        general_text = tk.Text(general_frame, wrap="word", height=8)
        general_text.grid(row=0, column=0, sticky="nsew")
        general_text.insert("1.0", summary.general_analysis)
        general_text.config(state="disabled")

        general_scroll = ttk.Scrollbar(
            general_frame, orient="vertical", command=general_text.yview
        )
        general_scroll.grid(row=0, column=1, sticky="ns")
        general_text["yscrollcommand"] = general_scroll.set

        # Feature analysis
        feature_frame = ttk.LabelFrame(left_frame, text="Feature Analyses")
        feature_frame.grid(row=2, column=0, sticky="nsew", pady=(10, 0))
        feature_frame.rowconfigure(0, weight=1)
        feature_frame.columnconfigure(0, weight=1)

        feature_text = tk.Text(feature_frame, wrap="word")
        feature_text.grid(row=0, column=0, sticky="nsew")

        for feat in summary.results:
            feature_text.insert(
                "end",
                f"Feature: {feat.feature}\n"
                f"Score: {feat.score}\n"
                f"Analysis: {feat.analysis}\n\n"
            )
        feature_text.config(state="disabled")

        feature_scroll = ttk.Scrollbar(
            feature_frame, orient="vertical", command=feature_text.yview
        )
        feature_scroll.grid(row=0, column=1, sticky="ns")
        feature_text["yscrollcommand"] = feature_scroll.set



        # ----- RIGHT SIDE: Horizontal Feature Bar Chart -----
        right_frame = ttk.Frame(results_win, padding=10)
        right_frame.grid(row=0, column=1, sticky="nsew")
        right_frame.rowconfigure(0, weight=1)
        right_frame.columnconfigure(0, weight=1)

        features = [f.feature for f in summary.results]
        scores = [f.score for f in summary.results]

        fig = Figure(figsize=(6, 5), dpi=100)
        ax_bar = fig.add_subplot(1, 1, 1)

        # Horizontal bar chart for feature scores
        ax_bar.barh(features, scores)
        ax_bar.set_title("Feature Scores (Horizontal Bar Chart)")
        ax_bar.set_xlabel("Score")

        fig.tight_layout()

        canvas = FigureCanvasTkAgg(fig, master=right_frame)
        canvas.draw()
        canvas_widget = canvas.get_tk_widget()
        canvas_widget.grid(row=0, column=0, sticky="nsew")


        # Exit button for results window
        end_button = tk.Button(results_win, text="Exit", command=results_win.destroy)
        end_button.grid(row=1, column=0, columnspan=2, pady=10)

        # Make the results window modal relative to the parent window
        results_win.transient(parent)
        results_win.grab_set()
        results_win.focus_set()
        results_win.wait_window()


if __name__ == "__main__":
    visualizer = DataVisualizer()
    print(visualizer.get_user_input())