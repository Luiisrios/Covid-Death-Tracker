import requests
import bs4

import tkinter as tk

# scrapping from web
def get_html_data(url):
    data = requests.get(url)
    return data

#get requested url
def get_covid_data():
    url = "https://www.worldometers.info/coronavirus/"
    #get the html data
    html_data = get_html_data(url)
    bs = bs4.BeautifulSoup(html_data.text, 'html.parser')
    #find the data
    info_div = bs.find("div", class_ ="content-inner") .findAll("div", id="maincounter-wrap")
    all_data=""
   
   #search block for each covid cases
    for block in info_div:
        text = block.find("h1", class_=None).get_text() #coivd cases
        count = block.find("span", class_=None).get_text() #amount from web
        all_data = all_data + text + " " + count + "\n"
       
    
    return all_data




#reload for the button
def reload():
    new_data = get_covid_data()
    mainlabel['text']=new_data



get_covid_data()

#for gui
root = tk.Tk()
root.geometry("900x700")
root.title("Luis Covid Tracker")
f = ("poppins", 25, 'bold')

#banner image
banner = tk.PhotoImage(file="")
bannerlabel = tk.Label(root, image=banner)
bannerlabel.pack()

#show data
mainlabel = tk.Label(root, text=get_covid_data(), font=f)
mainlabel.pack()



#button form reloaad
rbtn = tk.Button(root,text="Reload", font=f, relief="solid", command=reload)
rbtn.pack()

root.mainloop()