function sendData() {
    var mainDiv = document.getElementById(''),
    id = mainDiv.getElementsByTagName('input')[0];
    $.post('/edit', {xml: id });
}
