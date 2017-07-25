

var body = $("body"),
    htmlBody = $("html, body"),
    overlay = $(".overlay"),
    header = $(".header"),
    $mobileMenu = $(".mobile-menu"),
    searchOpen = $(".search-open"),
    headerSearch = $(".header .search"),
    navItemDropdown = $(".header__nav-item--dropdown"),
    lngDropDown = $(".lng-dropdown"),
    menuClose = $(".menu-close"),
    menuOpen = $(".menu-open"),
    pat = /^https?:\/\//i,
    contentAjax = $("#content-ajax"),
    searchClose = $(".search-close");

var lazyloadSettings = {
    load: function (left, settings) {
        var $this = $(this);
        /*
        if(!($this.hasClass("lazy-bg-img") || $this.hasClass("lazy-img"))) {
            $this = $this.parent();
        }
        */
        if(this.tagName == 'IMG') {
            $this = $this.parent();
        }
        $this.addClass("image-loaded");
    }
};


$(window).on("load", function() {
    initScripts();
    headerNavDropdown();
    headerLangDropdown();
    search();
    mobileMenu();
    mobileMenuMaxHeight();
    body.css("opacity", 1);
});

/*
body.on("click", ".js-ajax-link", function(e) {
    if (pat.test(window.location.href)) {
        e.preventDefault();
        if ($(this).hasClass("mobile-ajax-off") && window.innerWidth >= 1133 || !$(this).hasClass("mobile-ajax-off")) {
            contentAjax.addClass("is-loading");
            setTimeout(function() {
                htmlBody.animate({
                    scrollTop: 0
                }, 0)
            }, 300);
            var t = $(this).attr("href");
            window.innerWidth < 1133 && mobileMenuClose();
            $.ajax({
                url: t,
                processData: !0,
                dataType: "html",
                success: function(e) {
                    document.title = $(e).filter("title").text(), void 0 !== history.pushState && history.pushState(e, "Page", t);
                    var i = $("#content-ajax");
                    setTimeout(function() {
                        i.html(" ");
                        i.html($(e).find("#content-ajax").html());
                        initScripts();
                        contentAjax.removeClass("is-loading");
                        body.css("opacity", 1);
                    }, 100)
                },
                error: function(e) {
                    return !0
                }
            })
        }
    } else {
        e.preventDefault();
        body.css("opacity", 0);
        var i = $(this).attr("href");
        setTimeout(function() {
            window.location.href = i;
        }, 200)
    }
});
*/

window.onpopstate = function(e) {
    pat.test(window.location.href) && (contentAjax.addClass("is-loading"), setTimeout(function() {
        htmlBody.animate({
            scrollTop: 0
        }, 0)
    }, 300),
    $.ajax({
        url: document.location,
        processData: !0,
        dataType: "html",
        success: function(e) {
            document.title = $(e).filter("title").text();
            var t = $("#content-ajax");
            setTimeout(function() {
                t.html(" "), t.html($(e).find("#content-ajax").html()), initScripts(), contentAjax.removeClass("is-loading"), body.css("opacity", 1)
            }, 100)
        }
    }));
};

/*
body.on("click", ".tabs__link", function(e) {
    var t = $("#tabs-content");
    if (pat.test(window.location.href)) {
        e.preventDefault(), $(this).parent().siblings("li").removeClass("is-active"), $(this).parent().addClass("is-active"), t.addClass("is-loading");
        var i = $(this).attr("href");
        $.ajax({
            url: i,
            processData: !0,
            dataType: "html",
            success: function(e) {
                var i = $("#tabs-content");
                setTimeout(function() {
                    i.html(" "), i.html($(e).find("#tabs-content").html()), t.removeClass("is-loading"), lazyload(), sr.sync(), body.css("opacity", 1)
                }, 200)
            }
        })
    }
});
*/


function breakpoint() {
    var e = $(".header__nav"),
        t = $(".header__nav-dropdown");
    Breakpoints({
        mobileMenu: {
            min: 0,
            max: 1132
        }
    }), Breakpoints.is("mobileMenu"), Breakpoints.get("mobileMenu").on({
        enter: function() {
            e.appendTo(".mobile-menu__scroll-content"), headerSearch.appendTo(".mobile-menu__scroll-content"), header.removeClass("search-opened"), headerSearch.stop().fadeOut(300), overlay.removeClass("is-fade"), searchClose.stop().fadeOut(300), searchOpen.stop().fadeIn(300)
        },
        leave: function() {
            e.appendTo(".header__left"), headerSearch.insertAfter(".header__right"), navItemDropdown.removeClass("is-active"), t.stop().fadeOut(300), mobileMenuClose()
        }
    })
}

function lazyload() {
    $(".lazy-bg-img").lazyload(lazyloadSettings);
    $(".lazy-img img").lazyload(lazyloadSettings);
}

function scrollRevealInit() {
    var e = $(".scrollAnimateHeader");
    window.sr = ScrollReveal(), $(".scrollAnimateBottomFade").length && sr.reveal(".scrollAnimateBottomFade", {
        duration: 1e3,
        mobile: !1,
        distance: "15px",
        origin: "bottom",
        scale: 1,
        viewFactor: 1e-14,
        viewOffset: {
            bottom: 50
        }
    }), $(".scrollAnimateFade").length && sr.reveal(".scrollAnimateFade", {
        duration: 1e3,
        mobile: !1,
        distance: "0px",
        origin: "bottom",
        scale: 1,
        viewFactor: 1e-14,
        viewOffset: {
            bottom: 50
        }
    }), e.length && "hidden" == e.css("visibility") && sr.reveal(".scrollAnimateHeader", {
        duration: 1e3,
        mobile: !1,
        distance: "0px",
        origin: "bottom",
        scale: 1,
        viewFactor: 1e-14,
        viewOffset: {
            bottom: 50
        }
    }), $(".scrollAnimateHeroSlider").length && sr.reveal(".scrollAnimateHeroSlider", {
        duration: 1e3,
        delay: 0,
        mobile: !1,
        distance: "0px",
        origin: "bottom",
        scale: 1,
        viewFactor: 1e-14,
        viewOffset: {
            bottom: 50
        }
    })
}

function headerNavDropdown() {
    navItemDropdown.on({
        mouseenter: function() {
            window.innerWidth >= 1133 && (overlay.addClass("is-fade"), $(this).addClass("is-active").find(".header__nav-dropdown").stop().fadeIn(300), lngDropDown.removeClass("open"))
        },
        mouseleave: function() {
            window.innerWidth >= 1133 && (overlay.removeClass("is-fade"), $(this).removeClass("is-active").find(".header__nav-dropdown").stop().fadeOut(300))
        }
    }), navItemDropdown.on("click", function(e) {
        setTimeout(function() {
            navItemDropdown.trigger("mouseleave")
        }, 50)
    }), $(".header__nav-item--dropdown > a").on("click", function(e) {
        if (window.innerWidth <= 1132) {
            e.preventDefault();
            var t = $(this).parent();
            navItemDropdown.not(t).removeClass("is-active"), navItemDropdown.not(t).find(".header__nav-dropdown").stop().slideUp(300), t.toggleClass("is-active"), t.find(".header__nav-dropdown").stop().slideToggle(300)
        }
    }), $(".header__nav-sub-dropdown > a").on("click", function(e) {
        window.innerWidth < 1133 && (e.preventDefault(), $(this).parent().toggleClass("is-active"), $(this).parent().find(">ul").stop().slideToggle(300))
    })
}

function headerLangDropdown() {
    lngDropDown.on("show.bs.dropdown", function() {
        overlay.addClass("is-fade")
    }), lngDropDown.on("hide.bs.dropdown", function() {
        header.hasClass("search-opened") || overlay.removeClass("is-fade")
    })
}

function search() {
    searchOpen.on("click", function(e) {
        e.preventDefault(), header.addClass("search-opened"), overlay.addClass("is-fade"), headerSearch.stop().fadeIn(300), searchClose.stop().fadeIn(300), searchOpen.stop().fadeOut(300), $(".header .search__field").focus()
    }), searchClose.on("click", function(e) {
        e.preventDefault(), header.removeClass("search-opened"), headerSearch.stop().fadeOut(300), overlay.removeClass("is-fade"), searchClose.stop().fadeOut(300), searchOpen.stop().fadeIn(300)
    }), $(document).on("click", function(e) {
        window.innerWidth >= 1133 && ($(e.target).closest(".search, .search-open, .search-close, .search__quick-links").length || (header.hasClass("search-opened") && overlay.removeClass("is-fade"), header.removeClass("search-opened"), headerSearch.stop().fadeOut(300), searchClose.stop().fadeOut(300), searchOpen.stop().fadeIn(300)))
    })
}

function mobileMenuClose() {
    body.removeClass("mobile-menu-opened"), menuClose.stop().hide(), menuOpen.stop().show(), $mobileMenu.stop().fadeOut(300), overlay.removeClass("is-fade")
}

function mobileMenu() {
    menuOpen.on("click", function(e) {
        e.preventDefault(), $(this).hide(), body.addClass("mobile-menu-opened"), menuClose.show(), $mobileMenu.css("max-height", $(window).outerHeight() - header.outerHeight()), $mobileMenu.stop().fadeIn(300), overlay.addClass("is-fade")
    }), menuClose.on("click", function(e) {
        e.preventDefault(), mobileMenuClose()
    }), $(document).on("click", function(e) {
        $(e.target).closest(".mobile-menu, .menu-open, .menu-close").length || (body.hasClass("mobile-menu-opened") && overlay.removeClass("is-fade"), overlay.removeClass("mobile-menu-opened"), $mobileMenu.stop().fadeOut(300), menuClose.hide(), menuOpen.show())
    })
}

function mobileMenuMaxHeight() {
    $mobileMenu.css("max-height", $(window).outerHeight() - header.outerHeight()), $(window).on("resize", function() {
        $mobileMenu.css("max-height", $(window).outerHeight() - header.outerHeight())
    })
}

function mobileMenuOverflowScroll() {
    isMobile.any() ? $mobileMenu.css("overflow", "auto") : $mobileMenu.on("mousewheel", function(e) {
        e.preventDefault();
        var t = $(".mobile-menu__scroll-content"),
            i = $(this),
            n = t.outerHeight(),
            o = parseInt(i.css("max-height")),
            s = parseInt(t.css("top")),
            r = o - n,
            a = e.deltaY;
        n > o && (a < 0 ? s + a > r ? t.css("top", s + a) : t.css("top", r) : s + a < 0 ? t.css("top", s + a) : t.css("top", 0))
    })
}

function heroSlider() {
    var e = $(".hero-slider");
    e.each(function(e, t) {
        var i = $(this).parents(".hero-slider-wrap").find(".hero-slider-dots");
        $(this).not(".slick-initialized").slick({
            fade: !0,
            dots: !0,
            appendDots: i,
            swipeToSlide: !0,
            touchMove: !0
        })
    }), e.each(function(e, t) {
        $(this).find(".sld").eq(0).find(".hero-slider__lazy-load-img").lazyload(lazyloadSettings)
    }), $(".hero-slider-wrap").each(function(e, t) {
        $(this).find(".hero-slider-nums").html('<div class="slick-nums">1/' + $(this).find(".sld").length + "</div>")
    }), e.on("beforeChange", function(e, t, i, n) {
        $(this).find(".sld").eq(n).find(".hero-slider__lazy-load-img").lazyload(lazyloadSettings);
        var o = n;
        o += 1, $(this).parents(".hero-slider-wrap").find(".hero-slider-nums").html('<div class="slick-nums">' + o + "/" + $(this).find(".sld").length + "</div>")
    }), $(".hero-slider__slide-name, .hero-slider__button a").on({
        mouseenter: function() {
            $(this).parents(".hero-slider__slide").find(".hero-slider__slide-image").addClass("is-hover")
        },
        mouseleave: function() {
            $(this).parents(".hero-slider__slide").find(".hero-slider__slide-image").removeClass("is-hover")
        }
    })
}

function categoriesMobile() {
    var e = $(".aside_categories-list__collapse");
    $(".aside_categories-list__toggle").on("click", function(t) {
        t.preventDefault(), $(this).text(function(e, t) {
            return "Hide categories" === t ? "Show categories" : "Hide categories"
        }), e.stop().slideToggle(300)
    }), $(document).on("click", function(t) {
        window.innerWidth < 739 && ($(t.target).closest(".aside_categories-list").length || e.stop().slideUp(300))
    })
}

function asideLeftMobile() {
    var e = $(".aside-left__collapse");
    $(".aside-left__toggle").on("click", function(t) {
        t.preventDefault(), $(this).text(function(e, t) {
            return "Hide menu" === t ? "Show menu" : "Hide menu"
        }), e.stop().slideToggle(300)
    }), $(document).on("click", function(t) {
        window.innerWidth < 992 && ($(t.target).closest(".aside-left").length || e.stop().slideUp(300))
    })
}

function seoSpoiler() {
    var e = $(".seo-spoiler__link");
    e.unbind(), e.on("click", function(e) {
        e.preventDefault();
        var t = $(this).parents(".seo-spoiler").find(".seo-spoiler__text").outerHeight();
        if ($parent = $(this).parents(".seo-spoiler"), $parent.hasClass("is-opened")) $parent.find(".seo-spoiler__wrap").stop().animate({
            height: 0
        }, 200);
        else {
            $parent.find(".seo-spoiler__wrap").stop().animate({
                height: t
            }, 200), clearTimeout(i);
            var i = setTimeout(function() {
                $parent.find(".seo-spoiler__wrap").css({
                    height: "auto"
                })
            }, 201)
        }
        $parent.toggleClass("is-opened"), $(this).toggleClass("is-active"), $(this).text(function(e, t) {
            return "Show less" === t ? "Show more" : "Show less"
        })
    }), $(window).resize(function(e) {
        $(".seo-spoiler.is-opened").find(".seo-spoiler__wrap").css({
            height: $(this).find(".seo-spoiler__text").outerHeight()
        })
    })
}

function initScripts() {
    breakpoint(), lazyload(), heroSlider(), categoriesMobile(), asideLeftMobile(), scrollRevealInit(), seoSpoiler(), mobileMenuOverflowScroll()
}

var isMobile = {
    Android: function() {
        return navigator.userAgent.match(/Android/i)
    },
    BlackBerry: function() {
        return navigator.userAgent.match(/BlackBerry/i)
    },
    iOS: function() {
        return navigator.userAgent.match(/iPhone|iPad|iPod/i)
    },
    Opera: function() {
        return navigator.userAgent.match(/Opera Mini/i)
    },
    Windows: function() {
        return navigator.userAgent.match(/IEMobile/i)
    },
    any: function() {
        return isMobile.Android() || isMobile.BlackBerry() || isMobile.iOS() || isMobile.Opera() || isMobile.Windows()
    }
};

