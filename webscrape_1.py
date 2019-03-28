from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uOpen

filename="pc_games2.csv"
file=open(filename,"w")
file.close()
file=open(filename,"a+")
headers="name,company,price,save\n"
file.write(headers)
for i in range(1,11):
	myUrl='https://www.newegg.com/Product/ProductList.aspx?Submit=ENE&N=100007756&IsNodeId=1&Description=pc%20games&page={}&bop=And&PageSize=36&order=BESTMATCH'.format(i)
	Client=uOpen(myUrl)
	page=Client.read()
	Client.close()
	html_page=soup(page,"html.parser")
	containers=html_page.findAll("div",{"class":"item-container"})

	
	

	for container in containers:
		name=container.a.img["title"]
		b=(container.find("div","item-action").ul.li.text).strip()
		old_price=b[0:6]
		c=(container.find("div","item-action").ul).find("li","price-current").text.strip()
		new_price=c[0:6]
		#save=(container.find("div","item-action").ul).find("li","price-save").find("span","price-save-percent").text.strip()
		print("\n")
		print("name          "+name)
		try:
			company=container.find("div","item-info").img["title"]
		except:
			company=" "


		print("company       "+company)
		
		#print("old_price     "+old_price)
		if(new_price[0]!='$'):
			new_price=str("  "+new_price[2:5])

		print("price     "+new_price)
		
		try:
			save=(container.find("div","item-action").ul).find("li","price-save").find("span","price-save-percent").text.strip()
		except:
			save="0%"
		else:
			print("save          "+save)
		if not old_price:
				old_price=new_price
		
		
		file.write(name.replace(",","")+","+company+","+new_price+","+save+"\n")
	file.write("\n\n\n"+"page "+str(i+1))

file.close()