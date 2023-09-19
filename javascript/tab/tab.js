// 버튼0 을누르면 orange 클래스명 부착, div에 show 클래스명 부착. 기존 버튼의 것은 제거

var button = $(".tab-button");
var content = $(".tab-content");

// for (let i = 0; i < button.length; ++i) {
//     OpenTab(i);
// }

document.querySelector(".list").addEventListener("click", function(e) {
    OpenTab2(parseInt(e.target.dataset.id));
})

function OpenTab1(index) {
    button.eq(index).on("click", function() {
        button.removeClass("orange");
        button.eq(index).addClass("orange");
        content.removeClass("show");
        content.eq(index).addClass("show");
    })
}

function OpenTab2(index) {
    button.removeClass("orange");
    button.eq(index).addClass("orange");
    content.removeClass("show");
    content.eq(index).addClass("show");
}