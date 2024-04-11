let user = "";
// import { initializeApp } from "https://www.gstatic.com/firebasejs/9.22.1/firebase-app.js";

// import {
//   getFirestore,
//   collection,
//   getDocs,
//   addDoc,
//   doc,
//   getDoc,
//   setDoc,
//   updateDoc,
//   serverTimestamp,
//   deleteDoc,
//   query,
//   orderBy,
//   limit,
//   where,
// } from "https://www.gstatic.com/firebasejs/9.22.1/firebase-firestore.js";

// import {
//   getAuth,
//   signOut,
//   onAuthStateChanged,
//   createUserWithEmailAndPassword,
//   signInWithEmailAndPassword,
//   updateProfile,
// } from "https://www.gstatic.com/firebasejs/9.22.1/firebase-auth.js";

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
let auth = firebase.auth();

function createNewUser() {
  let mail = document.querySelector("#mail").value;

  let passord = document.querySelector("#passord").value;
  auth
    .createUserWithEmailAndPassword(mail, passord)
    .then(async () => {
      let user = auth.currentUser;

      let userData = {
        email: mail,
        password: passord,
      };

      await dataBase
        .collection("brukere")
        .doc(user.uid)
        .set(userData)
        .then(() => {
          location.href = "tidslinje.html";
        });
    })

    .catch(() => {
      alert("Ugyldig brukerinformasjon. Prøv igjen");
    });
}

function sign_in() {
  let email = document.querySelector("#email").value;
  let password = document.querySelector("#password").value;

  auth
    .signInWithEmailAndPassword(email, password)
    .then((userCredential) => {
      successfulLogIn(userCredential);

      location.href = "tidslinje.html";
    })
    .catch(() => {
      alert("Ugyldig brukerinformasjon. Prøv igjen");
    });
}
function successfulLogIn(userCredential) {
  console.log(userCredential);
  user = userCredential.user;
}

function signOut() {
  auth.signOut().then(() => {});
  location.href = "logIn.html";
}

// import { initializeApp } from "https://www.gstatic.com/firebasejs/9.22.1/firebase-app.js";

// import {
//   getFirestore,
//   collection,
//   getDocs,
//   addDoc,
//   doc,
//   getDoc,
//   setDoc,
//   updateDoc,
//   serverTimestamp,
//   deleteDoc,
//   query,
//   orderBy,
//   limit,
//   where,
// } from "https://www.gstatic.com/firebasejs/9.22.1/firebase-firestore.js";

// import {
//   getAuth,
//   signOut,
//   onAuthStateChanged,
//   createUserWithEmailAndPassword,
//   signInWithEmailAndPassword,
//   updateProfile,
// } from "https://www.gstatic.com/firebasejs/9.22.1/firebase-auth.js";

// const app = initializeApp(firebaseConfig);
// const db = getFirestore(app);
// const auth = getAuth();

// const loginEmail = document.querySelector("#mail");
// const loginPassword = document.querySelector("#passord");

// async function register() {
//   let email = loginEmail.value;
//   let password = loginPassword.value;

//   createUserWithEmailAndPassword(auth, email, password)
//     .then((userCredential) => {
//       //signed in

//       const user = userCredential.user;
//       username = user.displayName;
//       updateProfile(auth.currentUser, {
//         displayName: loginUsername.value,
//       })
//         .then(() => {
//           // Profile updated!

//           console.log(user.displayName);
//         })
//         .catch((error) => {
//           // An error occurred
//         });
//     })

//     .catch((error) => {
//       const errorCode = error.code;

//       const errorMessage = error.message;
//     });
// }

// //login

// function login() {
//   let email = loginEmail.value;
//   let password = loginPassword.value;

//   signInWithEmailAndPassword(auth, email, password)
//     .then((userCredential) => {
//       //signed in

//       const user = userCredential.user;
//       console.log(user);
//       username = user.displayName;
//     })

//     .catch((error) => {
//       const errorCode = error.code;
//       const errorMessage = error.message;
//       alert("Feil brukernavn eller ");
//     });
// }

// //logout

// function logout() {
//   signOut(auth)
//     .then(() => {
//       //sign-out successful

//       sessionStorage.removeItem("uid");
//       checkIfLoggedInFast();
//     })
//     .catch((error) => {
//       alert(error);
//     });
// }

// //check if user is logged in

// let username = "";

// onAuthStateChanged(auth, (user) => {
//   if (user) {
//     //user is signed in

//     const uid = user.uid;
//     mainContent.style.display = "block";
//     loginContainer.style.display = "none";
//     sessionStorage.setItem("uid", uid);

//     username = user.displayName;
//   } else {
//     //user is signed out

//     mainContent.style.display = "none";
//   }
// });
