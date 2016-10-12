var image_array = new Array();

$(document).ready(function() {

    $("#input-image").change(function() {

        $("#add-post-image-form").submit();
    });

    $(".add-image-icon").click(function() {
        $("#input-image").click();
        return false;
    });

    $("#add-post-image-form").ajaxForm(function(data) {


        var json = jQuery.parseJSON(data);
        var html = "";
        var maxwidth = $(".div-post-item").width();
        var width = $(".div-collage").width();

        $.each( json, function( value ) {

          width += json[value].thumb_size[0];

          var source = "/media/image/tmp/"+json[value].thumb;
          var w = json[value].thumb_size[0];
          var h = json[value].thumb_size[1];
          var item = [source, w, h];

          image_array.push(item);

          var item = "<a href=\"#\" style=\"position:relative\"><div class=\"remove_attach_image\"></div><div class=\"attach_image\ add-file-icon\ add-image-icon\" style=\"background-image:url('/media/image/tmp/"+json[value].thumb+"'); width:147px; height:147px; float:left; background-position: center; background-size: cover;\"></div></a>";
          html = item;
          $("input[name='input-avatar-url']").val("/media/image/tmp/"+json[value].thumb);       
         });

        if (width < maxwidth) {
            $(".div-collage").css("width", width);
        }else {
            $(".div-collage").css("width", maxwidth);
        }

        $(".collage-image").html("");
        $(".collage-image").html($(".collage-image").html() + html);
        $(".avatar").hide();
        $(".add-image-icon").bind( "click", function() {
        $("#input-image").click();
        return false;            
        });
        bindImageAttach();
    });
});