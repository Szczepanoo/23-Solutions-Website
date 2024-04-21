function scrollToDiv(divId) {
            var targetDiv = document.getElementById(divId);
            targetDiv.scrollIntoView({ behavior: 'smooth', block: 'start' });
        }


function showMenu() {
    var topnav = document.getElementById("myTopnav");
    var hamburger = document.getElementById("hamburger");
    if (topnav.className === "topnav") {
        topnav.className = "responsive_topnav";
    } else {
        topnav.className = "topnav";
    }

    if (topnav.className === "responsive_topnav"){

    }


}


window.addEventListener('resize', function() {
var szerokoscEkranu = window.innerWidth;
var obiekt = document.getElementById('myTopnav');

if (szerokoscEkranu > 1227) {
    obiekt.className = 'topnav';
}
});