<!DOCTYPE HTML>
<html>
<head>
    <title>Vicky Stream</title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <!-- Bootstrap -->
    <link href="/css/bootstrap.css" rel="stylesheet">
</head>
<body>
    <div class="container">
        <h1 class="text-center">
            Vicky Stream !</h1>
        <br />
        <div class="media">
            <audio id="audElement" controls autoplay class="media-object">
				<source src="{{AudioFile}}" type="audio/mpeg" />
				<em>Sorry, your browser doesn't support HTML5 audio.</em>
			</audio>
			<div>
				<button onclick="document.getElementById('audElement').play()">Play</button>
				<button onclick="document.getElementById('audElement').pause()">Pause</button>
				<button onclick="document.getElementById('audElement').volume+=0.1">Volume Up</button>
				<button onclick="document.getElementById('audElement').volume-=0.1">Volume Down</button>
		</div> 
	    </div>
		<h3 class="text-left"> Global PlayList </h2>
		<form method="POST" action="./">
			% for item in audList:
					<input class="btn btn-link" name="filename" type="submit" value="{{item}}"/>
					<br/>
				% end
		</form>
		<br />
		<form method="POST" enctype="multipart/form-data" action="">
        <input id="inFile" type="file" value="Browse" name="upfile"/>
        <br />
	    <div class="btn-group">
           <input type="submit" class="btn btn-success" value="Play File">
        </div>
       </form>
    </div>
</body>
</html>
