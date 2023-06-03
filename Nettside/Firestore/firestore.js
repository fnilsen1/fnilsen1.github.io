// Your web app's Firebase configuration
const firebaseConfig = {
  apiKey: "AIzaSyBBM_Ey_JtDxZNa-CCyz24NQ7bF2k05nnY",
  authDomain: "tempprosjekt12102022-9a0bd.firebaseapp.com",
  projectId: "tempprosjekt12102022-9a0bd",
  storageBucket: "tempprosjekt12102022-9a0bd.appspot.com",
  messagingSenderId: "109304422757",
  appId: "1:109304422757:web:b5f84ab3e3a237be1ac18c",
};


firebase.initializeApp(firebaseConfig);
let dataBase = firebase.firestore();
let auth = firebase.auth();



auth.onAuthStateChanged(() => {
  if (!auth.currentUser) {
    location.href = "logIn.html";
  }
});

console.log(auth);

//Endrer farge på navEl når du klikker på Gaming eller Sport
let header = document.getElementById("nav");
let btns = header.getElementsByClassName("navEl");
for (var i = 0; i < btns.length; i++) {
  btns[i].addEventListener("click", function () {
    var current = document.getElementsByClassName("active");
    current[0].className = current[0].className.replace(" active", "");
    this.className += " active";
  });
}


let forum_valg = "sport";

let sport = document.getElementById("sport");
sport.addEventListener("click", changeToSport);
let gaming = document.getElementById("gaming");
gaming.addEventListener("click", changeToGaming);

function changeToSport() {
  forum_valg = "sport"
  getMessages("sport");
  
}

function changeToGaming() {
  forum_valg = "gaming"
  getMessages("gaming");
}


document.querySelector("#add").addEventListener("click", forum_choice);

function forum_choice() {
  if (forum_valg == "sport") {
    addNewRowSport("sport");
  } else {
    addNewRowGaming("gaming");
  }
}


function getMessages(sporring) {

  
  let olEl = document.querySelector("#messageContainer");
  olEl.innerHTML = "";
  
  dataBase.collection(`${sporring}Messages`).get().then((snapshot) => {
 
    let dokumenter = snapshot.docs;
    dokumenter.forEach((doc) => {
      if(state == "yourPosts"){
        if(doc.data().from == user_name){
          let divEl = document.createElement("div");
          divEl.className = "messageEl";
          divEl.id = doc.id
       

      
          divEl.innerHTML =
            " From: " +
            doc.data().from +
            "<br>" +
            "Message: " +
            doc.data().message +
            "<br>" +
            "Posted: " +
            doc.data().timestamp+"<br>"+
            `<img src="Images/trash.png" alt="" class="trash" onclick="remove(this)">`;

          olEl.appendChild(divEl);

  
        }
      }



      else{
        let divEl = document.createElement("div");
        divEl.className = "messageEl";
        divEl.id = doc.id
  
        divEl.innerHTML =
          " From: " +
          doc.data().from +
          "<br>" +
          "Message: " +
          doc.data().message +
          "<br>" +
          "Posted: " +
          doc.data().timestamp;
        olEl.appendChild(divEl);
      }

    });
    
  });


}


getMessages("sport")



function addNewRowSport() {
  const now = new Date();
  const dateString = now.toLocaleDateString();
  const timeString = now.toLocaleTimeString();
  const dateTimeString = dateString + " " + timeString;

  let message = document.getElementById("message").value;

  dataBase
    .collection("users")
    .doc(auth.currentUser.uid)
    .get()
    .then((doc) => {
      let from = doc.data().username;
      dataBase.collection("sportMessages").add({
        from: from,
        message: message,
        timestamp: dateTimeString,
  
      });
      
  getMessages("sport");
    });



}

function addNewRowGaming() {
  const now = new Date();
  const dateString = now.toLocaleDateString();
  const timeString = now.toLocaleTimeString();
  const dateTimeString = dateString + " " + timeString;

  let message = document.getElementById("message").value;

  dataBase
    .collection("users")
    .doc(auth.currentUser.uid)
    .get()
    .then((doc) => {
      let from = doc.data().username;
      dataBase.collection("gamingMessages").add({
        from: from,
        message: message,
        timestamp: dateTimeString,
  
      });
      
  getMessages("gaming");
    });



}

let state;
function updateQuery(){
  const selectElement = document.getElementById('select');
  state = selectElement.value;
  

  dataBase
  .collection("users")
  .doc(auth.currentUser.uid)
  .get()
  .then((doc) => {
  user_name = doc.data().username
  
  });
getMessages(forum_valg)
  
  }

function remove(e){
 id = e.parentNode.id
let collection = forum_valg+"Messages"
dataBase.collection(collection).doc(id).delete()
element = document.getElementById(id)
element.remove()
}

let user_name = ""
document.querySelector("#change").addEventListener("click", changeName);
function changeName(){
let new_name = document.getElementById("middle").value
user_name = new_name
dataBase.collection("users").doc(auth.currentUser.uid).update({
username: new_name
});  

}




let logOutEl = document.getElementById("logOut");
logOutEl.addEventListener("click", signOut);

function signOut() {
  auth.signOut().then(() => {});
  location.href = "logIn.html";
}



