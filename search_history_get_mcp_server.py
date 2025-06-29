from fastmcp import FastMCP
import sqlite3
import shutil
import os
import datetime

app = FastMCP(__name__)

@app.tool('/fetch_history')
def fetch_search_history_tools(profile_number):
 shutil.copy(f'/home/viraj/.config/google-chrome/Profile {profile_number}/History', '/home/viraj/history.db')

 conn = sqlite3.connect('/home/viraj/history.db')

 cursor = conn.cursor()

 cursor.execute(f"SELECT url,title,last_visit_time FROM urls")

 data = cursor.fetchall()
 search_history = ""

 for url, title, last_visit_time in data:
  date = datetime.datetime(1601, 1, 1) + datetime.timedelta(microseconds = last_visit_time)

  if date.strftime('%Y-%u-%d') == datetime.datetime.now().strftime('%Y-%u-%d'):
   if 'Google Search' not in title:
    search_history += f'url-{url}, title-{title}\n\n'
 
   else:
    search_history += f'title - {title}\n\n'

 os.remove('/home/viraj/history.db')
 
 return search_history

if __name__ == '__main__':
 app.run(transport = 'sse')