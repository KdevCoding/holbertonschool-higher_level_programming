const header = document.querySelector('header');
const update = document.getElementById('update_header');

update.addEventListener('click', () => {
  header.textContent = 'New Header!!!';
});
