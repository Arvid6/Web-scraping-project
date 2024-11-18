from projmain import scrape, sort_list
import tkinter as tk
from tkinter import ttk
import json
import webbrowser
from countrylist import getCountry


def scrapeprogram(searchwords, keywords, country):
    scrape(searchwords, keywords, country)
    # sort_list(filename, keywords)


def sortprogram(keyword, country):
    sort_list(keyword, country)


def addSearch():
    if searchword.get() != "":
        searchwords.append(searchword.get())
        searchword.delete(0, tk.END)
        updateParams()
        print(searchwords)


def addKeyword():
    if keyword.get() != "":
        keywords.append(keyword.get())
        keyword.delete(0, tk.END)
        updateParams()
        print(keywords)


def loadJSON():
    jsonoutputname = outputname + ".json"
    with open(jsonoutputname, 'r', encoding='utf-8') as json_file:
        return json.load(json_file)


def updateCountry(event):
    country = getCountry(country_combobox.get())
    region_combobox['values'] = list(country[4])
    region_combobox.set('')  # Clear previous selection


def updateURL(event):
    # Clear the URLs combobox
    selected_domain = domain_combobox.get()
    url_combobox['values'] = list(json_output[selected_domain].keys())
    url_combobox.set('')  # Clear previous selection
    output_text.delete(1.0, tk.END)  # Clear existing text


def updateText(event):
    # Get the selected URL from the dropdown
    selected_domain = domain_combobox.get()
    selected_url = url_combobox.get()

    # Get the corresponding text
    text = json_output[selected_domain].get(selected_url, "No text available.")
    if len(text) > 30000:
        output_text.config(state=tk.NORMAL)  # Enable the text box
        output_text.delete(1.0, tk.END)  # Clear existing text
        output_text.insert(tk.END, "text to long to display")  # Insert the corresponding text
        output_text.config(state=tk.DISABLED)  # Disable it again
        return
    # Clear existing text and insert the new text
    output_text.config(state=tk.NORMAL)  # Enable the text box
    output_text.delete(1.0, tk.END)  # Clear existing text
    output_text.insert(tk.END, text)  # Insert the corresponding text
    output_text.config(state=tk.DISABLED)  # Disable it again


def updateParams():
    # Get the selected URL from the dropdown
    srs = "Searchwords: " + str(searchwords)
    key = "Keywords: " + str(keywords)

    # Get the corresponding text
    text = srs +"\n" + key

    # Clear existing text and insert the new text
    searchparams.config(state=tk.NORMAL)  # Enable the text box
    searchparams.delete(1.0, tk.END)  # Clear existing text
    searchparams.insert(tk.END, text)  # Insert the corresponding text
    searchparams.config(state=tk.DISABLED)  # Disable it again


def openPage():
    page = url_combobox.get()  # Get url
    print(page)
    webbrowser.open_new(page)  # Open URL to webpage


def mainprogram():
    print(searchwords)
    print(keywords)
    lang = country_combobox.get()
    region = region_combobox.get()
    sensetivity = sen.get()
    depth = dep.get()
    results = res.get()
    global outputname
    outputname = name.get()
    scrape(searchwords, keywords, lang, region, outputname, sensetivity, depth, results)
    #scrapeprogram(searchwords, keywords, lang, region)
    #sortprogram(keywords, cl)
    global json_output
    json_output = loadJSON()
    displaywindow()


# Create the main window
root = tk.Tk()
root.title("Web Scraper GUI")

searchwords = []
keywords = []
# Searchword entry
tk.Label(root, text="Enter Search Word:").grid(row=0, column=0, padx=10, pady=10)
searchword = tk.Entry(root, width=40)
searchword.grid(row=0, column=1, padx=10, pady=10)
run_button = tk.Button(root, text="Add Search Word", command=addSearch)
run_button.grid(row=0, column=2, padx=10, pady=10)
# Keyword entry
tk.Label(root, text="Enter keyword:").grid(row=1, column=0, padx=10, pady=10)
keyword = tk.Entry(root, width=40)
keyword.grid(row=1, column=1, padx=10, pady=10)
run_button = tk.Button(root, text="Add keyword", command=addKeyword)
run_button.grid(row=1, column=2, padx=10, pady=10)

# Filter Dropdown
#.Label(root, text="Select Country:").grid(row=3, column=0, padx=10, pady=10)
#countrylist = tk.StringVar()
#filter_dropdown = ttk.Combobox(root, textvariable=countrylist)
#filter_dropdown['values'] = ("Austria", "Finland", "Portugal", "Czech Republic", "Greece", "Sweden")
#filter_dropdown.grid(row=3, column=1, padx=10, pady=10)

country_combobox = ttk.Combobox(root, values=("Austria", "Finland", "Portugal", "Czech Republic", "Greece", "Sweden"))
country_combobox.bind("<<ComboboxSelected>>", updateCountry)
country_combobox.grid(row=3, column=1, padx=10, pady=5)

# Create a combobox for Regions
region_combobox = ttk.Combobox(root, width=50)
region_combobox.bind("<<ComboboxSelected>>")
region_combobox.grid(row=4, column=1, padx=10, pady=5)

tk.Label(root, text="Enter name of file:").grid(row=5, column=0, padx=10, pady=10)
name = tk.Entry(root, width=40)
name.grid(row=5, column=1, padx=10, pady=10)

# Run Button
run_button = tk.Button(root, text="Run Program", command=mainprogram)
run_button.grid(row=6, column=1, pady=20)

# Output Text Box
searchparams = tk.Text(root, wrap=tk.WORD, width=75, height=15)
searchparams.grid(row=7, columnspan=4, padx=10, pady=10)
tk.Label(root, text="Settings:").grid(row=8, column=0, padx=10, pady=10)
tk.Label(root, text="Sensetivity:").grid(row=9, column=0, padx=10, pady=10)
sen = tk.Scale(root, from_=0, to=60, orient=tk.HORIZONTAL)
sen.grid(row=9, column=1, padx=10, pady=10)
sen.set(10)
tk.Label(root, text="Search depth:").grid(row=10, column=0, padx=10, pady=10)
dep = tk.Scale(root, from_=1, to=6, orient=tk.HORIZONTAL)
dep.grid(row=10, column=1, padx=10, pady=10)
dep.set(3)
tk.Label(root, text="Results per Searchterm:").grid(row=11, column=0, padx=10, pady=10)
res = tk.Scale(root, from_=1, to=10, orient=tk.HORIZONTAL)
res.grid(row=11, column=1, padx=10, pady=10)
res.set(7)

# Create the second window
def displaywindow():
    second_window = tk.Toplevel(root)
    second_window.title("URL Output Display")

    # Create a combobox for domains
    global domain_combobox, url_combobox, output_text
    domain_combobox = ttk.Combobox(second_window, values=list(json_output.keys()))
    domain_combobox.bind("<<ComboboxSelected>>", updateURL)

    # Create a combobox for URLs
    url_combobox = ttk.Combobox(second_window, width=50)
    url_combobox.bind("<<ComboboxSelected>>", updateText)
    # Create a frame for the text area and scrollbar
    frame = tk.Frame(second_window)

    frame.grid(row=2, column=0, padx=10, pady=10, columnspan=2)

    output_text = tk.Text(frame, wrap=tk.WORD, height=35, width=50)
    output_text.pack(side=tk.LEFT)

    # Create a scrollbar
    scrollbar = tk.Scrollbar(frame, command=output_text.yview)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    output_text.config(yscrollcommand=scrollbar.set)
    output_text.config(state=tk.DISABLED)  # Start with the text box disabled

    # Arrange widgets in a grid
    domain_combobox.grid(row=0, column=0, padx=10, pady=5)
    url_combobox.grid(row=1, column=0, padx=10, pady=5)
    websitebutton = tk.Button(second_window, text="Go to page", command=openPage)
    websitebutton.grid(row=1, column=1, columnspan=2)


# Start the GUI event loop
root.mainloop()
