
let caughtCodes = [];
let codeDetect = true;
let redline;
fetch("/config/carInfo.json")
    .then((response) => response.json())
    .then((json) => {
        redline = json.vehicle.redline;
    });


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
        DTCcode();
    } else {
        document.querySelector("html").style.backgroundColor = "darkslategrey"
    }
}, 1500)


// uptop rpm controller
let fil = document.getElementById("filler");
let acRpm = document.getElementById("live-rpm");
let updRPM = (rpm) => {
    fil.style.width = (rpm / redline) * 100 + "%";
    acRpm.innerHTML = rpm;
}
