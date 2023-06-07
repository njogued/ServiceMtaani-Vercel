$(document).ready(function(){
    // get data from btn
    $(".orderPartBtn").click(function(){
        var part_id = $(this).data("part-id");
        // console.log("Part Id: " + part_id);

        var data = {part_id:part_id};

        //send data
        $.ajax({
            url: "/client/myorders",
            method: "POST",
            data: JSON.stringify(data),
            contentType: "application/json",
            success: function(response) {
                location.reload(true);
                console.log("Order data sent successfully");
            },
            error: function(xhr, status, error) {
                console.error("Error sending data:", error);
            }
        });

    });
});