$(document).ready(function() {
  $("#openModalBtn").click(function() {
    // Remove btn-success class from all buttons
    $(".btn-jobs").removeClass("btn-primary");

    // Add btn-success class to the clicked button
    $(this).addClass("btn-primary");

    // Remove btn-primary class from all other buttons
    $(".btn-jobs").not(this).removeClass("btn-primary");

    // Add btn-primary class to the other button
    $(".btn-jobs").not(this).addClass("btn-secondary");
    //   $("#myModal").modal("show");

  });

  $(".btn-open-jobs").click(function() {
    $(".btn-jobs").not(this).removeClass("btn-primary");
    $(this).removeClass("btn-secondary");
    $(this).addClass("btn-primary");
    $(".btn-jobs").not(this).addClass("btn-secondary");
    var new_heading = "Open Jobs";
    $("#jobs-heading").text(new_heading);
  });

  $(".btn-completed-jobs").click(function() {
    $(".btn-jobs").not(this).removeClass("btn-primary");
    $(this).removeClass("btn-secondary");
    $(this).addClass("btn-primary");
    $(".btn-jobs").not(this).addClass("btn-secondary");
    var new_heading = "Completed Jobs";
    $("#jobs-heading").text(new_heading);

    $.ajax({
      url: "/client/completedjobs",
      type: "GET",
      success: function(response) {
        // Handle the success response
        // console.log(response);
      },
      error: function(xhr, status, error) {
        // Handle the error response
        console.error(error);
      }
    });
  });

  $(".btn-active-jobs").click(function() {
    $(".btn-jobs").not(this).removeClass("btn-primary");
    $(this).removeClass("btn-secondary");
    $(this).addClass("btn-primary");
    $(".btn-jobs").not(this).addClass("btn-secondary");
    var new_heading = "Active Jobs";
    $("#jobs-heading").text(new_heading);

    $.ajax({
      url: "/client/activejobs",
      type: "GET",
      success: function(response) {
        // Handle the success response
        // console.log(response);
      },
      error: function(xhr, status, error) {
        // Handle the error response
        console.error(error);
      }
    });
  });

//Get all Client Orders
  $(".btn-my-orders").click(function() {
    $(".btn-jobs").not(this).removeClass("btn-primary");
    $(this).removeClass("btn-secondary");
    $(this).addClass("btn-primary");
    $(".btn-jobs").not(this).addClass("btn-secondary");
    var new_heading = "Orders List";
    $("#jobs-heading").text(new_heading);

    $.ajax({
      url: "/client/myorders",
      type: "GET",
      success: function(response) {
        // Handle the success response
        // console.log(response);
      },
      error: function(xhr, status, error) {
        // Handle the error response
        console.error(error);
      }
    });
  });


  //post job
  $("#submitBtn").click(function() {
    var job_title = $("#job_title").val();
    var job_description = $("#job_desc").val();

    // Prepare the data to send to SQLAlchemy
    var data = {
      job_title: job_title,
      job_description: job_description
    };

    // Send an AJAX POST request to your Flask server
    $.ajax({
      url: "/client",  // Replace with your Flask route to handle the submission
      method: "POST",
      data: JSON.stringify(data),
      contentType: "application/json",
      success: function(response) {
        // Handle the success response
        // console.log("Data sent successfully");
        // Optionally, you can close the modal after successful submission
        //   $("#myModal").modal("hide");
        location.reload();
      },
      error: function(xhr, status, error) {
        // Handle the error response
        console.error("Error sending data:", error);
      }
    });
  });

  //Delete a Job
  $(".btn-delete").click(function(){
    var job_id = $(this).data("job-id");
    var data = {job_id: job_id};

    $.ajax({
      url: "/client",
      method: "DELETE",
      data: JSON.stringify(data),
      contentType: "application/json",
      success: function(response) {
        // Handle the success response
        console.log("Job deleted successfully");
        // Optionally, you can close the modal after successful submission
        //   $("#myModal").modal("hide");
      },
      error: function(xhr, status, error) {
        // Handle the error response
        console.error("Error sending data:", error);
      }

    });
    location.reload(true)

  });
});
