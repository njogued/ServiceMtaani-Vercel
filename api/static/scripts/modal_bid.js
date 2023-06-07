$(document).on("click", ".bidForJob", function () {
    var jobId = $(this).data('id');
    $(".modal-body #job_id").val( jobId );


    // console.log(jobId);

    // As pointed out in comments,
    // it is unnecessary to have to manually call the modal.
    // $('#addBookDialog').modal('show');
});

$(document).on("click", "#editBidModal", function () {
    var bidId = $(this).data('id');
    $(".modal-body #bid_id").val( bidId );
});

$(document).on("click", "#submitBidChangeButton", function () {
    var bid_id = $("#bid_id").val();
    var bid_amount = $("#formprice").val();
    var data = {
        bid_id: bid_id,
        bid_amount: bid_amount
    };
    $.ajax({
        url: "/mechanic/openbids",  // Replace with your Flask route to handle the submission
        method: "PUT",
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

// $(document).on("click", ".submitbutton", function () {
//     $('.bidForJob').hide();
// });
$(document).on("click", ".editPartDetails", function () {
    var partId = $(this).data('id');
    $("#part_id").val( partId );
});