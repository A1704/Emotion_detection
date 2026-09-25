document.getElementById("runButton").addEventListener("click", async () => {
    const text = document.getElementById("textToAnalyze").value;
    const response = await fetch(
        `/emotionDetector?textToAnalyze=${encodeURIComponent(text)}`
    );
    document.getElementById("result").textContent = await response.text();
});
