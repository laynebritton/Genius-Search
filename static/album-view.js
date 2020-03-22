var album_has_been_deleted = false

function delete_album(id){
    var query= {
        "id": id,
    }

    $.ajax({
        type: "POST",
        url: "/mark-as-deleted",                
        dataType : "json",
        contentType: "application/json; charset=utf-8",
        data : JSON.stringify(query),
        success: function(result){
            // window.location.href = "/view/"+result["id"]
            console.log(result)

            insert_undo_button()
        },
        error: function(request, status, error){
            console.log("Error retrieving search results");
            console.log(request)
            console.log(status)
            console.log(error)
        }
    });

}

function insert_undo_button(){
    var card = $('<div class="undo-bar">')

    var delete_confirmed_text =$('<span class="">')
    $(delete_confirmed_text).text("\t" + album.title + " has been deleted.")

    var undo_button = $('<button class="btn btn-warning" id="undo-button">')

    $(undo_button).text("Undo")
    
    $(card).append(undo_button)

    $(card).append(delete_confirmed_text)

    $("#undo-container").append(card)

    $("#undo-button").click(function () {
        undo_delete_album(album.id)
    })
    
}

function remove_undo_button(){
    $("#undo-container").empty()
}

function undo_delete_album(id){
    var query= {
        "id": id,
    }

    $.ajax({
        type: "POST",
        url: "/unmark-as-deleted",                
        dataType : "json",
        contentType: "application/json; charset=utf-8",
        data : JSON.stringify(query),
        success: function(result){
            remove_undo_button()
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