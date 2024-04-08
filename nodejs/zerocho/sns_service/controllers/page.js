exports.renderProfile = (req, res, next) => {
    res.render("profile", { title: "내 정보 - NodeBird" });
};

exports.renderJoin = (req, res, next) => {
    res.render("join", { title: "회원 가입 - NodeBird"});
}

exports.renderMain = (req, res, next) => {
    res.render("main", {
        title: "NodeBird",
        twits: [],
    });
}

// Trend Develop Workflow : Router -> Controller -> Service(Request or Response)