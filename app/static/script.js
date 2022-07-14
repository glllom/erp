
function redirect(){
    let height = document.querySelector('.height').value;
    let width = document.querySelector('.width').value;
    console.log(height, width);
    window.location.href = `/${height}/${width}`;
}