!function () {
    "use strict";
    let e = document.querySelector(".header-nav");
    var n = 0, t = 0;
    const s = {pinned: "header-nav-pinned", unpinned: "header-nav-unpinned"};

    function c() {
        50 <= window.scrollY ? e.classList.add("header-sticky-top") : e.classList.remove("header-sticky-top")
    }

    function i() {
        (t = window.pageYOffset) < n ? e.classList.contains(s.unpinned) && (e.classList.remove(s.unpinned), e.classList.add(s.pinned)) : n < t && 400 <= window.scrollY && (!e.classList.contains(s.pinned) && e.classList.contains(s.unpinned) || (e.classList.remove(s.pinned), e.classList.add(s.unpinned))), n = t
    }

    window.onload = function () {
        window.onscroll = function () {
            i(), c()
        }
    }, window.addEventListener("load", function () {
        Lightense(".content img"), window.onscroll = function () {
            i(), c()
        }
    }, !1), function () {

    }(), document.querySelector(".navbar-toggler").addEventListener("click", function (e) {
        this.classList.toggle("toggle-menu")
    })
}();