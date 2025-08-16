document.querySelector("form").addEventListener("submit", function (e) {
  e.preventDefault();
  const mobileInput = document.getElementById("mobile");
  const mobileNumber = mobileInput.value.trim();

  if (/^09[0-9]{9}$/.test(mobileNumber)) {
    alert(`کد تایید به شماره ${mobileNumber} ارسال شد.`);
  } else {
    alert("لطفاً یک شماره موبایل معتبر وارد کنید (مثال: 09123456789)");
    mobileInput.focus();
  }
});
function changeLogo(newLogoUrl) {
  document.getElementById("logo-image").src = newLogoUrl;
}
