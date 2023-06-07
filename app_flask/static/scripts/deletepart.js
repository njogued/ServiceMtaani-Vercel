$(document).on("click", ".deleteVendorPart", function () {
    var partId = $(this).data('id');
    var data = {
        part_id: partId
    };

    $.ajax({
        url: "/vendor/catalogue",
        type: "DELETE",
        data: JSON.stringify(data),
        contentType: "application/json",
        success: function(response) {
                // Handle the success response
                console.log("Part deleted successfully");
                // Optionally, you can close the modal after successful submission
                //   $("#myModal").modal("hide");
                },
        error: function(xhr, status, error) {
                // Handle the error response
                console.error("Error sending data:", error);
                }
    });
    location.reload(true);
});