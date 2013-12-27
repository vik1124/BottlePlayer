import os,sched,time
from mutagen.mp3 import MP3
from mutagen.easyid3 import EasyID3
import sqlite3


temp='puriyavillai-hq.mp3'
#temp='3rds.mp3'
timeset = 0
currtime = 0.0
starttime = 0.0
audtime = 0.0

conn = sqlite3.connect('PyPlayer.db')

def settime():
	global temp,timeset,currtime,starttime,audtime
	currtime = time.time()-starttime
	if currtime>audtime:
		list = getAudioList()
		i = list.index(temp)
		if i == (len(list) - 1):
			i = 0
		else:
			i = i+1
		temp = list[i]
		print temp
		currtime = 0.0
		starttime = time.time()
		m = MP3('./doc/'+temp)
		audtime = m.info.length
		print audtime
	timeset = currtime
	storeTime(timeset)
	#print timeset
	s.enter(1,1,settime,())
	
def SQLsettime():
	global temp,timeset,currtime,starttime,audtime
	currtime = time.time()-starttime
	if currtime>audtime:
		list = getAudioList()
		i = list.index(temp)
		if i == (len(list) - 1):
			i = 0
		else:
			i = i+1
		temp = list[i]
		print temp
		currtime = 0.0
		starttime = time.time()
		m = MP3('./doc/'+temp)
		audtime = m.info.length
		print audtime
	timeset = currtime
	SQLstoreTime(timeset)
	print timeset
	s.enter(1,1,SQLsettime,())	

def getAudioList():
	list = os.listdir('./doc/')
	audlist=[]
	for i in list:
		if not os.path.isdir(i):
			temp = str.split(i,'.')
			if temp[len(temp)-1] in ['mp3']:
				audlist.append(i)
	return audlist
	
def storeTime(val):
	global temp
	f = open('timeset.txt','wb')
	f.write(temp+'\n')
	f.write(str(val))
	f.close()
	
def readTime():
	global temp
	f = open('timeset.txt','rb')
	temp = f.readline().rstrip()
	val = float(f.readline())
	f.close()
	return val
	
def SQLstoreTime(val):
	global temp
	#conn = sqlite3.connect('PyPlayer.db')
	c = conn.cursor()
	stmt = " update timeset set fname=?,currtime=? where ID = 1"
	c.execute(stmt,(temp,val))
	conn.commit()
	#conn.close()
	
def SQLreadTime():
	global temp
	#conn = sqlite3.connect('PyPlayer.db')
	c = conn.cursor()
	stmt = "select * from timeset where ID=1"
	a = c.execute(stmt)
	tup = a.fetchall()
	temp = tup[0][1]
	val = tup[0][2]
	#conn.close()
	return val
	
def dbinit():
	global temp
	#conn = sqlite3.connect('PyPlayer.db')
	c = conn.cursor()
	stmt = " create table if not exists timeset( ID INTEGER PRIMARY KEY ASC, fname varchar, currtime real)"
	c.execute(stmt)
	conn.commit()
	a = c.execute("Select * from timeset")
	b = a.fetchall()
	if len(b) == 0:
		c.execute("insert into timeset values(?,?,?)",(None,temp,0.0))
		conn.commit()
	#conn.close()
	

if __name__ == "__main__" :
	m = MP3('./doc/'+temp)
	audtime = m.info.length
	dbinit()
	print "Running..."
	#SQLstoreTime(0.0)
	storeTime(0.0)
	s = sched.scheduler(time.time,time.sleep)
	starttime = time.time()
	#s.enter(1,1,SQLsettime,())
	s.enter(1,1,settime,())
	s.run()
