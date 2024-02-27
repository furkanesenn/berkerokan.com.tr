const openButton = document.getElementById("_hamburger--open");
const closeButton = document.getElementById("_hamburger--close");
const nav = document.getElementById("_nav");

openButton.addEventListener("click", ()=>{
    nav.classList.toggle("active")
})
closeButton.addEventListener("click", ()=>{
    nav.classList.toggle("active")
})
