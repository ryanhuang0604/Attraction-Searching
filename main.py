import wikipedia
import googlemaps
from bs4 import BeautifulSoup
import urllib
import tkinter as tk


window = tk.Tk()
window.title("Traveasy GO！")
window.geometry("700x500")
label = tk.Label(window, text="請輸入旅遊景點： ", bg="#FFFF99", font=("Arial", 12))
label.pack()
e = tk.Entry(window)
e.pack()


def user_input():
	var = e.get()

	maps = googlemaps.Client(key="AIzaSyCA6E7RZK6PDBdv822exDtvRwVJkr0VIrw")
	wikipedia.set_lang("zh-tw")

	geo = maps.geocode(var)

	if geo == []:
		address = "無法搜尋"
	else:
		address = geo[0]["formatted_address"]
	try:
		wiki = wikipedia.page(var)
		summary = wiki.summary
	except:
		summary = "無法搜尋"
	try:
		url = "http://okgo.tw/Search.html?kw=" + urllib.parse.quote(var) + "&st=1"
		page = urllib.request.urlopen(url)
		soup = BeautifulSoup(page, "html.parser")
		url = "http://okgo.tw/" + soup.find("a", class_ = "STopic")["href"]
		page = urllib.request.urlopen(url)
		page = BeautifulSoup(page, "html.parser")
		traffic = page.find("div", id = "Buty_View_Traffic").get_text()
	except:
		traffic = "無法搜尋"

	t.insert("insert", var+"的旅遊資訊\n")
	t.insert("insert", "\n地址:\n{}\n".format(address))
	t.insert("insert", "\n簡介:\n{}\n".format(summary))
	t.insert("insert", "\n交通資訊:\n{}\n".format(traffic))
	t.insert("insert", "\n\n")


b1 = tk.Button(window, text="輸入", width=10, height=1, command=user_input)
b1.pack()
t = tk.Text(window, height=100)
t.pack()
window.mainloop()