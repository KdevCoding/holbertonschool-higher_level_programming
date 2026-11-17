const header = document.querySelector('Header');
const theader = document.getElementById('toggle_header');

theader.addEventListener('click', () => {
  header.classList.toggle('green');
  header.classList.toggle('red');
});
