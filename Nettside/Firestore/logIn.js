import {
  getAuth,
  createUserWithEmailAndPassword,
  signInWithEmailAndPassword,
} from "https://www.gstatic.com/firebasejs/9.15.0/firebase-auth.js";

import { initializeApp } from "https://www.gstatic.com/firebasejs/9.15.0/firebase-app.js";
import {
  getFirestore,
  collection,
  getDocs,
  addDoc,
  deleteDoc,
  serverTimestamp,
} from "https://www.gstatic.com/firebasejs/9.15.0/firebase-firestore.js";
// TODO: Add SDKs for Firebase products that you want to use
// https://firebase.google.com/docs/web/setup#available-libraries

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

// let toggleVisibility = document.getElementById("passwordToggle");
// let passwordVisible = document.getElementById("passwordVisibility");
// passwordVisible.addEventListener("check", passwordToggle);
// function passwordToggle() {
//   if (toggleVisibility.type === "password") {
//     toggleVisibility.type = "text";
//   } else {
//     toggleVisibility.type = "password";
//   }
// }

// Initialize Firebase
const app = initializeApp(firebaseConfig);
const db = getFirestore(app); //En referanse til databasen vår

//Det som skjer når man trykker login
let text_login = document.getElementById("login");
let text_register = document.getElementById("register");
let text_btn = document.getElementById("btn");

let loginbtnEl = document.getElementById("loginButton");
loginbtnEl.addEventListener("click", login);

function login() {
  text_login.style.left = "50px";
  text_register.style.left = "450px";
  text_btn.style.left = "0px";
}

let registerBtnEl = document.getElementById("registerButton");
registerBtnEl.addEventListener("click", register);

function register() {
  text_login.style.left = "-400px";
  text_register.style.left = "50px";
  text_btn.style.left = "110px";
}

let registerUserEl = document.getElementById("registerUser");
registerUserEl.addEventListener("click", registerUser);

function registerUser() {
  let userInput = document.querySelector("#userInput").value
  let emailInput = document.querySelector("#emailInput").value;
  let passwordInput = document.querySelector("#passwordInput").value;
  
  auth
    .createUserWithEmailAndPassword(emailInput, passwordInput)
    .then(async () => {
      let user = auth.currentUser;

      let userData = {
        
        username: userInput,
        email: emailInput

      };

      await dataBase
        .collection("users")
        .doc(user.uid)
        .set(userData)
        .then(() => {
          location.href = "firestore.html";
          
        });
    })

    .catch(() => {
      alert("Ugyldig brukerinformasjon. Prøv igjen");
    });
}



let loginUserEl = document.getElementById("loginUser");
loginUserEl.addEventListener("click", logInUser);

function logInUser() {
  let emailInput = document.querySelector("#emailInputLogin").value;
  let passwordInput = document.querySelector("#passwordToggle").value;

  auth
    .signInWithEmailAndPassword(emailInput, passwordInput)
    .then((userCredential) => {
 
      successfulLogIn(userCredential)

      location.href = "firestore.html";
    })
    .catch(() => {
      alert("Ugyldig brukerinformasjon. Prøv igjen");
    });
}
let user = "";
function successfulLogIn(userCredential) {
  user = userCredential.user;

}
