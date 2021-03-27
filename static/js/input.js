var INPUTS = [];

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
    var inputText = "";
    for (i = 0; i < INPUTS.length; i++) {
        inputText = inputText + INPUTS[i];
    }

    var repetition = document.getElementById("repetitions").value.toString();
    var outString = "";

    for (i = 0; i < INPUTS.length; i++) {
        if (outString == ""){
            outString = INPUTS[i];
        } else {
            outString = outString + ", " + INPUTS[i];
        }
    }

    var temp = "";
    for (i = 0; i < repetition; i++) {
        temp = outString + " " + temp
    }

    document.getElementById("success-alert").innerHTML = "Output:";
    document.getElementById("output").innerHTML = temp;
}
