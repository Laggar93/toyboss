
AOS.init({
    duration: 1000,
    once: true
});

function openDropdown(dropdownContentId) {
    document.getElementById(dropdownContentId).classList.toggle("show");
}

// Close the dropdown if the user clicks outside of it
window.onclick = function(event) {
    if (!event.target.matches('.dropbtn')) {
        var dropdowns = document.getElementsByClassName("dropdown-content");
        var i;
        for (i = 0; i < dropdowns.length; i++) {
            var openDropdown = dropdowns[i];
            if (openDropdown.classList.contains('show')) {
                openDropdown.classList.remove('show');
            }
        }
    }
}

function showMobileMenu() {
    var element = document.getElementById("mobile-menu");
    element.classList.add("active");
}
function hiddenMobileMenu() {
    var element = document.getElementById("mobile-menu");
    element.classList.remove("active");
}


$( function() {
    $( "#tabs" ).tabs();
    $( "#tabs-production" ).tabs();
    $( "#tabs-advantages" ).tabs();
    $( ".product-block-content-left" ).tabs();
    $( "#tab-history" ).tabs({

    });
    $( "#faq" ).accordion({
        heightStyle: "content",
        collapsible: true,
        active: false
    });
    $('.counter').counterUp({
        delay: 20,
        time: 1500
    });

    lightGallery(document.getElementById('lightgallery'), {
        speed: 500,
        share: false,
        download: false,
    });

    var scene = document.getElementById('scene-about-us');
    if(scene) {
        var parallaxInstance = new Parallax(scene);
    }

    var rellax = new Rellax('.rellax', {
        speed: -6,
        center: false,
        wrapper: null,
        round: true,
        vertical: true,
        horizontal: false
    });
    var scene = document.getElementById('phone');
    if(scene) {
        $("#phone").mask("(996) 999-999-999");
    }

} );


