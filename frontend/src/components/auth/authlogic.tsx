export async function sendLoginData(form: FormData) {
  try {
    const response = await fetch("http://127.0.0.1:8000/login", {
      method: "POST",
      body: form,
    });
    console.log(await response.json());
  } catch (e) {
    console.log(e);
  }
}

export async function sendRegisterData(form: FormData) {
  try {
    const response = await fetch("http://127.0.0.1:8000/register", {
      method: "POST",
      body: form,
    });
    console.log(await response.json());
  } catch (e) {
    console.log(e);
  }
}
