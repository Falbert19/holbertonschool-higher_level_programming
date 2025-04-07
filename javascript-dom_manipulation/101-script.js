document.addEventListener("DOMContentLoaded", function () {
  document.querySelector("#btn_translate").addEventListener("click", function () {
    const lang = document.querySelector("#language_code").value
    if (lang) {
      fetch("https://hellosalut.stefanbohacek.dev/?lang=" + lang)
        .then(function (response) {
          return response.json()
        })
        .then(function (data) {
          document.querySelector("#hello").textContent = data.hello
        })
    }
  })
})
