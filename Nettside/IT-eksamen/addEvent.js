const firebaseConfig = {
    apiKey: "AIzaSyCf9W4O9mbgNAUD72zE2rdyYP8-zPlMevM",
    authDomain: "eksamenprosjekt.firebaseapp.com",
    projectId: "eksamenprosjekt",
    storageBucket: "eksamenprosjekt.appspot.com",
    messagingSenderId: "136631219988",
    appId: "1:136631219988:web:669fc32ae52d0834997401",
  };
  

  firebase.initializeApp(firebaseConfig);
  let dataBase = firebase.firestore();
  
function leggTilHendelse() {
let event = document.getElementById("event").value
let start = document.getElementById("start").value
dataBase.collection("tidslinje").add({
    event: event,
    start: start    
});
}


