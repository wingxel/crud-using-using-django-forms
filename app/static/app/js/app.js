"use strict";

$(function() {
    $("#navbarSupportedContent").on("show.bs.collapse", () =>
        $("a.nav-link").click(() => $("#navbarSupportedContent").collapse("hide"))
    );
});