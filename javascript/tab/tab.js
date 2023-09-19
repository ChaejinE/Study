// 버튼0 을누르면 orange 클래스명 부착, div에 show 클래스명 부착. 기존 버튼의 것은 제거

var button = $(".tab-button");
var content = $(".tab-content");

for (let i = 0; i < button.length; ++i) {
    button.eq(i).on("click", function() {
        button.removeClass("orange");
        button.eq(i).addClass("orange");
        content.removeClass("show");
        content.eq(i).addClass("show");
    })
}