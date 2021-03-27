var INPUTS = [];

function addRowCol() {
    document.getElementById("matrix").innerHTML = "";
    rows = document.getElementById("rows").value.toString();
    cols = document.getElementById("cols").value.toString();

    for(x = 0; x < rows; x++) {
        var span = document.createElement("span");
        for(y = 0; y < cols; y++) {
            var col = y.toString();
            var row = x.toString()
            var label = document.createElement("label");
            label.innerHTML = "Row: " + row + ", Col: " + col;
            var input = document.createElement("input");
            var id = y.toString() + "," + x.toString();
            input.id = id;
            span.appendChild(label);
            span.appendChild(input);
        }
        var br = document.createElement("br");
        document.getElementById("matrix").appendChild(br);
        document.getElementById("matrix").appendChild(span);
    }

    document.getElementById("dimensions-tag").innerHTML = rows + ", " + cols
}

function addInput() {
    var inputText = document.getElementById("pattern").value;
    if (inputText == "") {
        alert("Empty string detected!")
        return
    }

    document.getElementById("pattern").value = "";
    INPUTS.push(inputText);
    var output = "";
    for (i = 0; i < INPUTS.length; i++) {
        if (output == ""){
            output = INPUTS[i];
        } else {
            output = output + ", " + INPUTS[i];
        }
    }
    document.getElementById("entry").innerHTML = output;
}

function reset() {
    INPUTS = [];
    document.getElementById("entry").innerHTML = "";
}

function patternTest() {
    if (INPUTS.length == 0) {
        alert("No inputs added!")
        return
    }

    var inputText = "";
    for (i = 0; i < INPUTS.length; i++) {
        inputText = inputText + INPUTS[i];
    }

    var outString = "";

    for (i = 0; i < INPUTS.length; i++) {
        if (outString == ""){
            outString = INPUTS[i];
        } else {
            outString = outString + ", " + INPUTS[i];
        }
    }

    document.getElementById("success-alert").innerHTML = "Output:";
    document.getElementById("output").innerHTML = outString;
}
