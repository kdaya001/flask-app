const logo = document.getElementById('logo');

let counter = 0;

function showEasterEgg() {
    if(counter != 2) {
        counter++;
    } else {
        const easterEgg = document.getElementById('easter-egg');
        if(easterEgg.style.display == "block") {
            easterEgg.style.display = "none";
        } else {
            easterEgg.style.display = "block";
        }
        counter = 0;
    }
}

logo.addEventListener('click', showEasterEgg);
