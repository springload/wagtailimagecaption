$(function() {

    // $('.richtext [contenteditable="false"]').each(function() {
    //     insertRichTextDeleteControl(this);
    // });

    $('.richtext [data-embedtype="image"]').each(function() {
        insertRichTextCaptionImageControl(this);
    });

    $('.richtext [data-embedtype="image"][data-caption]').each(function() {
        insertRichTextEditCaptionImageControl(this);
    });
    

});

// Set delete control for embeds which will actually remove the element from the DB. 
// On hold since the fact of removing it from the editor doesn't mean it would be removed from the RichTextField necessarily.
// function insertRichTextDeleteControl(elem) {
//     var a = $('<a class="icon icon-cross text-replace delete-control">Delete</a>');
//     $(elem).addClass('rich-text-deletable').prepend(a);
//     a.click(function() {
//         if ($(elem).hasClass("embed-placeholder") && $(elem).attr("data-type") === "video") {
//             var id = $(elem).attr("id");
//             return ModalWorkflow({
//                 url: window.removersUrls.embedsRemover + '?id=' + id,
//                 responses: {
//                     response: function(response) {
//                         if (response.status) {
//                             $(elem).fadeOut(function() {
//                                 $(elem).remove();
//                             });
//                         }
//                     }
//                 }
//             });
//         }
//         else {
//             $(elem).fadeOut(function() {
//                 $(elem).remove();
//             });
//         }
//     });
// }

// Set image icon to set caption to embedded images
function insertRichTextCaptionImageControl(elem) {
    // Inherit alignment class, this can be probably improved
    var align_class = "";
    if ($(elem).hasClass("right")) {
        align_class = "right";
    }
    else if ($(elem).hasClass("left")) {
        align_class = "left";
    }
    var a = $('<a class="icon icon-edit text-replace captionimage-control ' + align_class + '">Set image caption</a>');
    $(elem).addClass('richtext-image-editable').prepend(a);
    $(a).insertBefore($(elem));
    a.click(function() {
        var id = $(elem).attr("data-id");
        return ModalWorkflow({
            url: window.chooserUrls.imageCaption + '?image_id=' + id,
            responses: {
                captionChosen: function(status) {
                    // console.log(status);
                    // $($(elem).children("img").get(0)).attr("src", $(imageData.html).attr("src"));
                }
                //,
                // newEmbed: function(embed) {
                //     $(elem).attr("data-posterimage", embed);
                //     insertRichTextVideoEmbedDeleteImageControl(elem);
                // }
            }
        });
    });
}

// Set image icon to remove poster images from embed elements (only those whose type is Video)
function insertRichTextEditCaptionImageControl(elem) {
    // var a = $('<a class="icon icon-undo text-replace posterimage-delete-control">Remove poster image</a>');
    // $(elem).addClass('rich-text-delete-editable').prepend(a);
    // a.click(function() {
    //     var id = $(elem).attr("data-posterimage");
    //     return ModalWorkflow({
    //         url: window.removersUrls.posterimageRemover + '?id=' + id,
    //         responses: {
    //             deleted: function(response) {
    //                 // Set thumbnail url and remove icon
    //                 $($(elem).children("img").get(0)).attr("src", response.embed_thumbnail_url);
    //                 $(a).remove();
    //             }
    //         }
    //     });
    // });
}
