function submitHandler(event) {
  event.preventDefault();
  var container = event.target.parentNode;
  var form = container.querySelector(".newsletter-form");
  var formInput = container.querySelector(".newsletter-form-input");
  var success = container.querySelector(".newsletter-success");
  var errorContainer = container.querySelector(".newsletter-error");
  var errorMessage = container.querySelector(".newsletter-error-message");
  var backButton = container.querySelector(".newsletter-back-button");
  var submitButton = container.querySelector(".newsletter-form-button");
  var loadingButton = container.querySelector(".newsletter-loading-button");

  const rateLimit = () => {
    errorContainer.style.display = "flex";
    errorMessage.innerText = "Too many signups, please try again in a little while";
    submitButton.style.display = "none";
    formInput.style.display = "none";
    backButton.style.display = "block";
  };

  // Compare current time with time of previous sign up
  var time = new Date();
  var timestamp = time.valueOf();
  var previousTimestamp = localStorage.getItem("newsletter-form-timestamp");

  // If last sign up was less than a minute ago
  // display error
  if (previousTimestamp && Number(previousTimestamp) + 60000 > timestamp) {
    rateLimit();
    return;
  }
  localStorage.setItem("newsletter-form-timestamp", timestamp);

  submitButton.style.display = "none";
  loadingButton.style.display = "flex";

  var formBody = "email=" + encodeURIComponent(formInput.value);
  fetch(event.target.action, {
    method: "POST",
    body: formBody,
    headers: {
      "Content-Type": "application/x-www-form-urlencoded",
    },
  })
    .then(async (res) => {
      if (res.ok) {
        // If response successful, show success state and clear input.
        success.style.display = "flex";
        form.reset();
        return;
      }

      // Prefer API error message when available; fall back to status text.
      var message = "Subscription failed. Please try again.";
      try {
        var data = await res.json();
        if (data && data.message) {
          message = data.message;
        }
      } catch (jsonError) {
        if (res.statusText) {
          message = res.statusText;
        }
      }

      errorContainer.style.display = "flex";
      errorMessage.innerText = message;
    })
    .catch((error) => {
      // If error caught, display the message and reset rate limit timestamp.
      errorContainer.style.display = "flex";
      errorMessage.innerText = error.message ? error.message : "Network error. Please try again.";
      localStorage.setItem("newsletter-form-timestamp", "");
    })
    .finally(() => {
      formInput.style.display = "none";
      loadingButton.style.display = "none";
      backButton.style.display = "block";
    });
}
function resetFormHandler(event) {
  var container = event.target.parentNode;
  var formInput = container.querySelector(".newsletter-form-input");
  var success = container.querySelector(".newsletter-success");
  var errorContainer = container.querySelector(".newsletter-error");
  var errorMessage = container.querySelector(".newsletter-error-message");
  var backButton = container.querySelector(".newsletter-back-button");
  var submitButton = container.querySelector(".newsletter-form-button");

  success.style.display = "none";
  errorContainer.style.display = "none";
  errorMessage.innerText = "Oops! Something went wrong, please try again";
  backButton.style.display = "none";
  formInput.style.display = "flex";
  submitButton.style.display = "flex";
}

var formContainers = document.getElementsByClassName("newsletter-form-container");

for (var i = 0; i < formContainers.length; i++) {
  var formContainer = formContainers[i];
  var handlersAdded = formContainer.classList.contains("newsletter-handlers-added");
  if (handlersAdded) continue;
  formContainer.querySelector(".newsletter-form").addEventListener("submit", submitHandler);
  formContainer.querySelector(".newsletter-back-button").addEventListener("click", resetFormHandler);
  formContainer.classList.add("newsletter-handlers-added");
}
