$(document).ready(function(){
	
	/*======
		Burger Nav
	=======*/

	// $('.burger').on('click', function(){
	// 	$('.main-nav').toggleClass('open')
	// })


	/* ======
		Active link
	=========*/
	
	$('.main-nav a').each(function() {
   		var path = window.location.href;
	  if (this.href === path) {
	  		$(".main-nav li").removeClass("active");
		   	$(this).closest('li').addClass('active')
		   	$(this).closest('li a').css('color', 'black')
		   	
		   	if(path.includes('gallery')){
		   		$('#dropdown').addClass('active')
		   	}
		   	}
		})


	$('.dropdown-links a').each(function(){
   		var path = window.location.href;
	  	if (this.href === path) {
			$(this).css('color', 'red')
		}
	
	})


	$('.scroll').on('click', function(){		
		$(".main-nav li").removeClass("active");
		$('.main-nav li a').css('color', 'white')

		$(this).closest('li').addClass('active')
		$(this).closest('li a').css('color', 'black')
		$('.main-nav').toggleClass('open')
		
	})

	/*========
		GAllery
	=========*/
	$('.gallery-nav li').on('click', function(){
		$('.gallery-nav li').removeClass('active')
		$(this).addClass('active')

		// console.log($(this).attr('id'))

		if ($(this).attr('id') === 'one')
		{
			$('#one-one').siblings().css('display', 'none')
			$('#one-one').css('display', 'flex')


		}else if($(this).attr('id') === 'two'){
			$('#two-two').siblings().css('display', 'none')
			$('#two-two').css('display', 'flex')

			}
		else if($(this).attr('id') === 'three'){
			$('#three-three').siblings().css('display', 'none')
			$('#three-three').css('display', 'flex')

			}
	})
	

	/* ======
		smooth scrolling AvoutPage
	======*/
	$('.scroll').click(function(e){
		
		$('body, html').animate({scrollTop: $(this.hash).offset().top-200}, 1000)
		// console.log($(this).attr('href', 'http://127.0.0.1:8000/'))

	})

	/*=======
		GAlleryNav Smooth-scroll
	===========*/
	$('.gallery-nav a').click(function(){
		// let tag = $(this).find('a').attr("href")
		$('body, html').animate({scrollTop: $(this.hash).offset().top-600}, 1000)
	})


})