
$(window).on("load",function(){

          $(".title").hide(-1000);

          $(".loading").delay(5000).fadeOut("slow");
       
          $(".logo").animate({
            marginLeft:'-100px'} ,2000);

          $(".title").show(3000,"linear");  

  $(".logo").slideUp(800).slideDown(800, () => {

    $(".content").css({ display: 'block' });
    
    });
});


$("#trigger").click(function () {
  $("#hiddenDiv").slideToggle(400, "easeInOutExpo");
});