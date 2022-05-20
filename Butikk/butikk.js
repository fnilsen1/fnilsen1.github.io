let user = "";
const firebaseConfig = {
  apiKey: "AIzaSyCzPQEI2St1ZBJwf-VktojbyZP9I9nEf-A",
  authDomain: "butikk-758aa.firebaseapp.com",
  projectId: "butikk-758aa",
  storageBucket: "butikk-758aa.appspot.com",
  messagingSenderId: "235329400437",
  appId: "1:235329400437:web:2bd2b1956c773a7d93123c",
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
        Email: mail,
        cart: [],
      };

      await dataBase
        .collection("brukere")
        .doc(user.uid)
        .set(userData)
        .then(() => {
          location.href = "butikk.html";
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

      location.href = "butikk.html";
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
  location.href = "index.html";
}

function vis_varer(selection) {
  let varer = document.querySelector(".varer");
  varer.innerHTML = "";

  selection.get().then((snapshot) => {
    snapshot.forEach((doc) => {
      console.log(doc.data());

      let varer = document.querySelector(".varer");

      let boks = document.createElement("div");
      boks.classList = "boks";

      // let overlay = document.createElement("div");
      // productEl.id = "overlay1";

      let bilde = document.createElement("img");
      bilde.classList = "bilder";
      bilde.setAttribute("src", doc.data().bilde);

      let pris = document.createElement("h1");
      pris.innerHTML = doc.data().pris + " kr";

      // let categoryEl = document.createElement("h2");
      // categoryEl.innerHTML = doc.data().category;
      // categoryEl.classList = "product_category";

      let knapp = document.createElement("button");
      knapp.classList = "legg_til";
      knapp.id = doc.id;
      knapp.innerHTML = "Legg til i handlevogn";
      knapp.setAttribute("onclick", "legg_til(this)");

      let overlay = document.createElement("div");
      overlay.classList = "overlay";

      overlay.innerHTML =
        doc.data().navn +
        "<br>" +
        "Dimensjoner: " +
        doc.data().dimensjoner +
        "<br>" +
        "Pris: " +
        doc.data().pris +
        " kr";

      boks.appendChild(bilde);
      boks.appendChild(pris);
      boks.appendChild(knapp);
      boks.appendChild(overlay);

      varer.appendChild(boks);
    });
  });
}

// let categorySelectorEl = document.getElementById("select_category");

// let priceSelectorEl = document.getElementById("select_price");

let query = dataBase.collection("produkter");
vis_varer(query);

function sorter(valg) {
  let query = dataBase.collection("produkter");

  if (valg == "lav_hoy") {
    query = dataBase.collection("produkter").orderBy("pris", "asc");
  } else if (valg == "hoy_lav") {
    query = dataBase.collection("produkter").orderBy("pris", "desc");
  } else if (valg == "2x2") {
    query = query.where("kategori", "==", "2x2");
  } else if (valg == "3x3") {
    query = query.where("kategori", "==", "3x3");
  } else if (valg == "pyraminx") {
    query = query.where("kategori", "==", "pyraminx");
  }

  vis_varer(query);
}

function legg_til(vare) {

  dataBase
    .collection("brukere")
    .doc(auth.currentUser.uid)
    .get()
    .then((doc) => {
      console.log(doc.data());
      let cart = doc.data().cart;
      cart.push(vare.id);

      console.log(cart);

      dataBase.collection("brukere").doc(auth.currentUser.uid).update({
        cart: cart,
      });
    });
}
