async function searchJobs() {
  let res = await fetch("https://YOUR-RENDER-URL/jobs");
  let data = await res.json();
  document.getElementById("jobs").innerHTML =
    data.map(j => `<p>${j.title} - ${j.location}</p>`).join("");
}
