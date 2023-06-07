$(".mech-active-jobs").click(function() {
    $(".mech-jobs").not(this).removeClass("btn-primary");
    $(this).removeClass("btn-secondary");
    $(this).addClass("btn-primary");
    $(".mech-jobs").not(this).addClass("btn-secondary");
  });

  $(".mech-open-jobs").click(function() {
    $(".mech-jobs").not(this).removeClass("btn-primary");
    $(this).removeClass("btn-secondary");
    $(this).addClass("btn-primary");
    $(".mech-jobs").not(this).addClass("btn-secondary");
  });
  $(".mech-open-bids").click(function() {
    $(".mech-jobs").not(this).removeClass("btn-primary");
    $(this).removeClass("btn-secondary");
    $(this).addClass("btn-primary");
    $(".mech-jobs").not(this).addClass("btn-secondary");
  });
  $(".mech-completed-jobs").click(function() {
    $(".mech-jobs").not(this).removeClass("btn-primary");
    $(this).removeClass("btn-secondary");
    $(this).addClass("btn-primary");
    $(".mech-jobs").not(this).addClass("btn-secondary");
  });