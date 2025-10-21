document.addEventListener("DOMContentLoaded", () => {
  const form = document.getElementById("predictForm");
  const loader = document.getElementById("loader");
  const popup = document.getElementById("successPopup");
  const closePopup = document.getElementById("closePopup");
  const predictBtn = document.getElementById("predictBtn");

  form.addEventListener("submit", () => {
    loader.classList.remove("hidden");
    predictBtn.disabled = true;
    predictBtn.style.opacity = "0.6";
  });

  // If prediction result appears, show popup
  const resultCard = document.querySelector(".result-card");
  if (resultCard) {
    popup.classList.remove("hidden");
  }

  closePopup?.addEventListener("click", () => {
    popup.classList.add("hidden");
  });
});
