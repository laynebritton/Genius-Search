function add_review(){
    var query= {
        "id": album.id,
        "user_review": $("#review-input").val()
    }

    $.ajax({
        type: "POST",
        url: "/add-review",                
        dataType : "json",
        contentType: "application/json; charset=utf-8",
        data : JSON.stringify(query),
        success: function(result){
            window.location.href = "/view/"+album.id

        },
        error: function(request, status, error){
            console.log("Error retrieving search results");
            console.log(request)
            console.log(status)
            console.log(error)
        }
    });

}

$(document).ready(function () {

    $("#submit-button").click(function () {
        add_review()
    })    
    $(document).keyup(function (event) {
		var keycode = (event.keyCode ? event.keyCode : event.which);
		if (keycode == '13') {
            add_review()
		}
    });
})