document.addEventListener('DOMContentLoaded', doFirst, false)

function updatePageContent(page_type){
	alert(page_type);
	$.ajax({
		if(page_type == 'song'){
			url: '#!/song=' + slug,
			//section.innerHTML = '<h3>{{ song }}</h3>';
		}
		else if(page_type == 'playlist'){
			url: '#!/playlist=' + slug,
			//section.innerHTML = '<h3>{{ playlist }}</h3><ol>{% for song in songs %}<li><a href="#!/?song={{ song }}">{{ song }}</a></li>{% endfor %}</ol>';
		}
		else{
			//section.innerHTML = '<h3>All Songs</h3><ol>{% for song in songs %}li><a href="#!/?song={{ song.slug }}">{{ song }}</a></li>{% endfor %}</ol><a href="#!/upload-song/"><input type="button" class="btn" value="Upload Song"></a>';
		}
		success: function(data) {
			$('#music-section').html(data);
		}
	});
}

function getPageType(){
	url_song = getUrlVars()['song'];
	url_playlist = getUrlVars()['playlist'];
	if(url_song != undefined){
		page_type = 'song';
	}else if(url_playlist != undefined){
		page_type = 'playlist';
	}
	window.clearInterval(updatingPage);
	updatePageContent(page_type);
}

function updatePage(){
	href = this.href.toString();
	alert(href);
	
	updatingPage = setInterval(getPageType, 500);
}

function playOrPause(){
	/*if(!audio.paused && !audio.ended){
		audio.pause();
		play_btn.innerHTML='Play';
		window.clearInterval(updateBar);
	}else{
		audio.play();
		play_btn.innerHTML('Pause');
		updateBar = setInterval(Update, 500);
	}*/
	if(audio.paused || audio.ended){
		audio.play();
		play_btn.innerHTML='Pause';
		updateBar = setInterval(update, 500);
	}else{
		audio.pause();
		play_btn.innerHTML='Play';
		window.clearInterval(updateBar);
	}
}

function formatTime(seconds) {
    minutes = Math.floor(seconds / 60);
    minutes = (minutes >= 10) ? minutes : "" + minutes;
    seconds = Math.floor(seconds % 60);
    seconds = (seconds >= 10) ? seconds : "0" + seconds;
    return minutes + ":" + seconds;
}
function createSeeker(){
	dur = audio.duration;
	seekbar.min = audio.startTime;
	seekbar.max = dur
	seekbar.value = seekbar.min;
}

function seekaudio() {
	audio.currentTime = seekbar.value;
}

function update(){
	time = audio.currentTime;
	dur = audio.duration;
	elapsed_time.innerHTML = formatTime(time);
	song_dur.innerHTML = formatTime(dur);
	bar_width = (time/dur)*220;
	elapsed.style.width = bar_width.toString() + 'px';
	
	scrubber.style.left = Math.round(width=(bar_width-6)).toString() + 'px';
	seekbar.min = audio.startTime;
	seekbar.max = dur
	seekbar.value = time;
}

function loadSong(){

}

function next(){
	alert('Next!');
}

function previous(){
	if(audio.currentTime != 0 || audio.currentTime!=1){
		audio.currentTime = 0;
		audio.play();
		updateBar = setInterval(Update, 500);
	}else{
		
	}
}

function clickedBar(){
	
}

function doFirst(){
	url_song = getUrlVars()['song'];
	url_playlist = getUrlVars()['playlist'];
	page_type = null;
	
	
	audio = document.getElementById('song');
	
	section = document.getElementById('section');
	play_btn = document.getElementById('play');
	next_btn = document.getElementById('next');
	prev_btn = document.getElementById('previous');
	elapsed = document.getElementById('elapsed');
	scrubber = document.getElementById('scrubber');
	elapsed_time = document.getElementById('elapsed-time');
	song_dur = document.getElementById('song-dur');
	prog_bar = document.getElementById('progress-bar');
	seekbar = document.getElementById('seekbar');
	
	links = document.getElementsByTagName('a');
	for(i=0; i < links.length; i++){
		links[i].addEventListener('click', updatePage, false);
	}
	play_btn.addEventListener('click', playOrPause, false);
	next_btn.addEventListener('click', next, false);
	prev_btn.addEventListener('click', previous, false);
	elapsed.addEventListener('click', clickedBar, false);
	seekbar.addEventListener('change', seekaudio, false);
	
	createSeeker();
	getPageType();
}
