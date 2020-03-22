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

            clear_delete_container()
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

    $(card).append(delete_confirmed_text)


    $("#undo-container").append(card)

    var undo_button = $('<button class="btn btn-warning" id="undo-button">')

    $(undo_button).text("Undo")
    

    $("#delete-container").append(undo_button)

    $("#undo-button").click(function () {
        undo_delete_album(album.id)
    })
    
}

function insert_delete_button(){
    var delete_button = $('<button id="delete-album-button" class="btn btn-danger" alt="delete album">')


    // var trash_icon = $('<svg class="bi bi-trash" width="1em" height="1em" viewBox="0 0 16 16" fill="currentColor" xmlns="http://www.w3.org/2000/svg">')

    // var path1 = $('<path d="M5.5 5.5A.5.5 0 016 6v6a.5.5 0 01-1 0V6a.5.5 0 01.5-.5zm2.5 0a.5.5 0 01.5.5v6a.5.5 0 01-1 0V6a.5.5 0 01.5-.5zm3 .5a.5.5 0 00-1 0v6a.5.5 0 001 0V6z" />')
    // var path2 = $('<path fill-rule="evenodd" d="M14.5 3a1 1 0 01-1 1H13v9a2 2 0 01-2 2H5a2 2 0 01-2-2V4h-.5a1 1 0 01-1-1V2a1 1 0 011-1H6a1 1 0 011-1h2a1 1 0 011 1h3.5a1 1 0 011 1v1zM4.118 4L4 4.059V13a1 1 0 001 1h6a1 1 0 001-1V4.059L11.882 4H4.118zM2.5 3V2h11v1h-11z" clip-rule="evenodd" />')

    // $(trash_icon).append(path1)
    // $(trash_icon).append(path2)

    // $(delete_button).append(trash_icon)

    $(delete_button).text("Delete")

    $("#delete-container").append(delete_button)

    
    $("#delete-album-button").click(function () {
        delete_album(album.id)
	})    
}

function clear_undo_container(){
    $("#undo-container").empty()
}

function clear_delete_container(){
    $("#delete-container").empty()
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
            clear_delete_container()
            clear_undo_container()
            insert_delete_button()
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

    insert_delete_button()


})