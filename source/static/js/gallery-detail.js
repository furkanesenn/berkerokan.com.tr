window.addEventListener("DOMContentLoaded", () => {
  const images = document.querySelectorAll(".gallery-detail__main-item");
  const bigImageContainer = document.querySelector("#big-image-container");
  const background = document.createElement("div");
  background.classList.add("background");
  const image = document.createElement("img");
  bigImageContainer.appendChild(background);
  bigImageContainer.appendChild(image);

  image.addEventListener("click", () => {
    image.src = "";
    image.classList.remove("active");
    images.forEach((e) => {
      e.classList.remove("active");
    });
    document.body.style.overflowY = "scroll";
  });
  background.addEventListener("click", () => {
    image.src = "";
    image.classList.remove("active");
    images.forEach((e) => {
      e.classList.remove("active");
    });
    document.body.style.overflowY = "scroll";
  });
  images.forEach((e) => {
    e.addEventListener("click", () => {
      if (!e.classList.contains("active")) {
        images.forEach((_e) => {
          _e.classList.remove("active");
        });
        e.classList.add("active");
        image.classList.add("active");
        document.body.style.overflowY = "hidden";
        document.body.style.overflowX = "hidden";
        const galleryImage = e.querySelector("img");
        console.log(galleryImage);
        image.src = galleryImage.src;
      } else {
        e.classList.remove("active");
        image.src = "";
        image.classList.remove("active");
        document.body.style.overflowY = "scroll";
      }
    });
  });
});
