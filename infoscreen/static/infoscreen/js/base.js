function display_slide(url, loaded_callback) {
	$oldSlides = $(".slide");
	$slide = $("<iframe></iframe>").appendTo("body");
	$slide.attr('src', url).hide().addClass('slide').attr('seamless', '');
	$slide.css('z-index', 2);
	$slide.load(function() {
		function go_display_next() {
			$oldSlides.remove();
			// Fade in
			$slide.fadeIn(200, function() {
				loaded_callback($slide);
			});
		}
		if($oldSlides.length > 0) {
			// Done fading in.
			$oldSlides.fadeOut(200, go_display_next);
		} else {
			go_display_next();
		}
	});
}

SCROLL_TICK = 100;

function display_next_slide(end_of_slide_callback) {
	if(!this.slides ||this.slides.length < 1) {
		throw "No slides sat on this.slides";
	}
	var total_slides = this.slides.length;
	var was_last_slide = this.current_slide_index >= total_slides-1;
	if(this.current_slide_index >= 0 && !was_last_slide) {
		this.current_slide_index++;
	} else if(was_last_slide) {
		this.current_slide_index = 0;
		console.log("Overflow! Starting from the first slide.");
	} else {
		this.current_slide_index = 0;
	}
	var current_slide = this.slides[this.current_slide_index]
	console.log("Next slide is ", current_slide);
	// Display
	display_slide(current_slide.fields.url, function($slide) {
		// Pre delay
		console.log("Wait for", current_slide.fields.delay, "seconds.");
		setTimeout(function() {
			console.log("End of slide!");
			end_of_slide_callback($slide);
		}, current_slide.fields.delay * 1000);
	});
}

function start_slideshow() {
	display_next_slide(function() {
		start_slideshow();
	});
}

function initialize(slides) {
	console.log("Initializing info screen!", slides);
	this.slides = slides;
	start_slideshow();
}