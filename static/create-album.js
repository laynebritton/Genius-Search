function create_album(){
    var query= {
        "title": $("#title-input").val(),
        "artists": $("#artists-input").val(),
        "year": $("#year-input").val(),
        "genres": $("#genres-input").val(),
        "labels": $("#labels-input").val(),
        "producers": $("#producers-input").val(),
        "description": $("#description-input").val(),
        "album_art": $("#album-art-input").val(),
    }

    $.ajax({
        type: "POST",
        url: "/create-album",                
        dataType : "json",
        contentType: "application/json; charset=utf-8",
        data : JSON.stringify(query),
        success: function(result){
            window.location.href = "/view/"+result["id"]

        },
        error: function(request, status, error){
            console.log("Error retrieving search results");
            console.log(request)
            console.log(status)
            console.log(error)
        }
    });

}

function validate_input(){

	if($("#album-art-input").val()){
		$("#album-art-input").removeClass("error-field")
	}

	if($("#description-input").val()){
		$("#description-input").removeClass("error-field")
	}

	    
    if($("#producers-input").val()){
		$("#producers-input").removeClass("error-field")
	}
	
	if($("#labels-input").val()){
		$("#labels-input").removeClass("error-field")
	}
	
    if($("#genres-input").val()){
		$("#genres-input").removeClass("error-field")
	}

	if($("#year-input").val()){
		$("#year-input").removeClass("error-field")
	}
	
	if($("#artists-input").val()){
		$("#artists-input").removeClass("error-field")
	}

    if($("#title-input").val()){
		$("#title-input").removeClass("error-field")
	}

}

function validate_input_focus(){
    var input_is_verified = true

	if(!$("#album-art-input").val()){
		$("#album-art-input").addClass("error-field")
		$("#album-art-input").focus()
		
		input_is_verified = false
	}
	else{
		$("#album-art-input").removeClass("error-field")
	}

    if(!$("#description-input").val()){
		$("#description-input").addClass("error-field")
		$("#description-input").focus()
		
		input_is_verified = false
	}
	else{
		$("#description-input").removeClass("error-field")
	}

	    
    if(!$("#producers-input").val()){
		$("#producers-input").addClass("error-field")
		$("#producers-input").focus()
		
		input_is_verified = false
	}
	else{
		$("#producers-input").removeClass("error-field")
    }
	
	if(!$("#labels-input").val()){
		$("#labels-input").addClass("error-field")
		$("#labels-input").focus()
		
		input_is_verified = false
	}
	else{
		$("#labels-input").removeClass("error-field")
    }
	
    if(!$("#genres-input").val()){
		$("#genres-input").addClass("error-field")
		$("#genres-input").focus()
		
		input_is_verified = false
	}
	else{
		$("#genres-input").removeClass("error-field")
    }

	if(!$("#year-input").val()){
		$("#year-input").addClass("error-field")
		$("#year-input").focus()
		
		input_is_verified = false
	}
	else{
		$("#year-input").removeClass("error-field")
	}
	
	if(!$("#artists-input").val()){
		$("#artists-input").addClass("error-field")
		$("#artists-input").focus()
		
		input_is_verified = false
	}
	else{
		$("#artists-input").removeClass("error-field")
	}
	
    if(!$("#title-input").val()){
		$("#title-input").addClass("error-field")
		$("#title-input").focus()
		
		input_is_verified = false
	}
	else{
		$("#title-input").removeClass("error-field")
    }

	return input_is_verified;
}
$(document).ready(function () {

    $("#create-button").click(function () {
		console.log(validate_input_focus())
		if(validate_input_focus()){
			
            create_album()
        }
	})    
	
	$("input").keyup(function(){
		validate_input()
	});

})