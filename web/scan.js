let caughtCodes = [];


class DTCcode {
    constructor(code, severity) {
        this.code = code;
        this.severity = severity;

        // do something here to get code desc
        this.desc = null

    }
}


let addCode = (cd, sev) => {
    let newCode = DTCcode(cd, sev);
    caughtCodes.push(newCode);

}

let scanToLocal = (codeList) => {
    for (i = 0; i<codeList.length; i++) {
        addCode(codeList[i].code, codeList[i].severity);
    }
    return 1;
}

let scanCodes = async (codeList) => {
    let add = await scanToLocal(codeList);

    let codeArea = document.getElementById("codeOut");
    caughtCodes.forEach(code => {
        let codeDisp = document.createElement("a");
        codeDisp.className = "code";
        codeDisp.innerHTML = code.code;
        codeArea.appendChild(codeDisp);
    });

}


let clearCodes = async () => {
    let codeArea = document.getElementById("codeOut");
    // send a call to server

    // wait for response

    caughtCodes.length = 0;
    codeArea.innerHTML = "";
    let noCode = document.createElement('h2');
    noCode.innerHTML = "No Codes";
    codeArea.appendChild(noCode);

}