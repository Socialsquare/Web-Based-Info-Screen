var FADE_DURATION = 2000;

function display_slide(url, loaded_callback) {
	$oldSlides = $(".slide");
	$slide = $("<iframe></iframe>").appendTo("body");
	$slide.attr('src', url).hide().addClass('slide').attr('seamless', '');
	$slide.load(function() {
		function go_display_next() {
			$oldSlides.remove();
			// Fade in
			$slide.fadeIn(FADE_DURATION, function() {
				loaded_callback($slide);
			});
		}
		if($oldSlides.length > 0) {
			// Done fading in.
			$oldSlides.fadeOut(FADE_DURATION, go_display_next);
		} else {
			go_display_next();
		}
	});
}

function is_last_slide() {
	var total_slides = this.slides.length;
	return this.current_slide_index >= total_slides-1;
}

function display_next_slide(end_of_slide_callback) {
	if(!this.slides ||this.slides.length < 1) {
		throw "No slides sat on this.slides";
	}
	was_last_slide = is_last_slide();
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
		if(is_last_slide()) {
			console.log("It was the last slide!");
			// Fade out and reload
			$(".slide").fadeOut(FADE_DURATION, function() {
				location.reload();
			});
		} else {
			start_slideshow();
		}
	});
}

function initialize(slides) {
	console.log("Initializing info screen!", slides);
	this.slides = slides;
	start_slideshow();
}
