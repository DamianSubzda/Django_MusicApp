let elTitle = document.getElementById("song-title");
let elMp3_audio = document.getElementById("src-song-audio");
let elBackground = document.getElementById("logo-background");
let elMp3_download = document.getElementById("download_song");
let elPlaylistadd = document.getElementById("form-temp"); // ID song 2 popup
//let elPlaylistadd2 = document.getElementById("form-temp2");
let elnr = document.getElementById("nr-temp"); // ID song 1 popup
let elplaylist = document.getElementsByClassName("playlist_add");


function openForm(nr) {
  audio.src = '/musics/' + Mp3[nr-1];
  elTitle.innerHTML = Title[nr-1];
  elBackground.style.backgroundImage = "url(" + Image[nr-1]+ ")";
  elMp3_download.href = '/musics/' + Mp3[nr-1];
  elnr.innerHTML = nr;
  document.getElementById("myForm").style.display = "flex";
}

function closeForm() {
  document.getElementById("myForm").style.display = "none";
  document.getElementById("myForm2").style.display = "none";
  audio.pause();
}


function openForm2(nr) {
  elPlaylistadd.innerHTML = elnr.innerHTML;
  for(var i = 0; i < elplaylist.length; i++)
  {
    var splitURL = elplaylist[i].toString().split("/");
    if(splitURL[splitURL.length - 1]===''){
      elplaylist[i].href = elplaylist[i].href + elnr.innerHTML
    }else{
      splitURL.pop();
      elplaylist[i].href = splitURL.join("/");
      elplaylist[i].href = elplaylist[i].href +"/" +elnr.innerHTML
    }
    console.log(elplaylist[i].href);
  }
  document.getElementById("myForm2").style.display = "flex";
}

function closeForm2() {
  document.getElementById("myForm2").style.display = "none";
}



const audioPlayer = document.querySelector(".audio-player");
const audio = new Audio(
  '/musics/' + Mp3[0]
);


console.dir(audio);

audio.addEventListener(
  "loadeddata",
  () => {
    audioPlayer.querySelector(".time .length").textContent = getTimeCodeFromNum(
      audio.duration
    );
    audio.volume = .75;
  },
  false
);

//click on timeline to skip around
const timeline = audioPlayer.querySelector(".timeline");
timeline.addEventListener("click", e => {
  const timelineWidth = window.getComputedStyle(timeline).width;
  const timeToSeek = e.offsetX / parseInt(timelineWidth) * audio.duration;
  audio.currentTime = timeToSeek;
}, false);

//click volume slider to change volume
const volumeSlider = audioPlayer.querySelector(".controls .volume-slider");
volumeSlider.addEventListener('click', e => {
  const sliderWidth = window.getComputedStyle(volumeSlider).width;
  const newVolume = e.offsetX / parseInt(sliderWidth);
  audio.volume = newVolume;
  audioPlayer.querySelector(".controls .volume-percentage").style.width = newVolume * 100 + '%';
}, false)

//check audio percentage and update time accordingly
setInterval(() => {
  const progressBar = audioPlayer.querySelector(".progress");
  progressBar.style.width = audio.currentTime / audio.duration * 100 + "%";
  audioPlayer.querySelector(".time .current").textContent = getTimeCodeFromNum(
    audio.currentTime
  );
}, 500);

//toggle between playing and pausing on button click
const playBtn = audioPlayer.querySelector(".controls .icono-play");
playBtn.addEventListener(
  "click",
  () => {
    if (audio.paused) {
      playBtn.classList.remove("play");
      playBtn.classList.add("pause");
      audio.play();
    } else {
      playBtn.classList.remove("pause");
      playBtn.classList.add("play");
      audio.pause();
    }
  },
  false
);

audioPlayer.querySelector(".volume-button").addEventListener("click", () => {
  const volumeEl = audioPlayer.querySelector(".volume-container .volume");
  audio.muted = !audio.muted;
  if (audio.muted) {
    volumeEl.classList.remove("icono-volumeMedium");
    volumeEl.classList.add("icono-volumeMute");
  } else {
    volumeEl.classList.add("icono-volumeMedium");
    volumeEl.classList.remove("icono-volumeMute");
  }
});

//turn 128 seconds into 2:08
function getTimeCodeFromNum(num) {
  let seconds = parseInt(num);
  let minutes = parseInt(seconds / 60);
  seconds -= minutes * 60;
  const hours = parseInt(minutes / 60);
  minutes -= hours * 60;

  if (hours === 0) return `${minutes}:${String(seconds % 60).padStart(2, 0)}`;
  return `${String(hours).padStart(2, 0)}:${minutes}:${String(
    seconds % 60
  ).padStart(2, 0)}`;
}

