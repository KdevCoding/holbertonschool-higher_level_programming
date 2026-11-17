const header = document.querySelector('Header');
const rheader = document.getElementById('red_header');

rheader.addEventListener('click', () => {
  header.classList.add('red');
});
