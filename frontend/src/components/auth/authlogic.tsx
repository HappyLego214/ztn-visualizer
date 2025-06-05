const form = document.getElementById("login-form");

export async function sendLoginData(form: FormData) {
  try {
    const response = await fetch("http://127.0.0.1:8000/test", {
      method: "POST",
      body: form,
    });
    console.log(await response.json());
  } catch (e) {
    console.log(e);
  }
}

form?.addEventListener("submit", (e) => {
  e.preventDefault();
  console.log(e);
});
