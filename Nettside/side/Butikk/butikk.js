let user = "";
const firebaseConfig = {
  apiKey: "AIzaSyCCI0U5q0adkSFkK8FmvfH2tsOm2Z2vsUo",
  authDomain: "footybooty-1d6a4.firebaseapp.com",
  projectId: "footybooty-1d6a4",
  storageBucket: "footybooty-1d6a4.appspot.com",
  messagingSenderId: "960422536774",
  appId: "1:960422536774:web:0d2794d3de598237e74c47",
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
        cart: [            { navn: "arsenalAwayKit23", count: 0 },
        { navn: "adidasPredatorFreak", count: 0 },
        { navn: "barcelonaHomeKit23", count: 0 },
        { navn: "nikeMercurialVapor", count: 0 },
        { navn: "selectFotballEliteserien", count: 0 },
        { navn: "selectFotballSuperligax", count: 0 },
        { navn: "adidasVmFotball", count: 0 },
        { navn: "realmadridHomeKit23", count: 0 },
        { navn: "pumaFuture", count: 0 },
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
  location.href = "logIn.html";
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
    knapp.setAttribute("onclick", "leggTil(this)");

    let overlay = document.createElement("div");
    overlay.classList = "overlay";

    overlay.innerHTML =
      doc.data().navn +
      "<br>" +
      "Størrelse: " +
      doc.data().storrelse +
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

  dataBase
    .collection("brukere")
    .doc(auth.currentUser.uid)
    .get()
    .then((doc) => {
      // console.log(doc.data());
      let cart = doc.data().cart;
      let cartVarer = 0
      // document.querySelector("#antall").innerHTML = "Varer: " + cart.length;
      // var total_pris = 0;

      for (i = 0; i < cart.length; i++) {
        cartVarer += parseInt(cart[i].count);
    
        document.querySelector(".cartCount").innerHTML = cartVarer;


      }
    });
}

let produkt_array = [];
let alle_produkter = [];
dataBase
  .collection("produkter")
  .get()
  .then((querySnapshot) => {
   
    alle_produkter = [...querySnapshot.docs];
    produkt_array = alle_produkter;
  
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

function sorterPris(type) {
  produkt_array.sort((a, b) => {
    if (type === "lav_hoy") {
      return a.data().pris - b.data().pris;
    } else {
      return b.data().pris - a.data().pris;
    }
  });
  vis_varer();
}

let antall_varer = 0
function leggTil(vare) {
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

      dataBase
      .collection("brukere")
      .doc(auth.currentUser.uid)
      .get()
      .then((doc) => {
   
        let cart = doc.data().cart;
        let cartVarer = 0
 
  
        for (i = 0; i < cart.length; i++) {
          cartVarer += parseInt(cart[i].count);
      
          document.querySelector(".cartCount").innerHTML = cartVarer;
  
  
        }
      });

    });

}


