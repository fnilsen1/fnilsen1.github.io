// Your web app's Firebase configuration
const firebaseConfig = {
    apiKey: "AIzaSyChbMgD7aJZYGb-uuQe8Js9loMjfO78CYM",
    authDomain: "politikerprosjekt.firebaseapp.com",
    projectId: "politikerprosjekt",
    storageBucket: "politikerprosjekt.appspot.com",
    messagingSenderId: "10536170458",
    appId: "1:10536170458:web:9edbfd2d45f359d8ef06e3"
  };
  
  
  firebase.initializeApp(firebaseConfig);
  let dataBase = firebase.firestore();
  let auth = firebase.auth();

function nyPolitiker() {
    let fornavn = document.getElementById("fornavn").value;
    let etternavn = document.getElementById("etternavn").value;
    let parti = document.getElementById("parti").value;
    let krets = document.getElementById("krets").value;

    dataBase.collection("politikere").add({
        fornavn: fornavn,
        etternavn: etternavn,
        partiforkortelse: parti,
        valgkrets: krets

      });
  
  
  }
  