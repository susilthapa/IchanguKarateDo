// GSAP-ANIMATION


// document.addEventListener("DOMContentLoaded", ()=>{
window.onload =
	// response.setHeader("Set-Cookie", "HttpOnly;Secure;SameSite=Strict");
	// document.cookie = 'samesite=strict'
  	/*======
		Home Animations
  	=======*/
    // gsap.from('.d', {opacity:0, stagger:0.6,scale:0, duration:0.8,})
	// gsap.from('.d', {x:-300, duration:1})
	// console.log(one)
	gsap.from('.abt1', {scrollTrigger:{trigger: '.abt1',toggleActions: "restart pause resume"},
				 x:-500,
				 duration: 1.5
				})

	gsap.from('.abt2', {scrollTrigger:{trigger: '.abt2', toggleActions: "restart pause resume"},
				 x:500,
				 duration: 1.5
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

	// Auto dispaly-Image
	if(window.location.href.includes('gallery')){
		let intervalId = window.setInterval(()=>{	
			images[counter].style.display = 'none'
			counter++
			if(counter > images.length-1){
				counter = 0
			}
			images[counter].style.display = 'block'
		}, 3000)
	

		// Counter
		let counter = 0
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
// })
