async function getVideoId() {
  let [tab] = await chrome.tabs.query({ active: true, currentWindow: true });
  let url = new URL(tab.url);
  return url.searchParams.get("v");
}

document.getElementById("askBtn").addEventListener("click", async () => {
  const videoId = await getVideoId();
  const question = document.getElementById("question").value;

  await fetch("http://localhost:8000/extract", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ video_id: videoId })
  });

  const response = await fetch("http://localhost:8000/ask", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ video_id: videoId, question })
  });
  const data = await response.json();
  document.getElementById("answer").innerText = data.answer;
});