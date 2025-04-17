gsap.to(".navbar02", {
    top: "0%",
    borderRadius: "5vw",
    width: "85%",
    yoyo: true,
    scrollTrigger:{
        trigger: ".navbar02",
        scroller: "body",
        start: "top 0%",
        scrub: true,
    }
})
