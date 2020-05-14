$("#toggle_header").on({
  click: function(){
  if($("header").hasClass("green")){
  	$("header").toggleClass("green");
    $("header").addClass("red");
    $("header").removeClass("green");
    } else {
    $("header").toggleClass("red");
    $("header").addClass("green");
    $("header").removeClass("red");
    }
