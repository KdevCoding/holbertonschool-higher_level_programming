const list = document.querySelector('ul.my_list');
const additem = document.getElementById('add_item');

additem.addEventListener('click', () => {
  const li = document.createElement('li');
  li.textContent = 'Item';
  list.appendChild(li);
});
