auth.onAuthStateChanged(() => {
  if (!auth.currentUser) {
    location.href = "logIn.html";
  }
});
