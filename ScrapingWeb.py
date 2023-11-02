import requests
from bs4 import BeautifulSoup
import tkinter as tk
from tkinter import filedialog
import csv

# Function to perform web scraping and save data to CSV
def scrape_and_save():
    url = entry_url.get()
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    product_names = [item.text for item in soup.find_all('span', class_='product-name')]
    prices = [item.text for item in soup.find_all('span', class_='price')]
    ratings = [item.text for item in soup.find_all('span', class_='rating')]

    data = list(zip(product_names, prices, ratings))

    save_path = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV Files", "*.csv")])
    with open(save_path, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Product Name', 'Price', 'Rating'])
        writer.writerows(data)

# Create the GUI
root = tk.Tk()
root.title("E-commerce Web Scraper")

label_url = tk.Label(root, text="Enter E-commerce Website URL:")
label_url.pack()

entry_url = tk.Entry(root, width=50)
entry_url.pack()

button_scrape = tk.Button(root, text="Scrape and Save", command=scrape_and_save)
button_scrape.pack()

root.mainloop()
