function genN(n) {
    let w = new Worker("worker.js");
    w.postMessage(n);
    w.onmessage = e => {
        console.log(e.data);
    }
}

genN(7);