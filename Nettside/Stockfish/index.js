const stockfish = new Worker("stockfish/src/stockfish.js");
stockfish.postMessage('uci');

stockfish.onmessage = function (event) {
    if (event.data === 'uciok') {
      // Stockfish is ready to use.
    }
  };

const fenString = 'rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1';
stockfish.postMessage('position fen ' + fenString);

stockfish.postMessage('go depth 20');

stockfish.onmessage = function (event) {
  const message = event.data;

  if (message.startsWith('bestmove')) {
    const bestMove = message.split(' ')[1];
    // Use the best move.
  } else if (message.startsWith('info')) {
    const match = message.match(/score (cp|mate) (-?\d+)/);
    const scoreType = match[1];
    const scoreValue = parseInt(match[2]);
    // Use the score value.
  }
};