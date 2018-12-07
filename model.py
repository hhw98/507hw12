
import json
from datetime import datetime

GUESTBOOK_ENTRIES_FILE = "entries.json"
entries = []
next_id = 0

def init():
    global entries
    try:
        f = open(GUESTBOOK_ENTRIES_FILE)
        entries = json.loads(f.read())
        f.close()
    except:
        entries = []

def get_entries():
    global entries
    return entries

def add_entry(name, text):
    global entries, GUESTBOOK_ENTRIES_FILE,next_id
    now = datetime.now()
    #time_string = now.strftime("%b %d, %Y %-I:%M %p")
    # if you have an error using this format, just use
    time_string = str(now)	
    entry = {"id":str(next_id), "author": name, "text": text, "timestamp": time_string}
    next_id = next_id+1
    entries.insert(0, entry) ## add to front of list	
    try:
        f = open(GUESTBOOK_ENTRIES_FILE, "w")
        dump_string = json.dumps(entries)
        f.write(dump_string)
        f.close()
    except:
        print("ERROR! Could not write entries to file.")
def delete_entry(id):
    global entries, GUESTBOOK_ENTRIES_FILE
    for ele in entries:
        if ele.get('id') == id:
            entries.remove(ele)	
        try:
            f = open(GUESTBOOK_ENTRIES_FILE, "w")
            dump_string = json.dumps(entries)
            f.write(dump_string)
            f.close()
        except:
            print("ERROR! Could not write entries to file.")	
def update_entry(id, text):
    global entries, GUESTBOOK_ENTRIES_FILE
    now = datetime.now()
    #time_string = now.strftime("%b %d, %Y %-I:%M %p")
    # if you have an error using this format, just use
    time_string = str(now)
    for ele in entries:
        if ele.get('id') == id:
            ele['text'] = text
            ele['timestamp'] = time_string			
        try:
            f = open(GUESTBOOK_ENTRIES_FILE, "w")
            dump_string = json.dumps(entries)
            f.write(dump_string)
            f.close()
        except:
            print("ERROR! Could not write entries to file.")	
