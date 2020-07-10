


document.addEventListener("DOMContentLoaded", ()=>{
// window.onload =
	// response.setHeader("Set-Cookie", "HttpOnly;Secure;SameSite=Strict");
	// document.cookie = 'samesite=strict'


		/*=====
			Burger Navigation
		========*/	

		const burger = document.getElementsByClassName('burger')
		const main_nav = document.getElementsByClassName('main-nav')

		burger[0].addEventListener('click', ()=>{
			main_nav[0].classList.toggle('open')

		})
		




	/*============
		Gallery Image Slider
	===============
	*/

	const preview = document.querySelector('.preview')
	const images = document.querySelectorAll('.preview img')

	// Buttons

	const prev = document.querySelector('#prev')
	const next = document.querySelector('#next')

	// Gallery - Auto dispaly-Image
	if(window.location.href.includes('players')){
		// Counter
		let counter = 0

		let intervalId = window.setInterval(()=>{	
			images[counter].style.display = 'none'
			counter++
			if(counter > images.length-1){
				counter = 0
			}
			images[counter].style.display = 'block'
		}, 3000)
	

		next.addEventListener('click', ()=>{
			window.clearInterval(intervalId)
			images[counter].style.display = 'none'
			counter++
			if(counter > images.length-1){
				counter = 0
			}
			images[counter].style.display = 'block'
		})

		prev.addEventListener('click', ()=>{
			window.clearInterval(intervalId)
			images[counter].style.display = 'none'
			counter--
			if(counter < 0){
				counter = images.length - 1
			}
			images[counter].style.display = 'block'
		})
	}

})