
function submit_search(){
    var search_text = get_search_input()
    console.log('Entered search text: ' + search_text)

    if(validate_input(search_text)){
        retrieve_search_results(search_text)

    }
}

function update_results(){
    $("#search-input").val("")
    clear_search_results()
    populate_results()      
}

function populate_results (){
    console.log(results)

    results.forEach(add_result)
}

function clear_search_results(){
	$("#search-results-container").empty()
}

function add_result(result){
	var div = $('<div class="row search-result">')
    var img_div=$('<div class="col-md-2 col-sm-6 search-result-'+ result.id + '">')
    
    var result_image =$('<img src="' + result.album_art + '" class="search-img">')
    img_div.append(result_image)
    $(div).append(img_div)

	var search_result = $('<div class="search-results col-md-6 search-result-'+ result.id + '">')

    var album_title = $('<span class="album-title-text">')
    album_title.text(result.title)
    $(search_result).append(album_title)
    $(search_result).append($('<br>'))

    var album_artists = $('<span class="album-artists-text">')
    album_artists.text(result.artists)
    $(search_result).append(album_artists)
    $(search_result).append($('<br>'))

    var album_year = $('<span class="album-year-text">')
    album_year.text(result.year)
    $(search_result).append(album_year)
    $(search_result).append($('<br>'))

    var album_labels = $('<span class="album-labels-text">')
    album_labels.text(result.labels)
    $(search_result).append(album_labels)
    $(search_result).append($('<br>'))

    // Finally append the created div
    $(div).append(search_result)
	
	var search_result_delete = $('<div class="col-md-2">')
	var delete_search_result_button = $("<button class='btn btn-danger' id='" + result.id + "'>")
	delete_search_result_button.text("X")

	$(search_result_delete).append(delete_search_result_button)
	$(div).append(search_result_delete)

	$("#search-results-container").append(div)

    $(".search-result-" + result.id).click(function () {
        window.location.href = "/view/"+result.id;
    })

	$("#" + result.id).click(function () {
		delete_album($(this ).attr('id'))
    })
    
}

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
            $(".search-result-"+id).remove()
            $("#"+id).remove()

        },
        error: function(request, status, error){
            console.log("Error retrieving search results");
            console.log(request)
            console.log(status)
            console.log(error)
        }
    });

}

function get_search_input(){
    return $("#search-input").val()
}

function validate_input(input){
    var input_is_verified = true

    if(!input){
		$("#search-input").addClass("error-field")
		$("#search-input").focus()
		
		input_is_verified = false
	}
	else{
		$("#search-input").removeClass("error-field")
	}

	return input_is_verified;
}

function retrieve_search_results(input){
    var query= {
        "search_term": input,
    }

    $.ajax({
        type: "POST",
        url: "/search",                
        dataType : "json",
        contentType: "application/json; charset=utf-8",
        data : JSON.stringify(query),
        success: function(result){
            var all_results = result["results"]
            results = all_results
            update_results()
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
    $("#search-input").attr("placeholder", "Album name or artist").val("")
    
    $("#submit-button").click(function () {
        submit_search()
    })
    
    $("#create-button").click(function () {
        window.location.href = "/create"
    })

	$("#client-input").autocomplete({
		source: results
	})

    $(document).keyup(function (event) {
        validate_input(get_search_input)
    })

    $(document).keyup(function (event) {
		var keycode = (event.keyCode ? event.keyCode : event.which);
		if (keycode == '13') {
            submit_search()
		}
    });

    populate_results()
    

})