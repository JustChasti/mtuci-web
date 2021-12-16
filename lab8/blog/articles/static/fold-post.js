window.addEventListener("DOMContentLoaded", () => {
    const wrappers = document.querySelector(".archive");
  
    wrappers.addEventListener("click", (e) => {
      target = e.target;
      if (target && target.matches(".fold-button")) {
        if (target.parentElement.classList.contains("folded")) {
          target.innerHTML = "Свернуть";
          target.parentElement.classList.remove("folded");
        } else {
          console.log(target.parentElement);
          target.innerHTML = "Развернуть";
          target.parentElement.classList.add("folded");
        }
      }
    });
});