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

function clear_review_creator_container(){
    $("#review-creator-container").empty()
}

function clear_insert_leave_review_button(){
    $('#leave-review-button-container').empty()
}

function insert_leave_review_button(){
    var add_review_button = $('<button id="add-review-button" class="btn btn-primary">')
    $(add_review_button).text("Leave a review")

    $('#leave-review-button-container').append(add_review_button)

    $("#add-review-button").click(function () {
        clear_insert_leave_review_button()
        insert_review_creator()
	})


}

function insert_review_creator(){

    var form_group = $('<div class="form-group">')
    var label = $('<label>')
    $(label).text("Enter review: ")

    var text_area = $('<textarea id="review-textarea" class="form-control" rows="3">')

    var submit_button = $('<button id="submit-review-button" class="btn btn-primary" alt="Submit Review">')
    $(submit_button).text("Submit review")
    var cancel_button = $('<button id="cancel-review-button" class="btn btn-secondary" alt="Cancel review" >')
    $(cancel_button).text("Cancel")

    $(form_group).append(label)
    $(form_group).append(text_area)
    
    $(form_group).append(submit_button)
    
    var tab = $('<span>')
    $(tab).text("\t")
    $(form_group).append(tab)

    $(form_group).append(cancel_button)

    $('#review-creator-container').append(form_group)

    $("#cancel-review-button").click(function () {
        clear_review_creator_container()
        insert_leave_review_button()
    })
    
    $("#submit-review-button").click(function () {
        add_review()
        clear_review_creator_container()
        insert_leave_review_button()
    })
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


function add_review(){
    user_review =  $("#review-textarea").val()
    var query= {
        "id": album.id,
        "user_review": user_review
    }

    $.ajax({
        type: "POST",
        url: "/add-review",                
        dataType : "json",
        contentType: "application/json; charset=utf-8",
        data : JSON.stringify(query),
        success: function(result){
            album.user_reviews.push(user_review)
            clear_reviews()
            insert_reviews()
        },
        error: function(request, status, error){
            console.log("Error retrieving search results");
            console.log(request)
            console.log(status)
            console.log(error)
        }
    });

}

function clear_reviews(){
    $('#review-container').empty()
}

function insert_reviews(){
    if(album.user_reviews.length == 0){
        insert_no_reviews_text()
        return
    }
    album.user_reviews.forEach(insert_review)
}

function insert_review(review_text){
    var review_card = $('<div class="card">')

    var review_entry = $('<div class="card-body" >')
    $(review_entry).text(review_text)

    $(review_card).append(review_entry)
    $("#review-container").append(review_card)
}

function insert_no_reviews_text(){
    var span = $('<span>')

    $(span).text("No user reviews yet")

    $("#review-container").append(span)
}

$(document).ready(function () {
    insert_delete_button()
    insert_leave_review_button()
    insert_reviews()
})