console.log('Hallo')

// const button = document.getElementById('go-to');

var allButton = [...document.getElementsByClassName('redirect-button')]

allButton.forEach(button=>button.addEventListener('click', ()=>{
    const url_tutorial = button.value;
    console.log(url_tutorial)
    window.location.href = url_tutorial
}))

// button.addEventListener('click', function(){
//     console.log(button.name)
//     console.log(url_tutorial)
//     window.location.href = url_tutorial
// })
