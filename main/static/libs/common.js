window.onload = function() {
	$('.spoiler h3').on('click', function(e) {
		$('.spoiler h3').not($(this)).removeClass('is-active');
		$(this).toggleClass('is-active');
	})

	minHeight($('.question-section .container'));
	$('.select').selectmenu();


	slider('#credit-slider', 0, 10000, ' грн');
	slider('#termin-slider', 0, 50, 'дней');

	var popup = new Popup();

	$('.btnRegistration').on('click', function() {
		popup.open($('.popup #form-reg'));
		$('.popup #form-login').hide();
	});

	$('.btnLogin').on('click', function() {
		popup.open($('.popup #form-login'));
		$('.popup #form-reg').hide();

	});

	$('.btnApply').on('click', function() {
		popup.open($('.popup #form-apply'));
	});

	$('.btnKeep').on('click', function(e) {
		e.preventDefault();
        popup.open($('#form-confirm'));
		//popup.changeContent($('#form-confirm'));
	});	

	$('.profile-tab__btn').on('click', function(e) {
		$('.profile-tab__btn').not(this).removeClass('is-active');
		$(this).toggleClass('is-active');
	});

	$('input[type=file]').on('change', function(e) {
		var reader = new FileReader();

		var targ = getTarget(e);

		for (var i = 0; i < targ.files.length; i++) {
			var file = targ.files[i];
			var div = document.createElement('div');
			div.classList.add('profile__doc');

			var span = document.createElement("span");
			span.classList.add('doc-add__icon');

			var icon = document.createElement("i");
			icon.classList.add('far');
			icon.classList.add('fa-file');
			
			var title = document.createElement('span');
			title.classList.add('doc-add__text');

			var fileName = $(this).val().split('\\').pop();

			title.innerHTML = fileName;

			$(this).parent().before(div);
			div.append(span);
			span.append(icon);
			div.append(title);	
		}
	});

	$('.mobile-menu').on('click', function(e) {
		$(this).toggleClass('active');
	});
	function minHeight(selector) {
		var currentHeight = selector.height();
		console.log(currentHeight)
		selector.css({
			'min-height': currentHeight + 130 + 'px'
		})
	}
};

function slider(el, min, max, type) {
	$(el).slider({
		min: min,
		max: max,
		range: "min",
		animate: "slow",
		slide: function( event, ui) {
			$(el + ' .ui-slider-val').html(ui.value + ' ' + type);
		}
	});
}

function Popup() {
	var popup = $('.popup');
	var self = this;
	var popupFade = 200;
	var contentFade = 200;

	self.open = function(content) {
		self.content = content;
		popup.fadeIn(popupFade);	
		content.fadeIn(contentFade);
	}

	self.close = function(e) {
		var targ = e.target;

		if (!targ.classList.contains('popup') 
			&& !targ.classList.contains('popup__close')) return;
			$('.popup-content').fadeOut(contentFade);
		popup.fadeOut(popupFade);
	}

	self.changeContent = function(changeEl) {
		self.content.fadeOut(contentFade, function() {
			changeEl.fadeIn(contentFade);
		});
	}

	popup.on('click', self.close);
}

function getTarget(obj) {
	var targ;
	var e=obj;
	if (e.target) targ = e.target;
	else if (e.srcElement) targ = e.srcElement;
  if (targ.nodeType == 3) // defeat Safari bug
  	targ = targ.parentNode;
  return targ;
}



$(document).ready(function() {


// Login 
$('#form-login').submit(function(e){
    e.preventDefault();
    
        $.ajax({
            type: $(this).attr('method'),
            url: $(this).attr('action'),
            data: $(this).serialize(),
            success: handleSuccess,
            error: handleError
        });
        function handleSuccess(response) {
            if (response['errors'] != null) {
                errors = response.errors
                var p = $('.alert-danger').text(errors['__all__']);
            } else {
                window.location.href = $('input[name=next]').val();
            }

        }
        function handleError(ThrowError){
            console.log(ThrowError);

        }
 })

// Registration
$('#form-reg').submit(function(e){
        e.preventDefault();
        $.ajax({
        	type: $(this).attr('method'),
            url: $(this).attr('action'),
            data: $(this).serialize(),
            success: handleSuccess,
            error: handleError
           });
        function handleSuccess(response){
            if (response['errors'] != null) {
                errors = response.errors
                var phone = $('.alert-danger-phone').text(errors['phone']);
                var email = $('.alert-danger-phone').text(errors['email']);
                var password = $('.alert-danger-password').text(errors['password1']);
                var password2 = $('.alert-danger-password').text(errors['password2']);
                
            } else {
                var popup = new Popup();
                $('.popup #form-reg').hide();
                popup.open($('#form-confirm'));
            }
            
       }
       	function handleError(ThrowError){
       		console.log(ThrowError);
       	}

    })
})

// Sms confirm
$('#form-confirm').submit(function(e){
        e.preventDefault();
        $.ajax({
            type: $(this).attr('method'),
            url: $(this).attr('action'),
            data:$(this).serialize(),
            success: function(){
                window.location.href = 'users/private/';

        },
            error: function(ThrowError){

                console.log(ThrowError);

            }
        })
    })

