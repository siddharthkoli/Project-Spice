$("#username").change(function() {
    var username = $(this).val();

    $.ajax({
        type : 'GET',
        url : '/usernamevalidation',
        data : {
            "username" : username,
        },
        dataType : 'json',
        success : function(result) {
            if (result.is_taken){
                $("#username_validation").html(result.error_message);
            }
            else {
                $("#username_validation").html(result.success_message);
            }
        },
        error : function (result) {
            $("#username_validation").html(result.request_error)
        }
    });
});

$('#password, #confirm_password').on('keyup',function () {
    if($('#password').val() != $('#confirm_password').val())
    {
        $('#validation_msg').html('Passwords do not match!');
    }
    else
    {
        $('#validation_msg').html('');
    }
});

function checkIsOwner()
{
    checkbox = document.getElementById("isOwner");
    if (checkbox.checked)
    {
        checkbox.value = 'True';
        console.log(checkbox.value);
    }

}

function changeState()
{
    checkbox = document.getElementById("multipleFlats");
    if(checkbox.checked)
    {
        console.log("TRUE");
        checkbox.value = 'True';
        $('#divFlat2').css('visibility', 'visible');
    }
    else
    {
        console.log("FALSE");
        checkbox.value = 'False';
        $('#divFlat2').css('visibility', 'hidden');
    }
}
