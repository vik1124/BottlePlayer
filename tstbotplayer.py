 
audTemp ="""
 <audio id="audElement" controls class="media-object">
        <source src="./doc/%(fname)s" type="audio/mpeg" />
        <em>Sorry, your browser doesn't support HTML5 audio.</em>
 </audio>
 """
 
 
from bottle import Bottle,route, run, template, static_file,request,redirect
import os
from multiprocessing import Process
import time
#import android
#droid = android.Android()

temp='puriyavillai-hq.mp3'
hostip='192.168.2.4'
extip='98.235.224.147'
porty = 18080

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
	print temp
	#return template('playtest', AudioFile='/doc/'+temp)
	return template('playtest', AudioFile='http://'+extip+':'+str(porty)+'/mplay/'+temp,audList=getAudioList())
	
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
			if str.split(i,'.')[1] in ['mp3']:
				audlist.append(i)
	return audlist

run(app,host=hostip, port=porty, reloader=True, interval=0.5)