$(document).on("click", ".openReviewModalBtn", function () {
    var bidId = $(this).data('id');
    $("#bid_id").val( bidId );
});