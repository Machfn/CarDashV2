
let caughtCodes = [];
let codeDetect = true;


function loads() {
    let mesd = document.getElementById("message");
    eel.startf()(function(outd) {
        mesd.innerHTML = outd;
    })
    // eel.startf("hello");
}


let addCode = (DTC) => {
    caughtCodes.push(DTC);
}

let DTCcode = (code, severity) => {
    let wrn = document.getElementById("warning");
    wrn.style.display = "flex"

    setTimeout(() => {
        wrn.style.display = "none";
    }, 2500)
}


 setInterval(() => {
    if (caughtCodes.length > 0) {
        document.querySelector("html").style.backgroundColor = "rgb(54, 7, 7)"
    } else {
        document.querySelector("html").style.backgroundColor = "darkslategrey"
    }
}, 1500)
