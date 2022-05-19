const opens = document.querySelectorAll('.open');
const modals = document.querySelectorAll('.modal-bg');
const modalClose = document.querySelectorAll('.modal-close');
const modalClose2 = document.querySelectorAll('.modal-close2');

opens.forEach((btn, index) => {
  btn.addEventListener('click', () => {
    console.log(`${index}: clicked`);
    const modalClicked = modals[index];
    modalClicked.classList.add('bg-active');
  });
});

modalClose.forEach((ele, index) => {
  ele.addEventListener('click', () => {
    const modalClicked = modals[index];
    modalClicked.classList.remove('bg-active');
  });
});
modalClose2.forEach((ele, index) => {
  ele.addEventListener('click', () => {
    const modalClicked = modals[index];
    modalClicked.classList.remove('bg-active');
  });
});
