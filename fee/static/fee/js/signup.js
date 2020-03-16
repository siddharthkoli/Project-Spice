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
