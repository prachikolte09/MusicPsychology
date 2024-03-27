document.addEventListener("DOMContentLoaded", function () {
    const heartbeatForm = document.getElementById("heartbeatForm");
    const songContainer = document.getElementById("songContainer");
    const playerContainer = document.getElementById("player");

    heartbeatForm.addEventListener("submit", async function (event) {
        event.preventDefault();
        const heartbeat = document.getElementById("heartbeat").value;
        const response = await fetch(`/shuffle_music?heartbeat=${heartbeat}`);
        const data = await response.json();
        songContainer.innerHTML = `<p>Shuffled Song: ${data.song}</p>`;
        const videoId = getVideoId(data.song);
        loadVideoPlayer(videoId);
    });

    function getVideoId(song) {
        // Extract video ID from YouTube URL
        const match = song.match(/(?:https?:\/\/)?(?:www\.)?(?:youtube\.com\/(?:[^\/\n\s]+\/\S+\/|(?:v|e(?:mbed)?)\/|\S*?[?&]v=)|youtu\.be\/)([a-zA-Z0-9_-]{11})/);
        if (match) {
            return match[1];
        }
        return null;
    }

    function loadVideoPlayer(videoId) {
        if (videoId) {
            const iframe = document.createElement("iframe");
            iframe.setAttribute("width", "560");
            iframe.setAttribute("height", "315");
            iframe.setAttribute("src", `https://www.youtube.com/embed/${videoId}?autoplay=1`);
            iframe.setAttribute("frameborder", "0");
            iframe.setAttribute("allow", "accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture");
            playerContainer.innerHTML = "";
            playerContainer.appendChild(iframe);
        } else {
            playerContainer.innerHTML = "<p>No video available</p>";
        }
    }
});
