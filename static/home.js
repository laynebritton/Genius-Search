function update_results(){
    $("#search-input").val("")
    clear_search_results()
    populate_results()      
}

function populate_results (){
    results.forEach(add_result)
}

function clear_search_results(){
	$("#search-results-container").empty()
}

function add_result(result){
    var card = $('<div class="card">')

    var card_img = $('<img src="' + result.album_art + '" class="card-img-top search-img" id="'+ result.id +'" alt="'+ result.title + ' album art.">')
    $(card).append(card_img)

    var card_body = $('<div class="card-body">')

    var card_title=$('<h5 class="card-title" alt="'+ result.title + '">')
    $(card_title).text(result.title)
    $(card_body).append(card_title)

    var card_artists = $('<span class="card-text" alt="'+ result.artists+ '">')
    $(card_artists).text(result.artists)
    $(card_body).append(card_artists)

    var card_year = $('<span class="card-text year-text" alt="' +result.year + '">')
    $(card_year).text( ", " + result.year)
    $(card_body).append(card_year)

    $(card).append(card_body)

    $("#search-results-container").append(card)

	$("#" + result.id).click(function () {
        window.location.href = "/view/"+result.id
    })

    $("#" + result.id).hover(function () {
        $(this).addClass("hover-over-clickable")
    }, function () {
        
        $(this).removeClass('hover-over-clickable');
    });

    
}

$(document).ready(function () {

    populate_results()
    
})