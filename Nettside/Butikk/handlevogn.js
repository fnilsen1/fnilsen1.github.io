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

function signOut() {
  auth.signOut().then(() => {});
  location.href = "index.html";
}

// function vis_varer() {
//   let varer = document.querySelector(".varer");
//   varer.innerHTML = "";

//   dataBase
//     .collection("brukere")
//     .doc(auth.currentUser.uid)
//     .get()
//     .then((doc) => {
//       console.log(doc.data());
//       let cart = doc.data().cart;
//       document.querySelector("#antall").innerHTML = "Varer: " + cart.length;
//       var total_pris = 0;

//       for (i = 0; i < cart.length; i++) {
//         dataBase
//           .collection("produkter")
//           .doc(cart[i])
//           .get()
//           .then((doc) => {
//             total_pris += doc.data().pris;
//             console.log(total_pris);

//             let boks = document.createElement("div");
//             boks.classList = "boks";

//             let bilde = document.createElement("img");
//             bilde.classList = "bilder";
//             bilde.setAttribute("src", doc.data().bilde);

//             let pris = document.createElement("h1");
//             pris.innerHTML = doc.data().pris + " kr";

//             let knapp = document.createElement("button");
//             knapp.classList = "legg_til";
//             knapp.id = doc.id;
//             knapp.innerHTML = "Fjern vare";
//             knapp.setAttribute("onclick", "fjern_vare(this)");

//             boks.appendChild(bilde);
//             boks.appendChild(pris);
//             boks.appendChild(knapp);
//             varer.appendChild(boks);
//             document.querySelector("#total").innerHTML =
//               "Totalt: " + total_pris + " kr";
//           });
//       }
//     });
// }

// function fjern_vare(fjern) {
//   fjern.parentNode.remove();

//   dataBase
//     .collection("brukere")
//     .doc(auth.currentUser.uid)
//     .get()
//     .then((doc) => {
//       let cart = doc.data().cart;

//       const index = cart.indexOf(fjern.id);
//       if (index > -1) {
//         cart.splice(index, 1);
//       }

//       dataBase.collection("brukere").doc(auth.currentUser.uid).update({
//         cart: cart,
//       });
//       vis_varer();
//     });
// }

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
            { navn: "X-Man Bell Pyraminx", count: 0 },
            { navn: "gan_2x2", count: 0 },
            { navn: "mgc_2x2", count: 0 },
            { navn: "qiyi_thunderclap", count: 0 },
            { navn: "tengyun", count: 0 },
            { navn: "gan_pyraminx", count: 0 },
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
        console.log(antall);
        cart_varer += parseInt(cart[i].count);
        console.log(cart_varer);

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
