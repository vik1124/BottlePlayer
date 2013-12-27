audTemp ="""
 <audio id="audElement" controls class="media-object">
        <source src="./doc/%(fname)s" type="audio/mpeg" />
        <em>Sorry, your browser doesn't support HTML5 audio.</em>
 </audio>
 """
 
from bottle import Bottle,route, run, template, static_file,request,redirect
import os,sched,time
from multiprocessing import Process
from mutagen.mp3 import MP3
from mutagen.easyid3 import EasyID3
import socket
import webbrowser
#import android
#droid = android.Android()

sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sock.connect(("gmail.com",80))
hostip= sock.getsockname()[0]
sock.close()
print "hostip:",hostip

temp='puriyavillai-hq.mp3'
extip='98.235.224.147'
porty = 18080
timeset = 0
currtime = 0.0
starttime = 0.0
audtime = 0.0

app = Bottle()

def showurl(url="http://localhost:18080"):
	time.sleep(5)
	droid.webViewShow(url)

@app.route('/css/<scriptname>')
def getScript(scriptname):
	return static_file(scriptname, root='./css/')

@app.route('/')
def home_page():
	global temp
	global hostip
	global extip
	global timeset
	print temp
	timeset= readTime()
	return template('playtest', AudioFile='http://'+hostip+':'+str(porty)+'/mplay/'+temp,audList=getAudioList(), time_set = timeset, playList = GenPlayList())
	
@app.route('/mplay/<fname>')
def play_file(fname):
	print fname
	return static_file( fname, root='./doc/')
	
@app.route('/', method='POST')
def do_upload():
	global temp
	print "Post hit !"
	upload = request.files.get('upfile')
	if upload != None:
		name, ext = os.path.splitext(upload.filename)
		print upload.raw_filename
		print name,ext
		if not os.path.exists('./doc/'+upload.filename):
			upload.save('./doc/'+upload.filename) # appends upload.filename automatically
		temp = upload.filename
	elif request.forms.get('filename')!=None:
		temp = request.forms.get('filename')
	redirect('/')

def getAudioList():
	list = os.listdir('./doc/')
	audlist=[]
	for i in list:
		if not os.path.isdir(i):
			temp = str.split(i,'.')
			if temp[len(temp)-1] in ['mp3']:
				audlist.append(i)
	return audlist
	
def GenPlayList():
	global hostip,porty
	list = os.listdir('./doc/')
	audlist=""
	for i in list:
		if not os.path.isdir(i):
			temp = str.split(i,'.')
			if temp[len(temp)-1] in ['mp3']:
				audlist=audlist +'"http://'+hostip+':'+str(porty)+'/mplay/'+i+'",'
	return audlist[:-1]
	
def readTime():
	global temp
	f = open('timeset.txt','rb')
	temp = f.readline().rstrip()
	val = float(f.readline())
	f.close()
	return val

if __name__ == "__main__" :
	webbrowser.open_new_tab('http://'+hostip+':'+str(porty))
	run(app,host=hostip, port=porty)
	print "app running !"