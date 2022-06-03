auth.onAuthStateChanged(() => {
  if (!auth.currentUser) {
    location.href = "index.html";
  }
});
