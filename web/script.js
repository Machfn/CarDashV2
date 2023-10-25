function loads() {
    let mesd = document.getElementById("message");
    eel.startf()(function(outd) {
        mesd.innerHTML = outd;
    })
    // eel.startf("hello");
}