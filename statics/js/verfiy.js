document.addEventListener('DOMContentLoaded', () => {
    const mobileSpan = document.getElementById("mobile-number");
    const sessionPhone = mobileSpan.dataset.phone?.trim();
    if (sessionPhone) {
        mobileSpan.textContent = sessionPhone;
        localStorage.setItem("login-mobile", sessionPhone);
    } else {
        const storedPhone = localStorage.getItem("login-mobile");
        if (storedPhone) mobileSpan.textContent = storedPhone;
    }

    const inputs = document.querySelectorAll('.otp-input');
    inputs.forEach((input, index) => {
        input.addEventListener('input', () => {
            if (input.value.length === 1 && index < inputs.length - 1) {
                inputs[index + 1].focus();
            }
        });
        input.addEventListener('keydown', (e) => {
            if (e.key === "Backspace" && input.value === "" && index > 0) {
                inputs[index - 1].focus();
            }
        });
    });
})

const otpInputs = document.querySelectorAll(".otp-input");
otpInputs.forEach((input, index) => {
    input.addEventListener("input", (e) => {
        if (e.target.value.length === 1) {
            if (index < otpInputs.length - 1) otpInputs[index + 1].focus();
            else otpInputs[index].blur();
        }
    });

    input.addEventListener("keydown", (e) => {
        if (e.key === "Backspace" && e.target.value === "") {
            if (index > 0) {
                otpInputs[index - 1].focus();
                otpInputs[index - 1].value = "";
                otpInputs[index - 1].dispatchEvent(new Event("input"));
                e.preventDefault();
            }
        }
    });
});

// تایمر ارسال دوباره
let timerCount = 60;
const timerElement = document.getElementById("timer");
const resendLink = document.getElementById("resend-link");

function updateTimer() {
    if (timerElement) timerElement.textContent = ` (${timerCount} ثانیه)`;
    if (timerCount <= 0) {
        if (timerElement) timerElement.textContent = "";
        if (resendLink) resendLink.style.display = "inline";
    } else {
        timerCount--;
        setTimeout(updateTimer, 1000);
    }
}

if (resendLink) {
    resendLink.addEventListener("click", (e) => {
        e.preventDefault();
        timerCount = 60;
        resendLink.style.display = "none";
        updateTimer();
        alert("کد جدید برای شما ارسال شد.");
    });
    resendLink.style.display = "none";
}
updateTimer();

// ارسال فرم OTP
const form = document.querySelector("form");
if (form) {
    form.addEventListener("submit", function (e) {
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
}

