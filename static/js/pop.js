let open = document.getElementById('open');
let open2 = document.getElementById('open2');
let close = document.getElementById('close');
let post = document.getElementById('post');

open.addEventListener('click', () => {
    post.classList.toggle('none');
});
open2.addEventListener('click', () => {
    post.classList.toggle('none');
});
close.addEventListener('click', () => {
    post.classList.toggle('none');
});