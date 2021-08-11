// PASTE INTO THE CONSOLE IN THE PLAYLIST PAGE

(function() {
    let playlist = document.querySelectorAll("#contents"),
        timeSeconds = 0,
        timesContainer = null;

    for(let i = 0; i < playlist.length; i++){

        timesContainer = playlist[i].querySelectorAll(".style-scope ytd-thumbnail-overlay-time-status-renderer");

    }
    for(let i = 0; i < timesContainer.length; i++){
        let timeStr = timesContainer[i].innerText,
        timeParts = timeStr.split(":"),
        seconds = (timeParts[0] * 60) + parseInt(timeParts[1]);
        
        timeSeconds += seconds;
    }
    
    let hours = (timeSeconds / 60) / 60,
        minutes = (timeSeconds / 60) % 60,
        seconds = (timeSeconds % 60),
        result = parseInt(hours) + ":" + parseInt(minutes) + ":" + parseInt(seconds);
    
    alert(result);
    
    })();
