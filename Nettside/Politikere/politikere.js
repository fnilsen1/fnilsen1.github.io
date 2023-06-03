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
  


  function visPolitikere() {

    const selectElement = document.getElementById('select');
    sporring = selectElement.value;
    
    let tbody = document.querySelector("#tbody");
    tbody.innerHTML = "";
    
    dataBase.collection("politikere").orderBy("etternavn", "asc").get().then((snapshot) => {
   
      let dokumenter = snapshot.docs;
      dokumenter.forEach((doc) => {
        if(sporring=="Alle"){
            let tr = document.createElement("tr");
         
  
            tr.innerHTML =
            "<td>"+ doc.data().fornavn+ "</td>"+
            "<td>"+ doc.data().etternavn+ "</td>"+
            "<td>"+ doc.data().partiforkortelse+ "</td>"+
            "<td>"+ doc.data().krets+ "</td>"

            tbody.appendChild(tr);
  
        }
    
        else if(sporring==doc.data().partiforkortelse){
                
            let tr = document.createElement("tr");
         
  
            tr.innerHTML =
            "<td>"+ doc.data().fornavn+ "</td>"+
            "<td>"+ doc.data().etternavn+ "</td>"+
            "<td>"+ doc.data().partiforkortelse+ "</td>"+
            "<td>"+ doc.data().krets+ "</td>"

            tbody.appendChild(tr);
  
        }
  
      });
      
    });
  
  
  }
  

  
  visPolitikere()
  
