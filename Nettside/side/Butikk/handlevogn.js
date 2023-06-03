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

auth.onAuthStateChanged(() => {
  if (!auth.currentUser) {
    location.href = "logIn.html";
  } else vis_varer();
});

function hovedside() {
  location.href = "butikk.html";
}

function signOut() {
  auth.signOut().then(() => {});
  location.href = "index.html";
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
  dataBase
    .collection("brukere")
    .doc(auth.currentUser.uid)
    .get()
    .then((doc) => {
      let info = {
        Email: doc.data().Email,
        cart: doc.data().cart,
      };

      console.log(doc.data().cart);

      dataBase
        .collection("ordre")
        .doc()
        .set(info)
        .then(() => {
          let alle_varer = [
            { navn: "arsenalAwayKit23", count: 0 },
            { navn: "adidasPredatorFreak", count: 0 },
            { navn: "barcelonaHomeKit23", count: 0 },
            { navn: "nikeMercurialVapor", count: 0 },
            { navn: "selectFotballEliteserien", count: 0 },
            { navn: "selectFotballSuperligax", count: 0 },
            { navn: "adidasVmFotball", count: 0 },
            { navn: "realmadridHomeKit23", count: 0 },
            { navn: "pumaFuture", count: 0 },
          ];

          dataBase
            .collection("brukere")
            .doc(auth.currentUser.uid)
            .get()
            .then(async () => {
              dataBase.collection("brukere").doc(auth.currentUser.uid).update({
                cart: alle_varer,
              });

              await dataBase
                .collection("brukere")
                .doc(auth.currentUser.uid)
                .get()
                .then(() => {
                  vis_varer();
                  location.reload();
                });
            });
        });
    });
}

function vis_varer() {
  let varer = document.querySelector(".varer");
  varer.innerHTML = "";
  let cart_varer = parseInt(0);
  let total_pris = parseInt(0);
  dataBase
    .collection("brukere")
    .doc(auth.currentUser.uid)
    .get()
    .then((doc) => {
      // console.log(doc.data());
      let cart = doc.data().cart;
      // document.querySelector("#antall").innerHTML = "Varer: " + cart.length;
      // var total_pris = 0;

      for (i = 0; i < cart.length; i++) {
        let antall = cart[i].count;
  
        cart_varer += parseInt(cart[i].count);
       

        document.querySelector("#antall").innerHTML = "Varer: " + cart_varer;

        if (cart[i].count > 0) {
          dataBase
            .collection("produkter")
            .doc(cart[i].navn)
            .get()
            .then((doc) => {
              let boks = document.createElement("div");
              boks.classList = "boks";

              let bilde = document.createElement("img");
              bilde.classList = "bilder";

              bilde.setAttribute("src", doc.data().bilde);

              let pris = document.createElement("h1");
              pris.innerHTML = doc.data().pris * antall + " kr";

              total_pris += parseInt(doc.data().pris * antall);

              let tall = document.createElement("h1");
              tall.innerHTML = "Antall:";
              document.querySelector("#total").innerHTML =
                "Totalt: " + total_pris + " kr";

              let input = document.createElement("input");
              input.setAttribute("type", "number");
              input.setAttribute("min", "0");
              input.setAttribute("onchange", "endre(this)");
              input.id = doc.id;

              input.value = antall;

              boks.appendChild(bilde);
              boks.appendChild(pris);
              boks.appendChild(tall);
              boks.appendChild(input);

              varer.appendChild(boks);
            });
        } else {
          document.querySelector("#total").innerHTML =
            "Totalt: " + total_pris + " kr";
        }
      }
    });
}

function endre(vare) {
  let fjern = vare.parentNode.remove();
  let verdi = vare.value;
  let cube = vare.id;

  dataBase
    .collection("brukere")
    .doc(auth.currentUser.uid)
    .get()
    .then((doc) => {
      let vogn = doc.data().cart;

      if (verdi === 0) {
        fjern();
        vogn.forEach((item) => {
          if (item.navn === cube) {
            item.count = parseInt(0);
            vis_varer();
          }
        });
      } else {
        vogn.forEach((item) => {
          console.log(item.navn);
          if (item.navn === cube) {
            item.count = parseInt(verdi);
          }
        });

        dataBase
          .collection("brukere")
          .doc(auth.currentUser.uid)
          .get()
          .then(async () => {
            dataBase.collection("brukere").doc(auth.currentUser.uid).update({
              cart: vogn,
            });

            await dataBase
              .collection("brukere")
              .doc(auth.currentUser.uid)
              .get()
              .then(() => {
                vis_varer();
              });
          });
      }
    });
}
