var menu = ['инструкция', 'загрузить файл', 'связаться']
var swiper = new Swiper(".mySwiper", {
    spaceBetween: 100,
    pagination: {
el: '.swiper-pagination',
clickable: true,
renderBullet: function (index, className) {
  return '<span class="' + className + '">' + (menu[index]) + '</span>';
},
},

});

$('.input-file input[type=file]').on('change', function(){
  let file = this.files[0];
  $(this).closest('.input-file').find('.input-file-text').html(file.name);
  });



const selectSingle = document.querySelector('.__select');
const selectSingle_title = selectSingle.querySelector('.__select__title');
const selectSingle_labels = selectSingle.querySelectorAll('.__select__label');

selectSingle_title.addEventListener('click', () => {
  if ('active' === selectSingle.getAttribute('data-state')) {
    selectSingle.setAttribute('data-state', '');
  } else {
    selectSingle.setAttribute('data-state', 'active');
  }
});

for (let i = 0; i < selectSingle_labels.length; i++) {
  selectSingle_labels[i].addEventListener('click', (evt) => {
    selectSingle_title.textContent = evt.target.textContent;
    selectSingle.setAttribute('data-state', '');
  });
}

const reset = document.querySelector('.reset');
reset.addEventListener('click', () => {
  selectSingle_title.textContent = selectSingle_title.getAttribute('data-default');
});



