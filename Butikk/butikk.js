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
        cart: [
          { navn: "X-Man Bell Pyraminx", count: 0 },
          { navn: "gan_2x2", count: 0 },
          { navn: "mgc_2x2", count: 0 },
          { navn: "qiyi_thunderclap", count: 0 },
          { navn: "tengyun", count: 0 },
          { navn: "gan_pyraminx", count: 0 },
        ],
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

function vis_varer() {
  let varer = document.querySelector(".varer");
  varer.innerHTML = "";
  produkt_array.forEach((doc) => {
    let varer = document.querySelector(".varer");

    let boks = document.createElement("div");
    boks.classList = "boks";

    let bilde = document.createElement("img");
    bilde.classList = "bilder";
    bilde.setAttribute("src", doc.data().bilde);

    let pris = document.createElement("h1");
    pris.innerHTML = doc.data().pris + " kr";

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
}

let produkt_array = [];
let alle_produkter = [];
dataBase
  .collection("produkter")
  .get()
  .then((querySnapshot) => {
    console.log(querySnapshot);
    alle_produkter = [...querySnapshot.docs];
    produkt_array = alle_produkter;
    console.log(produkt_array);
    vis_varer();
  });

function sorter(valg) {
  produkt_array = [];

  if (valg !== "alle") {
    alle_produkter.forEach((doc) => {
      if (doc.data().kategori === valg) produkt_array.push(doc);
    });
  } else {
    produkt_array = [...alle_produkter];
  }
  vis_varer();
}

function sorter_pris(type) {
  produkt_array.sort((a, b) => {
    if (type === "lav_hoy") {
      return a.data().pris - b.data().pris;
    } else {
      return b.data().pris - a.data().pris;
    }
  });
  vis_varer();
}

function legg_til(vare) {
  dataBase
    .collection("brukere")
    .doc(auth.currentUser.uid)
    .get()
    .then((doc) => {
      let vogn = doc.data().cart;
      vogn.forEach((item) => {
        if (item.navn === vare.id) {
          item.count++;
        }
      });

      dataBase.collection("brukere").doc(auth.currentUser.uid).update({
        cart: vogn,
      });
    });
}
