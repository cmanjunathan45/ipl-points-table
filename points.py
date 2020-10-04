from bs4 import BeautifulSoup
import numpy as np
import pandas as pd
import requests

page = requests.get("https://www.cricbuzz.com/cricket-series/3130/indian-premier-league-2020/points-table")

soup = BeautifulSoup(page.text,"lxml")
tbl = soup.find("table",class_="table cb-srs-pnts")
column_names = [x.get_text() for x in tbl.find_all('td',class_="cb-srs-pnts-th")]
column_names[5]='pts'
team_names = [x.get_text() for x in tbl.find_all('td',class_="cb-srs-pnts-name")]
pnt_table = [x.get_text() for x in tbl.find_all('td',class_="cb-srs-pnts-td")]
np_pnt_table = (np.array(pnt_table)).reshape(len(team_names),7)
np_pnt_table = np.delete(np_pnt_table,6,1)
np_pnt_table = np_pnt_table.astype(int)
consol_tbl = pd.DataFrame(np_pnt_table,index=team_names,columns=column_names)
consol_tbl.columns.name = "Teams"
print(consol_tbl)
