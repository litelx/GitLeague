$(document).ready(function() {
    alert('out of function');

    $("#userform").on('submit', function(json) {
        event.preventDefault();
        $.ajax({
            type:"POST",
            url: '/edit_group/',
            data: {
                username: $("#id_username").val()
            },
            success: function(json){
                $("#users").prepend(data.username);
            alert(" yes");
            },
            error: function(){
                alert(" no");
            }
        });
        return false;

//        var form = $(this);
//        var data = {
//                username: $("#id_username").val()
//            };
//        $.post( function (resp) {
//            var el = $(resp);
//            alert(data.username+ " yes");
//
//        }).fail(function(resp) {
//            console.error(resp.responseJSON);
//            alert(data.username+ " no");
//           /* $("#users").prepend(data.username);*/
//            form.get(0).reset();
//        });
//        return false;
    });

});
/**
 * Created by litel on 10/07/16.
 */
//$(document).ready(function() {
//
//    $("#adduform").submit(function () {
//
//        // $.ajax({
//        //     type:"POST",
//        //     url: '/edit_group/',
//        //     data: {
//        //         username: $("#id_username").val()
//        //     },
//        //     success: function(){
//        //         $("#users").prepend(data.username);
//        //         alert(url + " yes");
//        //     },
//        //     error: function(){
//        //         alert(url + " no");
//        //     }
//        // });
//        // return false;
//
//        var form = $(this);
//        var data = {
//            username: my_app //$("#id_username").val()
//        };
//        $.post( function (resp) {
//            var el = $(resp);
//            alert(data.username+ " yes");
//            $("#users").prepend(el);
//        }).fail(function(resp) {
//            console.error(resp.responseJSON);
//            alert(data.username+ " no");
//            $("#users").prepend(data.username);
//            form.get(0).reset();
//        });
//        return false;
//    });
//
//});
/**
 * Created by litel on 10/07/16.
 */
