const form = document.getElementById("login-form");

async function sendLoginData(form: HTMLFormElement) {
  const formData = new FormData(form);
  try {
    const response = await fetch("", {
      method: "POST",
      body: formData,
    });
    console.log(await response.json());
  } catch (e) {
    console.log(e);
  }
}

form?.addEventListener("submit", (e) => {
  e.preventDefault();
});
