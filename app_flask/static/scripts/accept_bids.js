$(document).ready(function() {
    $(".accept_bid").click(function() {
        // Prepare the data to send
        var bidId = $(this).data("bid-id");
        // console.log("Bid ID: " + bidId);
        var data = {
            // Add your data properties here
            bid_id: bidId
        };
        console.log(data)
        

        // Send an AJAX PUT request to your Flask server
        $.ajax({
            url: "/client",  // Replace with your Flask route
            method: "PUT",
            data: JSON.stringify(data),
            contentType: "application/json",
            success: function(response) {
                // Handle the success response
                console.log("Data sent successfully");
                location.reload();
            },
            error: function(xhr, status, error) {
                // Handle the error response
                console.error("Error sending data:", error);
            }
        });
    });

    $(".bidDelete").click(function(){
        var bidId = $(this).data("bid-id");

        var data = {
            bid_id: bidId,
        }

        $.ajax({
            url: "/mechanic/openbids",
            method: "DELETE",
            data: JSON.stringify(data),
            contentType:"application/json",

            success: function(response) {
                console.log("Bid Deleted Successfully");
            },
            error: function(xhr, status, error) {
                // Handle the error response
                console.error("Error sending data:", error);
            }

        });

    location.reload(true);
    });
});
