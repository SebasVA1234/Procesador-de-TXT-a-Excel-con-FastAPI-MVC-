import React, { useState } from 'react';

function App() {
  const [files, setFiles] = useState([]);
  const [result, setResult] = useState("");

  const handleSubmit = async (e) => {
    e.preventDefault();
    const formData = new FormData();
    for (let file of files) {
      formData.append("files", file);
    }

    try {
      const res = await fetch("http://localhost:8000/upload-folder/", {
        method: "POST",
        body: formData
      });
      const json = await res.json();
      setResult(JSON.stringify(json, null, 2));
    } catch (err) {
      setResult("Error al enviar archivos: " + err.message);
    }
  };

  return (
    <div style={{ padding: "2rem" }}>
      <h1>Subir archivos .xlsx</h1>
      <form onSubmit={handleSubmit}>
        <input
          type="file"
          multiple
          accept=".xlsx"
          onChange={e => setFiles(e.target.files)}
        />
        <button type="submit">Enviar</button>
      </form>
      <pre>{result}</pre>
    </div>
  );
}

export default App;
