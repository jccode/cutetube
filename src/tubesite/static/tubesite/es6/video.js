/**
 * Created by IT on 2017/7/24.
 */

function pageLoad() {
    const player = videojs("video-player"),
        $player = $("#video-player"),
        video_model = JSON.parse($player.attr("data-model"));
    player.poster(video_model.poster);
    if (video_model['extra']) {
        const extra = JSON.parse(video_model['extra']);
        const playlist = extra.videos.map(x => {
            return {
                poster: x.poster,
                sources: [ {src: x.src, type: videoType(x.src)} ]
            };
        });
        console.log(playlist);
        player.playlist(playlist);
        player.playlist.autoadvance(0);
        player.playlist.repeat(false);
    } else {
        player.src(video_model.src);
    }
}

function videoType(url) {
    let type;
    if (url.endsWith(".mp4")) {
        type = "video/mp4";
    } else if (url.endsWith(".flv")) {
        type = "video/x-flv";
    } else {
        type = "video/mp4";
    }
    return type;
}


// READY
$(function () {
    pageLoad();
});



