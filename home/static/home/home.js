console.log("hallo leute")

// const button = document.getElementById('go-to')
const url = window.location.href
var allButtons = [...document.getElementsByClassName('redirect-button')]

allButtons.forEach(button=> button.addEventListener('click', ()=>{
    console.log(button.name.toLowerCase())
    var destination = button.name.toLowerCase()
    console.log(url + destination + '/')
    window.location.href = url + destination + '/';
}))
// button.addEventListener('click', ()=>{
//     console.log(button.name.toLowerCase())
//     var destination = button.name.toLowerCase()
//     console.log(url + destination + '/')
//     window.location.href = url + destination + '/';

// })