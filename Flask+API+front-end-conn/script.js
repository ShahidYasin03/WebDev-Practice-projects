document.getElementById("studentForm").addEventListener("submit", function (e) {
  e.preventDefault(); // stop page reload (VERY IMPORTANT)

  const data = {
    name: document.getElementById("name").value,
    job_profile: document.getElementById("job").value,
    phone: document.getElementById("phone").value,
  };

  fetch("http://127.0.0.1:5000/write", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(data),
  })
    .then((res) => res.json())
    .then((response) => {
      document.getElementById("msg").innerText =
        response.message || response.error;
      document.getElementById("studentForm").reset();
      fetch("http://127.0.0.1:5000/read")
        .then((res) => res.json())
        .then((data) => {
          const list = document.getElementById("list");

          data.forEach((item) => {
            const li = document.createElement("li");
            li.textContent = `${item[0]} - ${item[1]} - ${item[2]}`;
            list.appendChild(li);
          });
        })
        .catch((err) => console.error(err));
    })
    .catch((err) => console.error(err));
});
