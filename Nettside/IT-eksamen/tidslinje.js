
function visHendelser() {
    document.querySelector(".timeline").innerHTML = "";
    let obj = {};
    dataBase
      .collection("tidslinje")
      .orderBy("start", "asc")
      .get()
      .then((snapshot) => {
        let dokumenter = snapshot.docs;
     
  
        for (let i = 0; i < dokumenter.length; i++) {
          let start = dokumenter[i].data().start;
          let event = dokumenter[i].data().event;
  
          if (obj.hasOwnProperty(start)) {
            obj[start].push(event);
          } else {
            obj[start] = [event];
          }
        }
  
        console.log(obj);
  
        let counter = 0;
        Object.keys(obj).forEach((key) => {
            console.log("sup");
          let div1 = document.createElement("div");
      
          let div2 = document.createElement("div");
          div2.setAttribute("class", "content");
  
          // Sjekker om det er et partall
          if (counter % 2 === 0) {
            div1.setAttribute("class", "left container");
          }
          // Oddetall
          else {
            div1.setAttribute("class", "right container");
          }
  
          let container = document.querySelector(".timeline");
  
          let text = "";
         
            text = "<h2>" + key + "</h2>" + " <br> ";

            for (let i = 0; i < obj[key].length; i++) {
              text += "<p>" + obj[key][i] + "</p>" + " <br> ";
            }
           
          
          div2.innerHTML = text;
          div1.appendChild(div2);
          container.appendChild(div1);
  
          counter++;
        });
      });
  }

visHendelser()

