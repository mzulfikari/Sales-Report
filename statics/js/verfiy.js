const mobileNumber = localStorage.getItem("login-mobile") || "0912****345";
document.getElementById("mobile-number").textContent = mobileNumber;
const otpInputs = document.querySelectorAll(".otp-input");

otpInputs.forEach((input, index) => {
  input.addEventListener("input", (e) => {
    if (e.target.value.length === 1) {
      if (index < otpInputs.length - 1) {
        otpInputs[index + 1].focus();
      } else {
        otpInputs[index].blur();
      }
    }
  });

  input.addEventListener("keydown", (e) => {
    if (e.key === "Backspace" && e.target.value === "") {
      if (index > 0) {
        otpInputs[index - 1].focus();
        otpInputs[index - 1].value = "";
        otpInputs[index - 1].dispatchEvent(new Event("input"));
        e.preventDefault();
        return false;
      }
    }
  });
});
let timerCount = 60;
const timerElement = document.getElementById("timer");
const resendLink = document.getElementById("resend-link");

function updateTimer() {
  timerElement.textContent = ` (${timerCount} ثانیه)`;

  if (timerCount <= 0) {
    timerElement.textContent = "";
    resendLink.style.display = "inline";
  } else {
    timerCount--;
    setTimeout(updateTimer, 1000);
  }
}

resendLink.addEventListener("click", (e) => {
  e.preventDefault();
  timerCount = 60;
  resendLink.style.display = "none";
  updateTimer();
  alert("کد جدید برای شما ارسال شد.");
});

resendLink.style.display = "none";
updateTimer();

document.querySelector("form").addEventListener("submit", function (e) {
  e.preventDefault();
  let otpCode = "";
  otpInputs.forEach((input) => {
    otpCode += input.value;
  });

  if (otpCode.length === 4) {
    alert(`کد ${otpCode} با موفقیت تایید شد.`);
  } else {
    alert("لطفاً کد چهار رقمی را کامل وارد کنید.");
  }
});
