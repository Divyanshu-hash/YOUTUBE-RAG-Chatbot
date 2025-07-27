async function getVideoId() {
  let [tab] = await chrome.tabs.query({ active: true, currentWindow: true });
  let url = new URL(tab.url);
  return url.searchParams.get("v");
}

document.getElementById("askBtn").addEventListener("click", async () => {
  const question = document.getElementById("question").value;
  const status = document.getElementById("status");
  const answerBox = document.getElementById("answer");

  answerBox.innerText = "";
  status.innerText = "⏳ Processing...";

  try {
    const videoId = await getVideoId();
    if (!videoId) throw new Error("Not a valid YouTube video.");

    // Extract transcript first
    await fetch("http://localhost:8000/extract", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ video_id: videoId })
    });

    // Ask the question
    const response = await fetch("http://localhost:8000/ask", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ video_id: videoId, question })
    });

    const data = await response.json();
    answerBox.innerText = data.answer || "⚠️ No answer returned.";
    status.innerText = "✅ Answer loaded";
  } catch (err) {
    answerBox.innerText = "";
    status.innerText = "❌ " + (err.message || "Something went wrong.");
  }
});
