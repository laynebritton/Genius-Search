function delete_album(id){
    var query= {
        "id": id,
    }

    $.ajax({
        type: "POST",
        url: "/delete-album",                
        dataType : "json",
        contentType: "application/json; charset=utf-8",
        data : JSON.stringify(query),
        success: function(result){
            // window.location.href = "/view/"+result["id"]
            console.log("success")
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

    $("#delete-album-button").click(function () {
        delete_album(album.id)
	})    

})