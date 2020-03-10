function submit_search(){
    var search_text = get_search_input()
    console.log('Entered search text: ' + search_text)

    if(validate_input(search_text)){
        retrieve_search_results(search_text)

    }
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

    window.location.href = "/search/"+input

    // $.ajax({
    //     type: "POST",
    //     url: "/search-results",                
    //     dataType : "json",
    //     contentType: "application/json; charset=utf-8",
    //     data : JSON.stringify(query),
    //     success: function(result){
    //         var all_results = result["results"]
    //         results = all_results
    //         update_results()
    //     },
    //     error: function(request, status, error){
    //         console.log("Error retrieving search results");
    //         console.log(request)
    //         console.log(status)
    //         console.log(error)
    //     }
    // });
}

function get_search_input(){
    return $("#search-input").val()
}

$(document).ready(function () {
    $("#search-input").attr("placeholder", "Artists, albums, & more").val("")
    
    $("#submit-button").click(function () {
        submit_search()
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

})