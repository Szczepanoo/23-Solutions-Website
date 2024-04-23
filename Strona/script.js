function scrollToDiv(divId) {
            var targetDiv = document.getElementById(divId);
            targetDiv.scrollIntoView({ behavior: 'smooth', block: 'start' });
        }


function showMenu() {
    var topnav = document.getElementById("myTopnav");
    var hamburger = document.getElementById("hamburger");

    if (topnav.className === "topnav") {
        topnav.className = "responsive_topnav";
        hamburger.className = "fa fa-times";
    } else {
        topnav.className = "topnav";
        hamburger.className = "fa fa-bars"
    }

}


window.addEventListener('resize', function() {
var szerokoscEkranu = window.innerWidth;
var obiekt = document.getElementById('myTopnav');
var hamburger = document.getElementById('hamburger');

if (szerokoscEkranu > 1227) {
    obiekt.className = 'topnav';
    hamburger.className = "fa fa-bars"
}
});