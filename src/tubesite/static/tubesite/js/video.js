/**
 * Created by IT on 2017/7/24.
 */

console.log("video.js 0");

(function () {

    console.log("video.js 1");

    function pageLoad() {
        var player = videojs("video-player");
        var $player = $("#video-player");
        var video_model = JSON.parse($player.attr("data-model"));
        console.log(video_model);
        console.log(video_model.poster);
        console.log(video_model.src);
        player.poster(video_model.poster);
        player.src(video_model.src);
        console.log("video.js 4");
    }


    $(function () {
        console.log("video.js 3");
        pageLoad();
    });

})();

console.log("video.js 2");
console.log($);