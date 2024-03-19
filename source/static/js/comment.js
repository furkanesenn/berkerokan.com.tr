const subcommentForm = document.getElementById("subcomment_form");

const commentsList = [...document.querySelectorAll(".comments__item[data-id]")];
let comments = {};
commentsList.forEach((e) => {
  comments[e.dataset.id] = e;
});

function replyToComment(id) {
  const form = subcommentForm.querySelector("form");
  form.action = `/comments/reply/${id}`;
  subcommentForm.style.display = "block";

  let elm = comments[id];
  elm.appendChild(subcommentForm);
}
