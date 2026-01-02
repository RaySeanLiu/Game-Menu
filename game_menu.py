import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk, ImageFont

class GameMenu:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Conquest Of Kingdoms")
        self.root.geometry("800x600")
        self.root.resizable(False, False)
        
        # Load background image FIRST - before creating any widgets
        self.load_background()
        
        # Center the window on screen
        self.center_window()
        
        # Create main frame with transparent background
        main_frame = tk.Frame(self.root, bg="")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Configure grid weights for centering
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        main_frame.columnconfigure(0, weight=1)
        
        # Button frame positioned at lower center
        button_frame = tk.Frame(main_frame)
        button_frame.place(relx=0.5, rely=0.75, anchor=tk.CENTER)  # Lower center positioning
        
        # Create styled buttons
        self.play_button = self.create_styled_button(button_frame, "Start", 0)
        self.options_button = self.create_styled_button(button_frame, "Options", 1)
        self.exit_button = self.create_styled_button(button_frame, "Exit", 2)
        
        # Handle window close event
        self.root.protocol("WM_DELETE_WINDOW", self.exit_clicked)
    
    def center_window(self):
        """Center the window on the screen"""
        self.root.update_idletasks()
        width = self.root.winfo_width()
        height = self.root.winfo_height()
        x = (self.root.winfo_screenwidth() // 2) - (width // 2)
        y = (self.root.winfo_screenheight() // 2) - (height // 2)
        self.root.geometry(f'{width}x{height}+{x}+{y}')
    
    def load_background(self):
        """Load and set the background image"""
        try:
            # Use medieval city background - check if file exists first
            import os
            bg_path = "assets/images/Basic Asset Pack/Pixel Art Landscapes - free/Pixel Art Landscapes 512x512 - free/Ready-To-Use_Landscapes/medieval_city_1.png"
            
            if os.path.exists(bg_path):
                self.bg_image = Image.open(bg_path)
                # Resize to fit window
                self.bg_image = self.bg_image.resize((800, 600), Image.Resampling.LANCZOS)
                self.bg_photo = ImageTk.PhotoImage(self.bg_image)
                
                # Create background label and place it behind everything
                bg_label = tk.Label(self.root, image=self.bg_photo)
                # Place background at coordinates 0,0 and fill entire window
                bg_label.place(x=0, y=0, width=800, height=600)
                # Send to very back so it's under everything
                bg_label.lower()  # Send to back
                print("Background loaded and placed successfully")
            else:
                raise FileNotFoundError(f"Background image not found at: {bg_path}")
        except Exception as e:
            print(f"Could not load background: {e}")
            # Fallback to solid color background
            self.root.configure(bg="#2C1810")
    
    def create_styled_button(self, parent, text, row):
        """Create a medieval styled button with simple orange rectangles"""
        try:
            # Create simple orange rectangles - this works perfectly
            from PIL import ImageDraw
            
            button_width, button_height = 120, 40
            normal_crop = Image.new('RGBA', (button_width, button_height), (255, 140, 0, 255))  # Orange
            pressed_crop = Image.new('RGBA', (button_width, button_height), (220, 100, 0, 255))  # Darker orange
            
            # Add simple border
            draw_normal = ImageDraw.Draw(normal_crop)
            draw_pressed = ImageDraw.Draw(pressed_crop)
            draw_normal.rectangle([0, 0, button_width-1, button_height-1], outline=(180, 80, 0, 255), width=2)
            draw_pressed.rectangle([0, 0, button_width-1, button_height-1], outline=(140, 60, 0, 255), width=2)
            
            print(f"Created simple rectangular button {row}")
            
            normal_photo = ImageTk.PhotoImage(normal_crop)
            pressed_photo = ImageTk.PhotoImage(pressed_crop)
            
            # Create a custom button using Label to avoid tkinter button issues
            button = tk.Label(parent, 
                                image=normal_photo,
                                text=text,
                                font=("Old English Text MT", 12, "bold"),
                                fg="#FFFFFF",  # White text
                                compound=tk.CENTER,
                                bg="systemTransparent",  # Use system transparent color
                                anchor=tk.CENTER,
                                cursor="hand2",  # Hand cursor on hover
                                relief=tk.FLAT,
                                bd=0)
                
                # Make label clickable
            def on_click(event):
                self.get_command(text)()
                
                def on_press(event):
                    # Change to pressed image
                    button.config(image=pressed_photo, fg="#CCCCCC")
                
                def on_release(event):
                    # Restore normal image
                    button.config(image=normal_photo, fg="#FFFFFF")
                
                button.bind("<Button-1>", on_click)
                button.bind("<ButtonPress-1>", on_press)
                button.bind("<ButtonRelease-1>", on_release)
                
                # Store both image references
                button.normal_image = normal_photo
                button.pressed_image = pressed_photo
                
                button.image = normal_photo  # Keep reference
                button.grid(row=row, column=0, pady=0)
                
                return button
                
        except Exception as e:
            print(f"Could not load button image: {e}")
            # Fallback to styled button with orange theme
            button = tk.Button(parent, 
                             text=text,
                             font=("Old English Text MT", 14, "bold"),
                             fg="#FFFFFF",
                             bg="#FF8C00",  # Dark orange color
                             width=20,
                             height=2,
                             relief=tk.RAISED,
                             bd=3,
                             command=self.get_command(text))
            button.grid(row=row, column=0, pady=0)
            return button
    
    def get_command(self, button_name):
        """Return the appropriate command for each button"""
        commands = {
            "Start": self.play_clicked,
            "Options": self.options_clicked,
            "Exit": self.exit_clicked
        }
        return commands.get(button_name, lambda: print(f"{button_name} clicked"))
    
    def play_clicked(self):
        """Handle Play button click"""
        print("Play button clicked - functionality not implemented yet")
    
    def options_clicked(self):
        """Handle Options button click"""
        print("Options button clicked - functionality not implemented yet")
    
    def exit_clicked(self):
        """Handle Exit button click"""
        self.root.quit()
        self.root.destroy()
    
    def run(self):
        """Start the application"""
        self.root.mainloop()

if __name__ == "__main__":
    app = GameMenu()
    app.run()
