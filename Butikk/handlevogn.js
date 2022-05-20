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

auth.onAuthStateChanged(() => {
  if (!auth.currentUser) {
    location.href = "index.html";
  } else vis_varer();
});

function hovedside() {
  location.href = "butikk.html";
}

function vis_varer() {
  let varer = document.querySelector(".varer");
  varer.innerHTML = "";

  dataBase
    .collection("brukere")
    .doc(auth.currentUser.uid)
    .get()
    .then((doc) => {
      console.log(doc.data());
      let cart = doc.data().cart;
      document.querySelector("#antall").innerHTML = "Varer: " + cart.length;
      var total_pris = 0;

      for (i = 0; i < cart.length; i++) {
        dataBase
          .collection("produkter")
          .doc(cart[i])
          .get()
          .then((doc) => {
            total_pris += doc.data().pris;
            console.log(total_pris);

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
            knapp.innerHTML = "Fjern vare";
            knapp.setAttribute("onclick", "fjern_vare(this)");

            boks.appendChild(bilde);
            boks.appendChild(pris);
            boks.appendChild(knapp);
            varer.appendChild(boks);
            document.querySelector("#total").innerHTML =
              "Totalt: " + total_pris + " kr";
          });
      }
    });
}

function fjern_vare(fjern) {
  fjern.parentNode.remove();

  dataBase
    .collection("brukere")
    .doc(auth.currentUser.uid)
    .get()
    .then((doc) => {
      let cart = doc.data().cart;

      const index = cart.indexOf(fjern.id);
      if (index > -1) {
        cart.splice(index, 1);
      }

      dataBase.collection("brukere").doc(auth.currentUser.uid).update({
        cart: cart,
      });
      vis_varer();
    });
}

function kjop_alt() {
  let alle_varer = [];
  dataBase.collection("brukere").doc(auth.currentUser.uid).update({
    cart: alle_varer,
  });
  document.querySelector("#total").innerHTML = "Totalt: 0 kr";
  vis_varer();
  // alert("Vellykket kjøp");
}
