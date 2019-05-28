// I would like to thank fellow stident John Longgately (johnL3_alumni on slack) for helping 
//   me with a solution to making button id's unique per parts card.
//
// DISLIKED BUTTON
$(".disliked-button").on('click', function(){
    console.log("Disliked button clicked!")
    
    // get id of button clicked
    let id = $(this).attr('id');
    let d = id.split('-');
    
    // get variables of button clicked
    var partNumber = this.getAttribute('data-part-number'); 
    var token = this.getAttribute('data-token');
    var data = {
        part_number: partNumber,
        button: "disliked",
        csrfmiddlewaretoken : token
    };
    
    let url ='/products/ratings/';
    
    $.ajax({
        url: url,
        type: 'POST',
        data: data,
        success: function(response) {
    
            // Do stuff once you get the response back
            if(response['success']) {
                
                // Assemble disliked
                let dislike =`#bb-${d[1]}`;
                $(dislike).text(response['new_disliked']);
                
                // Assemble liked
                let l = id.split('-');
                like =`#aa-${l[1]}`;
                $(like).text(response['new_liked']);
                
                console.log(response);
            } 
             else {
                console.log('it failed :(')
            }
        },
    });
});



// LIKED BUTTON
$(".liked-button").on('click', function(){
    console.log("Liked button clicked!")
    
    // Get id of button clicked
    let id = $(this).attr('id');
    let l = id.split('-');
    
    // Get vars of button clicked
    var partNumber = this.getAttribute('data-part-number');
    var token = this.getAttribute('data-token');
    var data = {
        part_number: partNumber,
        button: "liked",
        csrfmiddlewaretoken: token
    };
    
    let url ='/products/ratings/';
    
    $.ajax({
        url: url,
        type: 'POST',
        data: data,
        success: function(response) {
        
            // Do stuff once you get the response back
            if(response['success']) {
                
                // Assemble liked
                let like =`#aa-${l[1]}`;
                $(like).text(response['new_liked']);
                
                // Assemble disliked
                let d = id.split('-');
                dislike =`#bb-${d[1]}`;
                $(dislike).text(response['new_disliked']);
                
                console.log(response);
            } 
            else {
                console.log('it failed :(')
            }
        },
    });
}); 