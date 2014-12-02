function(modal) {
    modal.respond('captionChosen', {{ response|safe }});
    modal.close();
}
