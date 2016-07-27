$(document).ready(function() {

    $("#userform").on('submit', function(json) {
        $.ajax({
            type:"POST",
            url: $(this).attr('action'),
            data: {
                username: $("#id_username").val()
            },
            success: function(resp){
                var el = $(resp)
                $("#xx").before(el);
            },
            error: function(msg){
                alert("Something happen improperly. \n" +
                        "User may already exist.");
            }
        });
        return false;
    });
});
