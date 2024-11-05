let preveiwContainer = document.querySelector('.products-preview');
let previewBox = preveiwContainer.querySelectorAll('.preview');

document.querySelectorAll('.fight-container .smile').forEach(smile =>{
    smile.onclick = () =>{
        preveiwContainer.style.display = 'flex';
      let name = smile.getAttribute('data-name');
      previewBox.forEach(preview =>{
        let target = preview.getAttribute('data-target');
        if (name == target){
            preview.classList.add('active');
        }
      });
    };
});

previewBox.forEach(close =>{
close.querySelector('.fa-times').onclick = () =>{
  close.classList.remove('active');
  preveiwContainer.style.display = 'none';
};
});
