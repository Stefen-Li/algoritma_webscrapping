from flask import Flask, render_template 
import pandas as pd
import requests
from bs4 import BeautifulSoup 
from io import BytesIO
import base64
import matplotlib.pyplot as plt

app = Flask(__name__)

def scrap(url):
    #This is fuction for scrapping
    url_get = requests.get(url)
    soup = BeautifulSoup(url_get.content,"html.parser")
    
    #Find the key to get the information
    table = soup.find('table', attrs={'class':'centerText newsTable2'}) 
    tr = table.find_all('tr') 

    temp = [] #initiating a tuple

    for i in range(1, len(tr)):
        row = table.find_all('tr')[i]
        #use the key to take information here
        #name_of_object = row.find_all(...)[0].text
        Tanggal = row.find_all('td')[0].text.replace('\xa0',' ')
        Tanggal = Tanggal.strip()
    
        KursJual = row.find_all('td')[1].text
        KursJual = KursJual.strip()
    
        KursBeli = row.find_all('td')[2].text
        KursBeli = KursBeli.strip()






        temp.append((Tanggal,KursJual,KursBeli)) #append the needed information 
    
    temp = temp[::-1] #remove the header

    df = pd.DataFrame(temp, columns = ('Tanggal','KursJual','KursBeli')) #creating the dataframe
   #data wranggling -  try to change the data type to right data type
    list_indo = ['Januari','Februari','Maret','April','Mei','Juni','Juli','Agustus','September','Oktober','November','Desember']
    list_ing = ['January','February','March','April','May','June','July','August','September','October','November','December']

    df['Tanggal'] = df['Tanggal'].replace(list_indo,list_ing,regex=True)
    df['KursJual'] = df['KursJual'].replace(",",".",regex=True)
    df['KursBeli'] = df['KursBeli'].replace(",",".",regex=True)    

    df['Tanggal'] = pd.to_datetime(df['Tanggal'],dayfirst=True)
    df['KursJual'] = df['KursJual'].astype('float64')
    df['KursBeli'] = df['KursBeli'].astype('float64')
    df['Bulan'] = df['Tanggal'].dt.to_period('M')
    df = df.groupby('Bulan').mean()
   #end of data wranggling

    return df

@app.route("/")
def index():
    df = scrap('https://monexnews.com/kurs-valuta-asing.htm?kurs=JPY&searchdatefrom=01-01-2019&searchdateto=31-12-2019') #insert url here

    #This part for rendering matplotlib
    fig = plt.figure(figsize=(5,2),dpi=300)
    df.plot()
    
    #Do not change this part
    plt.savefig('plot1',bbox_inches="tight") 
    figfile = BytesIO()
    plt.savefig(figfile, format='png')
    figfile.seek(0)
    figdata_png = base64.b64encode(figfile.getvalue())
    result = str(figdata_png)[2:-1]
    #This part for rendering matplotlib

    #this is for rendering the table
    df = df.to_html(classes=["table table-bordered table-striped table-dark table-condensed"])

    return render_template("index.html", table=df, result=result)


if __name__ == "__main__": 
    app.run()
