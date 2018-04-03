(function( $ ) {
  $.fn.TabsToCollapse = function(appendTo) {
  	var main_element = '<div class="panel-group" id="accordion" role="tablist" aria-multiselectable="true">'
  	$.each($(this).find('.nav li a'), function(key, value){
  		var title = $(value).text();
  		var id_elem = $(value).attr("aria-controls");
  		var text = $("#"+ id_elem).html();
  		var heading = '<div class="panel-heading" role="button" data-toggle="collapse" data-parent="#accordion" href="#'+id_elem+'2" aria-expanded="false" aria-controls="'+id_elem+'2"> <h4 class="panel-title"><a>'+title+'</a></h4></div>'
  		var body = '<div id="'+id_elem+'2" class="panel-collapse collapse" role="tabpanel" aria-labelledby="headingThree"><div class="panel-body">'+text+'</div></div>'
  		main_element += '<div class="panel panel-default">'+heading+body+'</div>'
  	})
  	main_element+='</div>';
  	$(appendTo).html(main_element);
  };

  $.fn.ImageHover = function(){
    
  }

  $.fn.animateCss = function (animationName) {
    var animationEnd = 'webkitAnimationEnd mozAnimationEnd MSAnimationEnd oanimationend animationend';
    this.addClass('animated ' + animationName).one(animationEnd, function() {
        $(this).removeClass('animated ' + animationName);
    });
  }
})(jQuery);