import tkinter as tk
from tkinter import filedialog, messagebox, Toplevel, Text, Scrollbar
import base64


# Function to encode file to base64
def encode_file_to_base64(file_path):
    with open(file_path, "rb") as file:
        encoded_string = base64.b64encode(file.read()).decode('utf-8')
    return encoded_string


# Function to generate minified JavaScript code
def generate_js_code():
    keyword = keyword_entry.get()
    file_path = file_path_entry.get()
    strobe_rate = strobe_rate_entry.get()
    search_frequency = search_frequency_entry.get()
    loop_audio = loop_audio_var.get()

    if not keyword or not file_path or not strobe_rate or not search_frequency:
        messagebox.showerror("Error", "Please provide all inputs.")
        return

    try:
        base64_string = encode_file_to_base64(file_path)
        js_code = f'''
        javascript:(function(){{
            const keyword="{keyword}";
            const sound=new Audio('data:audio/mp3;base64,{base64_string}');
            let strobeInterval;
            let audioPlaying=false;
            function startStrobe(){{
                let body=document.body;
                strobeInterval=setInterval(()=>{{body.style.backgroundColor=body.style.backgroundColor==='red'?'blue':'red';}}, {strobe_rate});
            }}
            function stopStrobe(){{
                clearInterval(strobeInterval);
                document.body.style.backgroundColor='';
            }}
            function checkForKeyword(){{
                console.log("Checking for keyword...");
                if(document.body.innerText.includes(keyword)&&!audioPlaying){{
                    console.log("Keyword found!");
                    sound.loop={str(loop_audio).lower()};
                    sound.play().catch(error=>console.log('Error playing sound:',error));
                    startStrobe();
                    audioPlaying=true;
                }}else{{
                    console.log("Keyword not found.");
                }}
            }}
            function stopAll(){{
                if(audioPlaying){{
                    sound.pause();
                    sound.currentTime=0;
                    stopStrobe();
                    audioPlaying=false;
                    window.removeEventListener('mousemove',stopAll);
                }}
            }}
            setInterval(checkForKeyword, {search_frequency});
            window.addEventListener('mousemove',stopAll);
        }})();
        '''
        js_code_minified = js_code.replace("\n", "").replace("    ", "")
        output_text.delete(1.0, tk.END)
        output_text.insert(tk.END, js_code_minified)
    except Exception as e:
        messagebox.showerror("Error", f"Failed to generate code: {e}")


# Function to browse and select the MP3 file
def browse_file():
    file_path = filedialog.askopenfilename(filetypes=[("MP3 files", "*.mp3")])
    if file_path:
        file_path_entry.delete(0, tk.END)
        file_path_entry.insert(0, file_path)


# Function to copy generated code to clipboard
def copy_to_clipboard():
    root.clipboard_clear()
    root.clipboard_append(output_text.get(1.0, tk.END))
    messagebox.showinfo("Copied", "JavaScript code copied to clipboard!")


# Function to show how to use the bookmarklet
def show_how_to():
    how_to_window = Toplevel(root)
    how_to_window.title("How to Use the Bookmarklet")
    how_to_window.geometry("600x400")

    scrollbar = Scrollbar(how_to_window)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    how_to_text = Text(how_to_window, wrap=tk.WORD, yscrollcommand=scrollbar.set)
    how_to_text.pack(expand=True, fill=tk.BOTH)
    scrollbar.config(command=how_to_text.yview)

    instructions = """How to Use the Bookmarklet:

1. Generate the JavaScript Code:
   - Enter the desired keyword.
   - Browse and select an MP3 file.
   - Enter the strobe rate in milliseconds (e.g., 500 for 500ms).
   - Enter the search frequency in milliseconds (e.g., 5000 for 5 seconds).
   - Check the "Loop Audio" checkbox if you want the audio to loop.
   - Click "Generate JavaScript Code" to produce the minified JavaScript bookmarklet code.
   - Click "Copy to Clipboard" to copy the generated code to the clipboard.

2. Add the Bookmarklet:
   - Open your web browser.
   - Create a new bookmark.
   - In the URL field of the bookmark, paste the JavaScript code copied to the clipboard.
   - Name the bookmark something meaningful (e.g., "Solarwinds Incident Alert").

3. Use the Bookmarklet:
   - Navigate to the SolarWinds ServiceDesk page in your browser.
   - Click the bookmark you created.
   - The script will start running and check for the keyword you specified every X milliseconds.
   - If the keyword is found, it will play the selected audio file and trigger a color strobing effect.
   - Move your mouse to stop the audio and strobing effect.

I'm planning to make improvements and add more tools.
"""
    how_to_text.insert(tk.END, instructions)


# Tkinter GUI setup
root = tk.Tk()
root.title("Solarwinds Incident Alert Generator")

tk.Label(root, text="Keyword:").grid(row=0, column=0, padx=10, pady=10, sticky=tk.W)
keyword_entry = tk.Entry(root, width=50)
keyword_entry.grid(row=0, column=1, padx=10, pady=10)

tk.Label(root, text="MP3 File:").grid(row=1, column=0, padx=10, pady=10, sticky=tk.W)
file_path_entry = tk.Entry(root, width=50)
file_path_entry.grid(row=1, column=1, padx=10, pady=10)
browse_button = tk.Button(root, text="Browse", command=browse_file)
browse_button.grid(row=1, column=2, padx=10, pady=10)

tk.Label(root, text="Strobe Rate (ms):").grid(row=2, column=0, padx=10, pady=10, sticky=tk.W)
strobe_rate_entry = tk.Entry(root, width=20)
strobe_rate_entry.grid(row=2, column=1, padx=10, pady=10, sticky=tk.W)

tk.Label(root, text="Search Frequency (ms):").grid(row=3, column=0, padx=10, pady=10, sticky=tk.W)
search_frequency_entry = tk.Entry(root, width=20)
search_frequency_entry.grid(row=3, column=1, padx=10, pady=10, sticky=tk.W)

loop_audio_var = tk.BooleanVar()
loop_audio_check = tk.Checkbutton(root, text="Loop Audio", variable=loop_audio_var)
loop_audio_check.grid(row=4, column=0, columnspan=2, padx=10, pady=10, sticky=tk.W)

generate_button = tk.Button(root, text="Generate JavaScript Code", command=generate_js_code)
generate_button.grid(row=5, column=0, columnspan=3, padx=10, pady=20)

copy_button = tk.Button(root, text="Copy to Clipboard", command=copy_to_clipboard)
copy_button.grid(row=6, column=0, columnspan=3, padx=10, pady=10)

how_to_button = tk.Button(root, text="How to Use", command=show_how_to)
how_to_button.grid(row=7, column=0, columnspan=3, padx=10, pady=10)

output_text = tk.Text(root, wrap=tk.WORD, width=80, height=10)
output_text.grid(row=8, column=0, columnspan=3, padx=10, pady=10)

root.mainloop()