const url = window.location.href

function submit(formName) {
    var elements = document.forms[formName].elements;

    var json = {};

    for (i = 0; i < elements.length; i++) {
        if (elements[i].value.length != 0) json[elements[i].name] = elements[i].value;
        else {
            alert("Cannot have empty field");
            return;
        }
    }

    console.log(json)

    fetch(url, {
        method: 'POST',
        headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(json)
    })
}