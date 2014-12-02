function(modal) {
    modal.respond('deleted', {{ response|safe }});
    modal.close();
}