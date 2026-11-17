document.addEventListener('DOMContentLoaded', function () {
  const update = document.querySelector('#hello');
  fetch('https://hellosalut.stefanbohacek.com/?lang=fr')
    .then((response) => response.json())
    .then((data) => {
      update.textContent = data.hello;
    });
});
