function(modal) {
    $('form.caption-form', modal.body).submit(function() {
        var formdata = new FormData(this);

        $.ajax({
            url: this.action,
            data: formdata,
            processData: false,
            contentType: false,
            type: 'POST',
            dataType: 'text',
            success: function(response){
                modal.loadResponseText(response);
            }
        });

        return false;
    });
    
    $('a.delete-caption').click(function(event) {
        event.preventDefault()
        $.ajax({
            url: this.href,
            type: 'GET',
            dataType: 'text',
            success: function(response){
                modal.loadResponseText(response);
            }
        });

        return false;
    });
}