document.body.onload = addElement

function addElement(){
	const lightbox = document.createElement('div')
	lightbox.id = 'lightbox'
	document.body.appendChild(lightbox)

	const all_images = document.querySelectorAll('.gallery img')
	
	all_images.forEach(image => {
		image.addEventListener('click', e =>{
			lightbox.classList.add('active')
			const img = document.createElement('img')
			img.src = image.src;
			while(lightbox.firstChild){
				lightbox.removeChild(lightbox.firstChild)
			}
			lightbox.appendChild(img)
		})
	})

	lightbox.addEventListener('click', e => {
		if(e.target !== e.currentTarget) return
		lightbox.classList.remove('active')
	})	

}