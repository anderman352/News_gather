# -*- coding: utf-8 -*-
"""
Created on Tue May 28 14:58:42 2024

@author: david
"""

import requests
from bs4 import BeautifulSoup
import webbrowser

# Define a list of cybersecurity news sites
sites = [
    "https://krebsonsecurity.com",
    "https://www.darkreading.com",
    "https://www.securityweek.com",
    "https://www.bleepingcomputer.com",
    "https://www.zdnet.com/topic/security/"
]

# Prompt the user to select a site from the list
print("Select a site from the following list:")
for i, site in enumerate(sites, start=1):
    print(f"{i}. {site}")
choice = int(input("Enter your choice (1-5): ")) - 1

# Get the top ten news stories from the selected site
url = sites[choice]
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")

articles = []
for article in soup.find_all("article", limit=10):
    title = article.find("h2").text.strip()
    link = article.find("a")["href"]
    articles.append(f"<a href='{link}'>{title}</a><br>")

# Create an HTML file with the top ten news stories
html = "<html><body>"
html += "<h1>Top Ten News Stories</h1>"
html += "".join(articles)
html += "</body></html>"

# Save the HTML file
with open("news.html", "w", encoding="utf-8") as f:
    f.write(html)

# Open the HTML file in Firefox
webbrowser.get("firefox").open("news.html")