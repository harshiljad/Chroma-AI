// const dropZone = document.getElementById("drop-zone")
// const fileInput = document.getElementById("file-input")
// const preview = document.getElementById("preview")

// dropZone.addEventListener("click",()=>fileInput.click())

// dropZone.addEventListener("dragover",(e)=>{
// e.preventDefault()
// dropZone.style.borderColor="#6c63ff"
// })

// dropZone.addEventListener("dragleave",()=>{
// dropZone.style.borderColor="#444"
// })

// dropZone.addEventListener("drop",(e)=>{

// e.preventDefault()

// const file = e.dataTransfer.files[0]

// if(file){

// fileInput.files = e.dataTransfer.files

// showPreview(file)

// }

// })

// fileInput.addEventListener("change",(e)=>{

// const file = e.target.files[0]

// if(file){

// showPreview(file)

// }

// })

// function showPreview(file){

// const reader = new FileReader()

// reader.onload=function(e){

// preview.src = e.target.result

// preview.style.display="block"

// }

// reader.readAsDataURL(file)

// }