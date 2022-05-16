
const div = document.getElementById('song_title');

function openForm(thisdiv) {
  document.getElementById("myForm").style.display = "flex";
  div.innerHTML = thisdiv.get();
}

function closeForm() {
  document.getElementById("myForm").style.display = "none";
}