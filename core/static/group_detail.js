$(document).ready(function() {
//    alert('out of function');

    $("#userform").on('submit', function(json) {
        $.ajax({
            type:"POST",
            url: $(this).attr('action'),
            data: {
                username: $("#id_username").val()
            },
            success: function(data){
                // Check if already exists or new.
                $("#users").append(data.username);
                $("#id_username").val('');
            },
            error: function(){
                alert("something bad happened");
            }
        });
        return false;
    });
});

    /*

        $("#commentform").submit(function () {
        var form = $(this);
        var data = {
            title: $("#id_title").val(),
            content: $("#id_content").val()
        };
        $.post("", data).then(function (resp) {
            var el = $(resp);
            $("#comments").prepend(el);
            form.get(0).reset();
        }).fail(function(resp) {
            console.error(resp.responseJSON);
            alert('something bad happend');
        });







    $('a').click(function (json) {
        $.ajax({
            type:"DELETE",
            url: $(this).attr('action'),
            data: {
                id: 17,
            },
            success: function(data){
//                $("users").remove(to_delete);
//                $("#users").append($(this));
                $("#id_username").val('');
            },
            error: function(){
            }
        });
        return false;
    });*/

//    $("a").on('click', function(json) {
//        $.ajax({
//            type:"POST",
//            url: $(this).attr('action'),
//            data: {
//                id: $(this).attr('id'),
//            },
//            success: function(data){
////                $("#"+data.id).prev('li').remove();
//                $(this).prev('li').remove();
//                alert(data.idd);
//                $("#id_username").val('');
//            },
//            error: function(){
////                var dd = $("#{{u.id}}").attr('id');
//                alert("something bad happened");
//            }
//        });
//        return false;
//    });

